from flask import Flask, make_response, request


app = Flask(__name__)


@app.route('/')
def index():
	data = [request.remote_addr, request.server, request.user_agent]
	s = ''
	
	for x in data:
		s+=x+'<br>'


	return s


