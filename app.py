import forms
import requests
import utils
import config

from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/new_citizen/', methods=["GET", "POST"])
def new_citizen():
	resp = requests.get(config.ENDPOINT + "ecosystemslist")
	ecosystems_list = resp.json()['list']
	form = forms.NewCitizenForm(request.form)
	form.financial_institution.choices = [(el["id"], el["name"]) for el in ecosystems_list if el["id"] != u"1"]
	if request.method == 'POST' and form.validate():
		data = {}
		data["ecosystem_id"] = int(request.form["financial_institution"])
		data["wallet_address"] = request.form["wallet_address"]
		data["firstname"] = request.form["first_name"]
		data["lastname"] = request.form["last_name"]
		data["citizenship"] = request.form["citizenship"]
		utils.call_contract(config.ENDPOINT, config.PRKEY, "WaletRequest", data)
	return render_template('new_citizen.html', form=form)
