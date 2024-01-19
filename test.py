from flask import Flask, make_response, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
	data = [request.remote_addr, request.server, request.user_agent]
	s = ''
	
	for x in data:
		s+=str(x)+'<br>'
	
	return s+requests.get('https://icanhazip.com/').text



if __name__ == "__main__":
	app.run(host='0.0.0.0')