from godot import exposed, export, ClassDB, Dictionary
from godot import *

from web3 import Web3, EthereumTesterProvider
from eth_account import Account
import secrets

@exposed
class Python(Node):
	name = export(str)

	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	def _ready(self):
		self.a = 20
		self.b = "hello world"
		self.w3 = Web3(EthereumTesterProvider())
		print("INITIALIZED")

	def makeRandomAddress(self):
		priv = secrets.token_hex(32)
		private_key = "0x" + priv
		# print ("SAVE BUT DO NOT SHARE THIS:", private_key)
		acct = Account.from_key(private_key)
		obj = Dictionary({
			"public_key": acct.address,
			"private_key": private_key
		})
		return obj

	def isConnected(self):
		return self.w3.isConnected()

	def accounts(self):
		return self.w3.eth.accounts[1]
