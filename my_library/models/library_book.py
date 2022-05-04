# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'library.book'
    
    name = fields.Char(string="Titolo", tracking=True, store=True, help="Titolo")
    date_release = fields.Date(string="Data di uscita", tracking=True, store=True, help="Data di uscita")
    author_ids = fields.Many2many('res.partner', string="Authors")