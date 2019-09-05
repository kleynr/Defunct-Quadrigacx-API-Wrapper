import hashlib
import hmac
import requests
from time import time, sleep
#public - api get
url_ticker = 'https://api.quadrigacx.com/v2/ticker?book={}'
url_book = 'https://api.quadrigacx.com/v2/order_book?book={}'
url_transc = 'https://api.quadrigacx.com/v2/transactions?book={}'
#private - api post
url_bal = 'https://api.quadrigacx.com/v2/balance'
url_utransc = 'https://api.quadrigacx.com/v2/user_transactions'
url_open = 'https://api.quadrigacx.com/v2/open_orders'
url_lookup = 'https://api.quadrigacx.com/v2/lookup_order'
url_cancel = 'https://api.quadrigacx.com/v2/cancel_order'
url_buy = 'https://api.quadrigacx.com/v2/buy'
url_sell = 'https://api.quadrigacx.com/v2/sell'

class quadrigacx:
	def __init__(self, cx = 'ltc_cad', clientid = '2333344', apikey = 'cnrWeLpUIT', apisecret = '75e95716e7902b4853e77bae7cffd0d3'):
		self.clientid, self.apikey, self.apisecret, self.cx = str(clientid), apikey, apisecret, cx

	#Nonce and Signature
	def signature(self):
		nonce = str(int(time()*1000))
		msg = nonce+self.clientid+self.apikey
		signature = hmac.new(self.apisecret.encode(), msg=msg.encode(), digestmod=hashlib.sha256).hexdigest()
		return signature, nonce

	#public api 
	def ticker(self):
		i = 0
		while 1:
			try:
				response = requests.get(url_ticker.format(self.cx)).json()
			except ValueError:
				i += 1
				print('QCX Error {}'.format(i))
				continue
			break
		return self.handle_response(response)

	def book(self):
		i = 0
		while 1:
			try:
				response = requests.get(url_book.format(self.cx)).json()
			except ValueError:
				i += 1
				print('QCX Error {}'.format(i))
				continue
			break
		return self.handle_response(response)
		
	def transactions(self):
		i = 0
		while 1:
			try:
				response = requests.get(url_transc.format(self.cx)).json()
			except ValueError:
				i += 1
				print('QCX Error {}'.format(i))
				sleep(i*3)
				continue
			break
		return self.handle_response(response)

	#private api req. sign-in
	def balance(self):
		i = 0
		while 1:
			try:
				signature, nonce = self.signature()
				response = requests.post(url_bal, data={'key':self.apikey,'signature':signature,'nonce':nonce}).json()
			except ValueError:
				i += 1
				print('QCX Error {}'.format(i))
				sleep(i*3)
				continue
			break
		return self.handle_response(response)

	def open(self):
		i = 0
		while 1:
			try:
				signature, nonce = self.signature()
				response = requests.post(url_open, data={'key':self.apikey,'signature':signature,'nonce':nonce, 'book':self.cx}).json()
			except ValueError:
				i += 1
				print('QCX Error {}'.format(i))
				sleep(i*3)
				continue
			break
		return self.handle_response(response)

	def utransactions(self):
		i = 0
		while 1:
			try:
				signature, nonce = self.signature()
				response = requests.post(url_utransc, data={'key':self.apikey,'signature':signature,'nonce':nonce, 'book':self.cx}).json()
			except ValueError:
				i += 1
				print('QCX Error {}'.format(i))
				sleep(i*3)
				continue
			break
		return self.handle_response(response)

	def lookup(self, orderid):
		i = 0
		while 1:
			try:
				signature, nonce = self.signature()
				response = requests.post(url_lookup, data={'key':self.apikey,'signature':signature,'nonce':nonce, 'id':orderid}).json()
			except ValueError:
				i += 1
				print('QCX Error {}'.format(i))
				sleep(i*3)
				continue
			break
		return self.handle_response(response)

	#Market Actions
	def cancel(self, orderid):
		i = 0
		while 1:
			try:
				signature, nonce = self.signature()
				response = requests.post(url_cancel, data={'key':self.apikey,'signature':signature,'nonce':nonce, 'id':orderid}).json()
			except ValueError:
				i += 1
				print('QCX Error {}'.format(i))
				sleep(i*3)
				continue
			break
		return self.handle_response(response)

	def buy(self, amount, price):
		i = 0
		while 1:
			try:
				signature, nonce = self.signature()
				response = requests.post(url_buy, data={'key':self.apikey,'signature':signature,'nonce':nonce,
					'amount':amount,'price':price,'book':self.cx}).json()
			except ValueError:
				i += 1
				print('QCX Error {}'.format(i))
				sleep(i*3)
				continue
			break
		return self.handle_response(response)

	def sell(self, amount, price):
		i = 0
		while 1:
			try:
				signature, nonce = self.signature()
				response = requests.post(url_sell, data={'key':self.apikey,'signature':signature,'nonce':nonce,
					'amount':amount,'price':price,'book':self.cx}).json()
			except ValueError:
				i += 1
				print('QCX Error {}'.format(i))
				sleep(i*3)
				continue
			break
		return self.handle_response(response)

	def handle_response(self, response):
		if 'error' in response:
			response = 'Error' + str(time())
		return response

quadrigacx.py
Displaying quadrigacx.py.
