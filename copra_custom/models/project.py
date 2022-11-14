from odoo import api, models, fields, _


class ProjectProject(models.Model):
    _inherit = "project.project"

    def _get_custom_so_count(self):
        for rec in self:
            rec.custom_so_count = self.env['sale.order'].search_count([('analytic_account_id', '=', rec.analytic_account_id.id)])

    custom_so_count = fields.Integer('Manual SO', compute='_get_custom_so_count')

    def action_view_custom_so(self):
        self.ensure_one()
        view_form_id = self.env.ref('sale.view_order_form').id
        tree_view_id = self.env.ref('sale.view_order_tree').id
        custom_so_ids = self.env['sale.order'].search([('analytic_account_id', '=', self.analytic_account_id.id)])
        action = {
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', custom_so_ids.ids)],
            'view_mode': 'tree,form',
            'name': _('Sale Order'),
            'res_model': 'sale.order',
            'context': {'default_analytic_account_id': self.analytic_account_id.id}
        }
        if len(custom_so_ids) == 1:
            action.update({'views': [(view_form_id, 'form')], 'res_id': custom_so_ids.id})
        else:
            action.update({'views': [(tree_view_id, 'tree'), (view_form_id, 'form')]})
        return action
