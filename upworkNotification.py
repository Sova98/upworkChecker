from flask import Flask
from main import getPage
import time
app = Flask(__name__)

title = ''
while(True):
	title = getPage(title)
	time.sleep(60)

if __name__ == '__main__':
	app.run()

