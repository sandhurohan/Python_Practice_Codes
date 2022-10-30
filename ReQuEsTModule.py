import requests
r=requests.get("https://www.youtube.com/watch?v=u6_aYV-1LAE")
print(r.text)
print(r.status_code)