from bs4 import BeautifulSoup
import requests
import os
import json
import base64
from Crypto.Cipher import AES
from pprint import pprint
import smtplib
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class emailhandler:
	sender = None
	receivers = None
	message = ""

	def __init__(self,s,r,m):
		self.sender = s
		self.receivers = r
		self.message = m

	def send_email(self):
		try:
			smtpObj = smtplib.SMTP()
			smtpObj.connect('smtp.163.com')
			smtpObj.login('xxxxxxx@xxx','xxxxxx')
			smtpObj.sendmail(self.sender, self.receivers, self.message)
			print "Successfully sent email"
		except:
			print "Error: unable to send email"
		finally:
			smtpObj.close()

	
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Encoding':'gzip, deflate','Content-Type':'application/x-www-form-urlencoded','Referer':'http://music.163.com/','Cookie':'appver=1.5.0.75771;'}
mylist_id = 108674314
url_myplaylist = 'http://music.163.com/api/playlist/detail?id=' + str(mylist_id)
url = 'http://m2.music.126.net/JGzMkUjAsEaL-uzK2fCJUw==/6636652186291526.mp3'
email = 'xxxxxxxxx'
pwd = 'xxxxx'

s = requests.session()
res = s.get(url_myplaylist, headers = headers)
content = res.content

res = json.loads(content)

tracks = res['result']['tracks']

for i in range(100):
	try:
		print (('%d '+tracks[i]['audition']['name']+" : "+tracks[i]['artists'][0]['name']) %(i+1))
	except:
		print ('%d song name error' %(i+1))
	try:
		print ('mp3Url: '+tracks[i]['mp3Url'])
	except:
		print 'mp3 error'

song = []
for j in range(100):
	try:
		song.append(str(j+1)+" "+tracks[j]['audition']['name']+" : "+tracks[j]['artists'][0]['name'])
	except:
		song.append(str(j+1)+" "+ 'song name error')
	try:
		song.append('mp3Url: '+tracks[j]['mp3Url'])
	except:
		song.append('mp3 error')

sender = '13188316906@163.com'
receivers = '15026630170@163.com'
message = "From: From wenbo <13188316906@163.com>\n"+"To: To myself <15026630170@163.com>\n"+"Subject: my GF\'s favorite song:\n\n"

for k in range(100):
	message = message + song[k]+ '\n'


mail = emailhandler(sender,receivers,message)
mail.send_email()



