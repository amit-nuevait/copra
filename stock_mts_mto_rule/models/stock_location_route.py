# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class StockLocationRoute(models.Model):
    _inherit = "stock.location.route"

    auto_confirm_po = fields.Boolean(string="Auto Confirm Route", default=True)

    