import requests

def get_uid(url):
	resp = requests.get(url + '/getuid')
	result = resp.json()
	return result['token'], result['uid']

def sign(forsign, url, prKey):
	data = {'forsign': forsign, 'private': prKey}
	resp = requests.post(url + "/signtest/", params=data)
	result = resp.json()
	return result['signature'], result['pubkey']

def login(url, prKey):
	token, uid = get_uid(url)
	signature, pubkey = sign("LOGIN" + uid, url, prKey)
	fullToken = 'Bearer ' + token
	data = {'pubkey': pubkey, 'signature': signature}
	head = {'Authorization': fullToken}
	resp = requests.post(url + '/login', params=data, headers=head)
	res = resp.json()
	result = {}
	result["uid"] = uid
	result["timeToken"] = res["refresh"]
	result["jwtToken"] = 'Bearer ' + res["token"]
	result["pubkey"] = pubkey
	result["address"] = res["address"]
	result["key_id"] = res["key_id"]
	return result

def prepare_tx(url, prKey, entity, jvtToken, data):
	urlToCont = url + '/prepare/' + entity
	heads = {'Authorization': jvtToken}
	resp = requests.post(urlToCont, data=data, headers=heads)
	result = resp.json()
	forsign = result['forsign']
	signature, _ = sign(forsign, url, prKey)
	return {"time": result['time'], "signature": signature, "reqID": result['request_id']}

def call_contract(url, prKey, name, data):
	result = login(url, prKey)
	sign = prepare_tx(url, prKey, name, result["jwtToken"], data)
	dataContract = {"time": sign['time'], "signature": sign["signature"]}
	urlEnd = url + '/contract/' + sign["reqID"]
	resp = requests.post(urlEnd, data=dataContract, headers={"Authorization": jvtToken})
	result = resp.json()
	return result
