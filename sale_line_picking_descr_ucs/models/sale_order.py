# -*- coding: utf-8 -*-

from odoo import models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super().action_confirm()
        for order in self:
            if order.picking_ids:
                vals = {}
                if order.partner_invoice_id:
                    vals['sh_line_desc_partner_inv_id'] = order.partner_invoice_id.id
                if order.partner_id:
                    vals['sh_line_desc_partner_id'] = order.partner_id.id
                if vals:
                    order.picking_ids.sudo().write(vals)
        return res

