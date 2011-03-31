# -*- coding: utf-8 -*-
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    'name': 'Add in system tools and object',
    'name_ru_RU': 'Добавление дополнительных инструментов и объектов в систему',
    'version': '1.8.0',
    'author': 'Dmitry Klimanov',
    'email': 'k-dmitry2@narod.ru',
    'website': 'http://www.tryton.org/',
    'description': '''
''',
    'description_ru_RU': ''' 
    - Системные таблицы для словарей
    - Журнал изменения данных
''',
    'depends': [
        'ir',
        'res',
    ],
    'xml': [
        'xml/ekd_system.xml',
        'xml/ekd_journal.xml',
    ],
    'translation': [
        'ru_RU.csv',
    ]
}
