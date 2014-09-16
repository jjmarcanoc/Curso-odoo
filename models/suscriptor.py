# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class suscriptor(osv.osv):
    _name = 'co.suscriptor'
    _description = 'CO Suscriptor'

    _columns = {
        'name': fields.char('Nombre'),
        'identification': fields.char('Cédula'),
        'Adress': fields.text('Dirección'),
        }

suscriptor()