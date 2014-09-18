# -*- coding: utf-8 -*-

from openerp.osv import osv, fields


class tienda(osv.osv):
    _name = 'co.tienda'
    _description = 'CO Tienda'
<<<<<<< HEAD
    
=======

>>>>>>> 49e77823fa409c00b7c13482df75d9f23f5fed1c
    _columns = {
        'name': fields.char('Tienda'),
        'address': fields.char('Dirección'),
    }

<<<<<<< HEAD
tienda()
=======
tienda()
>>>>>>> 49e77823fa409c00b7c13482df75d9f23f5fed1c
