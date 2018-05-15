from wtforms import fields, validators, form

class NewCitizenForm(form.Form):
	first_name = fields.StringField(u'First Name', [validators.required()])
	last_name = fields.StringField(u'Last Name', [validators.required()])
	citizenship = fields.StringField(u'Citizenship', [validators.required()])
	wallet_address = fields.StringField(u'Wallet Address', [validators.required()])
	financial_institution = fields.SelectField(u'Financial Instution', [validators.required()])
