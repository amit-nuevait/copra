from odoo import fields, models, api, _
import xlrd
import base64


class ImportDocument(models.TransientModel):
    _name = 'import.document.wizard'
    _description = 'Import Document Wizard'
    
    name = fields.Char('name')
    file_upload = fields.Binary('Import File')

    def action_import_documents(self):
        binary_data = self.file_upload
        x = base64.decodestring(binary_data)
        workbook = xlrd.open_workbook(file_contents=x)
        sheet = workbook.sheet_by_index(0)
        num_rows = workbook.sheet_by_index(0).nrows
        for row in range(1,num_rows):
            product_default_code = sheet.cell_value(row, 0)
            document_name  = sheet.cell_value(row, 1)
            is_public_document = sheet.cell_value(row, 2)
            if product_default_code:
                prodcut_id = self.env['product.template'].search([('default_code','=',product_default_code)])
                document_id = self.env['ir.attachment'].search([('name','=',document_name)])
                if prodcut_id and document_id:
                    document_id.public = is_public_document
                    prodcut_id.write({'document_ids': [(4,document_id.id,0)]}) 