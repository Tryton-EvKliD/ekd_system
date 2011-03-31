# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
"Company"
from trytond.model import ModelView, ModelSQL, fields

class SystemDiction(ModelSQL, ModelView):
    'System Diction'
    _name = 'ir.dictions'
    _description = __doc__

    key = fields.Char('Key', size=128, required=True)
    value = fields.Char('Value', size=None, required=True, translate=True)
    active = fields.Boolean('Active', required=True)
    shortname = fields.Char('Shortname', size=64)
    sequence = fields.Char('Sequence', size=10)
    model = fields.Char('Model Name', size=128, required=True)
    pole = fields.Char('Pole', size=128, required=True)
    domain = fields.Char('Domain', size=None)

    def __init__(self):
        super(SystemDiction, self).__init__()
        self._order.insert(0, ('model', 'DESC'))
        self._order.insert(1, ('pole', 'DESC'))

    def default_active(self):
        return True

SystemDiction()
