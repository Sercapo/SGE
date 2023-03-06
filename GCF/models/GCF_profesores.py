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
    
    #Introducice metodo "archivar" que invierte el estado de "activo"
    #Recordamos se recive "self" como el modelo entero y no como un registro,
    #por ese motivo debemos iterar
    def archivar(self):
        #Por cada registro del modelo
        for record in self:
            #Cambiamos el valor de activo a su version negada
            record.activo = not record.activo
            
#Definimos modelo Biblioteca comic
class GCF(models.Model):

    #Nombre y descripcion del modelo
    _name = 'profesores'
    #Hereda de "base.archive" (el modelo abstracto creado antes)
    _inherit = ['base.archive']

    profesor_id = fields.Integer(string='Id del Porfesor', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    modulo_id = fields.Many2many('modulos', string='Modulo', required=True,index = True)
    centro_id = fields.Many2one('centros', string='Centro', required=True,index=True)