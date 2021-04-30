import requests

# r = requests.get("https://httpbin.org/get")
# r2 = requests.post("https://httpbin.org/post", data={'key': 'value'})
# r3 = requests.patch("https://httpbin.org/patch", data={'key1': 'value1'})
# r4 = requests.put("https://httpbin.org/put", data={'key2': 'value2'})
# r5 = requests.delete("https://httpbin.org/delete")
# r6 = requests.head("https://httpbin.org/get")
# r7 = requests.options("https://httpbin.org/get")
r = requests.options("https://httpbin.org/get", params={'k1': 'v1', 'k2': 'v2'})
r = requests.options("https://httpbin.org/get", params={'k1': 'v1', 'k2': ['v2', 'v3']})
print(r.text)
print(r.url)
