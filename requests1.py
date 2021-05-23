import requests
#jc_data={‘key1’: ‘value1’, ‘key2’: ‘value2’}
q=requests.get('http://127.0.0.1:8000/bhr/5246')
data_in=q.json()
r=requests.post('http://127.0.0.1:8000/jumpcloud/create', json=data_in)
print(q.text)
print(r.text)
print (r.url)
#print(“The data in is”,data_in,“Tada”)
print(r.json())