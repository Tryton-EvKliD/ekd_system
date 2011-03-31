# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
"Journal Change Data"
from trytond.model import ModelView, ModelSQL, fields
import datetime

class SystemJournal(ModelSQL, ModelView):
    'System Journal'
    _name = 'ir.journal'
    _description = __doc__

    user = fields.Many2One('res.user', 'User', required=True)
    date_operation = fields.DateTime('Date and Time', required=True)
    model_ref = fields.Reference(selection='get_model_ref', string='Model Ref', required=True)
    action = fields.Selection([
                            ('create', 'Create'),
                            ('write','Write'),
                            ('delete','Delete')
                            ], 'Action', required=True)
    message = fields.Text('Message')
    change_data = fields.Text('New data')
    old_data = fields.Text('Old data')

    def __init__(self):
        super(SystemJournal, self).__init__()
        self._order.insert(0, ('user', 'ASC'))
        self._order.insert(0, ('date_operation', 'ASC'))
        self._order.insert(0, ('model_ref', 'ASC'))
        self._order.insert(0, ('action', 'ASC'))

#        self._rpc.update({
#                    'loadData': True,
#                            })
    def default_active(self):
        return True

    def default_date_operation(self):
        return datetime.datetime.now()

    def get_model_ref(self):
        models_obj = self.pool.get('ir.model')
        res = []
        model_ids = models_obj.search( [])
        for model in models_obj.browse(model_ids):
            res.append([model.model, model.name])
        return res

SystemJournal()
