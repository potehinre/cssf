import forms
import requests
import utils
import config

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/new_citizen/', methods=["GET", "POST"])
def new_citizen():
	resp = requests.get(config.ENDPOINT + "ecosystemslist")
	form = forms.NewCitizenForm(request.form)
	form.financial_institution.choices = config.ECOSYSTEM_CHOICES
	if request.method == 'POST' and form.validate():
		data = {}
		data["ecosystem_id"] = int(request.form["financial_institution"])
		data["wallet_address"] = request.form["wallet_address"]
		data["firstname"] = request.form["first_name"]
		data["lastname"] = request.form["last_name"]
		data["citizenship"] = request.form["citizenship"]
		data["residence_address"] = request.form["residence_address"]
		utils.call_contract(config.ENDPOINT, config.PRKEY, "WaletRequest", data)
		form = forms.NewCitizenForm()
		form.financial_institution.choices = config.ECOSYSTEM_CHOICES
	return render_template('new_citizen.html', form=form)
	
@app.route('/static/style.css', methods=["GET"])
def root():
    return app.send_static_file('style.css')
	
app.run(debug = True)
