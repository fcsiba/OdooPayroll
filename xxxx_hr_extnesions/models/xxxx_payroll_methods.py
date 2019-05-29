# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PayrollCustomizations(models.Model):
	_inherit = 'hr.payslip'

	@api.multi
	def salaryfunction(self,empid,finetype,date_from,date_to):
		# fine=0
		# if(finetype=="NIC"):
		# 	fine=1
		# if(finetype=="HUSF"):
		# 	fine=2
		# if(finetype=="LOC"):
		# 	fine=4
		# if(finetype=="GUAR"):
		# 	fine=3
		fines = self.env['x.fine'].search([('name','=',"finetype")])
		penalty = self.env['x_penalties'].search(['&', '&', ('pemployee','=',empid), ('pfinetype','=',fines.id), '|', ('pdateto','=',None), '|', '&' ,('pdateto','>=',date_from),('pdateto','<=',date_to), '&',('pdatefrom','>=',date_from),('pdatefrom','<=',date_to)])
		#penalty = self.env['x_penalties'].search(['&', '&', ('pemployee','=',empid),('pfinetype','=',fine), '|', '&' ,('pdateto','>=',date_from),('pdateto','<=',date_to), '&',('pdatefrom','>=',date_from),('pdatefrom','<=',date_to)])
		fine_amt=0
		for i in penalty:
			fine_amt= fine_amt+i.pfineamount
		return  fine_amt