# -*- coding: utf-8 -*-
##############################################################################
#
#  licence AGPL version 3 or later
#  see licence in __openerp__.py or http://www.gnu.org/licenses/agpl-3.0.txt
#  Copyright (C) 2014 Akretion (http://www.akretion.com).
#  @author David BEAL <david.beal@akretion.com>
#          Sébastien BEAU <sebastien.beau@akretion.com>
#
##############################################################################

from openerp.osv import orm


class ResCompany(orm.Model):
    _inherit = 'res.company'
