import requests
import hashlib

ses = requests.session()

resp = ses.get("http://178.62.54.33:32228/");
text = resp.text[167:187]
m = hashlib.md5()
m.update(text.encode('utf-8'))

data = {"hash":m.hexdigest()}
send_back = ses.post("http://178.62.54.33:32228/",data=data)
text = resp.text[167:187]

print(send_back.text)
print("")
print("flag:"+send_back.text[210:234])
