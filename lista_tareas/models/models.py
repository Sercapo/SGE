# -*- coding: utf-8 -*-

from odoo import models, fields, api

class lista_tareas(models.Model):
     _name = 'lista_tareas.lista_tareas'
     _description = 'lista_tareas.lista_tareas'

     tarea = fields.Char()
     prioridad = fields.Integer()
     Urgente = fields.Boolean(compute="_value_urgente", store=True)
     Realizada = fields.Boolean()

     @api.depends('prioridad')
     def _value_urgente(self):
         for record in self:
             if record.prioridad <10:
                 record.Urgente = True
             else:
               record.Urgente = False
