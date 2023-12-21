import requests

url = "http://forex.cbm.gov.mm/api/latest"
res = requests.get(url).json()

rate = res.get('rates', {})

print("current USD/MMK rate from Central Bank is", rate.get('USD'))
