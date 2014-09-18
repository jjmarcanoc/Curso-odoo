# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class suscriptor(osv.osv):
    _name = 'co.suscriptor'
    _description = 'CO Suscriptor'
<<<<<<< HEAD
    
    _columns = {
        'name': fields.char('Nombre y Apellido'),
        'identification': fields.char('Cédula'),
        'address': fields.text('Dirección'),
    }
    
    _sql_constraints = [('identification_uniq', 'unique(identification)', u'Ya existe el número de cédula')]
    
suscriptor()
=======

    _columns = {
        'name': fields.char('Nombre'),
        'identification': fields.char('Cédula'),
        'address': fields.text('Dirección'),
        }

suscriptor()
>>>>>>> 49e77823fa409c00b7c13482df75d9f23f5fed1c
