from flask import Flask, request, redirect
import twilio.twiml
import os
import sys
import sqlite3
from twilio.rest import TwilioRestClient

app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def fetch():
	body = request.values.get('Body', None)
	db = sqlite3.connect('amazon.db')
	if body.isdigit():
		c = db.cursor()
	
		c.execute("select link from products where pid = " + body)
		lnk = c.fetchone()
		msg = lnk[0]
	else:
		c = db.cursor()
		c.execute("select link from products where title like '%" + body + "%'")
		links = c.fetchall()
		c.execute("select title, pid from products where title like '%" + body + "%'")
		title = c.fetchall()

		msg = ""
		if not links:
			msg = "Nothing Found"
		else:
			for i in title:
				c = db.cursor()
				msg+=str(str(i[1]) + '. ' + str(i[0]) + ' ')
				db.commit()
	resp = twilio.twiml.Response()
	resp.message(msg)
	return str(resp)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)