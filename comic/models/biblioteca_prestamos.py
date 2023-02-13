# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Modelo base, creado como modelo abstracto 
# Este modelo lo heredarara el modelo BibliotecaComic
# Y se ha creado puramente con fin didáctico para ver herencia entre modelos
class BaseArchive(models.AbstractModel):
    #Nombre y descripcion del modelo
    _name = 'base.archive'
    _description = 'Fichero abstracto'

    #Introduce el atributo "Activo"
    activo = fields.Boolean(default=True)
    leido = fields.Boolean()
    
    def archivar(self):
        #Por cada registro del modelo
        for record in self:
            #Cambiamos el valor de activo a su version negada
            record.activo = not record.activo


#Definimos modelo Biblioteca comic
class BibliotecaComic(models.Model):

    #Nombre y descripcion del modelo
    _name = 'prestamos'
    #Hereda de "base.archive" (el modelo abstracto creado antes)
    _inherit = ['base.archive']

    _description = 'Socio de la mazmorra'

    comic_id = fields.Many2one('biblioteca.comic', string='Comic',required=True, index=True)

    socio_id = fields.Many2one('socio', string='Socio',required=True,index = True)

    fecha_inicio = fields.Date('Fecha Inicio', required=True)

    fecha_final = fields.Date('Fecha Final')

    @api.constrains('fecha_inicio')
    def check_dateI(self):
        for record in self:
            if record.fecha_inicio < fields.Date.today():
                raise ValidationError('La fecha inicial no puede ser mayor que la fecha actual')

    @api.constrains('fecha_final')
    def check_dateF(self):
        for record in self:
            if record.fecha_final and record.fecha_final < record.fecha_inicio:
                raise ValidationError('La fecha final no puede ser menor que la fecha inicio')
