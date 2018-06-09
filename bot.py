# -*- coding: utf-8 -*-
import requests

def sendMes(text):
	requests.get('https://api.telegram.org/bot562507784:AAEqfLY0Bln35WZBmbVLCIPAth7xPytgFIU/sendMessage?chat_id=331856179&text='+text)
