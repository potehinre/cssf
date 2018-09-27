from wtforms import fields, validators, form

class NewCitizenForm(form.Form):
	first_name = fields.StringField(u'First Name', [validators.required()])
	last_name = fields.StringField(u'Last Name', [validators.required()])
	citizenship = fields.StringField(u'Citizenship', [validators.required()])
	residence_address = fields.StringField(u'Residence Address', [validators.required()])
	wallet_address = fields.StringField(u'Wallet Address', [validators.required()])
	financial_institution = fields.SelectField(u'Select Financial Instution', [validators.required()])
	
