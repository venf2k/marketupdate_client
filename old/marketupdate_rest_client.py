###################################
#
#  
#
###################################

import requests

Host = 'http://127.0.0.1:8000/'

urls_update = 'api/updates/'
update_date = '2018-08-12'
update_time = '13:00:00'
#update_hook = update_time + '@' + update_time
payload_update = {'notes_text': 'rilevazione di prova da client', 'pub_date': update_date, 'pub_hour': update_time}
r = requests.post(Host + urls_update, data = payload_update)
print('URL request' + r.url)
print('Request status code: ' + str(r.status_code))
print('Request status code: ' + str(r.status_code))
print('Response header:' +  str(r.headers))
update_content = r.json()
update_pk = update_content['pk']
print('Content response:' +  str(update_content))
print('Content pk value:' + str(update_pk))

urls_category = 'api/categories/'
payload_category = {'name': 'Titoli gevernativi', 'description': 'Tassi e Spread principali titoli benchmark', 'update': update_pk}
r = requests.post(Host + urls_category, data = payload_category)
print('URL request' + r.url)
print('Request status code: ' + str(r.status_code))

#payload_category = {'name': 'Tassi', 'description': 'Principali punti della curva EUR IRS', 'update': update_hook}
#r = requests.post(Host + urls_category, data = payload_category)
#print('URL request' + r.url)
#print('Request status code: ' + str(r.status_code))


#urls_symbol = 'api/symbol/'
#payload_symbol = {'notes_text': 'rilevazione di prova da client', 'pub_date': '2018-08-03', 'pub_hour': '08:00:00'}
#r = requests.post(Host + urls_symbol, data = payload_symbol)
#print('URL request' + r.url)
#print('Request status code: ' + str(r.status_code))

#urls_value = 'api/value/'
#payload_value = {'notes_text': 'rilevazione di prova da client', 'pub_date': '2018-08-03', 'pub_hour': '08:00:00'}
#r = requests.post(Host + urls_value, data = payload_value)
#print('URL request' + r.url)
#print('Request status code: ' + str(r.status_code))