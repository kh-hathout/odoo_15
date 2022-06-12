# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    asset_depreciation_ids = fields.One2many('account.asset.depreciation.line', 'move_id',
                                             string='Assets Depreciation Lines')

    def button_cancel(self):
        for move in self:
            for line in move.asset_depreciation_ids:
                line.move_posted_check = False
        return super(AccountMove, self).button_cancel()

<<<<<<< HEAD
<<<<<<< HEAD
    def action_post(self):
        for move in self:
            for depreciation_line in move.asset_depreciation_ids:
                depreciation_line.post_lines_and_close_asset()
        return super(AccountMove, self).action_post()
=======
=======
>>>>>>> 7c978808bacd4a1cc1fb5707f4bd586d98d14108
    def post(self):
        for move in self:
            for depreciation_line in move.asset_depreciation_ids:
                depreciation_line.post_lines_and_close_asset()
        return super(AccountMove, self).post()
<<<<<<< HEAD
>>>>>>> 7c978808bacd4a1cc1fb5707f4bd586d98d14108
=======
>>>>>>> 7c978808bacd4a1cc1fb5707f4bd586d98d14108
