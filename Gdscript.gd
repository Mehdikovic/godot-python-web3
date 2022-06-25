extends Node

onready var web3 = get_node("./Python")

func _ready():
	print("in gdscript")
	print(web3.isConnected())
	# print(web3.accounts())
	$CanvasLayer/PublicKey.text = ""
	$CanvasLayer/PrivateKey.text = ""



func _on_Button_button_down():
	var res = web3.makeRandomAddress()
	$CanvasLayer/PublicKey.text = res.public_key
	$CanvasLayer/PrivateKey.text = res.private_key
