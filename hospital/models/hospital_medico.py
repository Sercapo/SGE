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
class Hospital(models.Model):

    #Nombre y descripcion del modelo
    _name = 'hospital.medico'
    
    #Hereda de "base.archive" (el modelo abstracto creado antes)
    _inherit = ['base.archive']

    _description = 'Medicos del Loquero'

    _rec_name = 'nombre'

    nombre = fields.Char('Nombre',required=True)

    apellido = fields.Char('Apellido',required=True)

    medico_id = fields.Char('Id',required=False)