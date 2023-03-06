from app import app, cache
from config import Config
from flask import request
import json
import urllib.request

# Home/Index page
@app.route('/')
def index():
	return 'hello'

@app.route('/api/latest/<int:quantity>', methods=['GET'])
@cache.cached()
def latest(quantity=10):
	category = 'general'
	url = f'{Config.GNEWS_URL}/top-headlines?category={category}&lang=en&country=us&max={quantity}&apikey={Config.API_KEY}'
	return init_request(url)

@app.route('/api/search/<string:keyword>', methods=['GET'])
@app.route('/api/search/<string:keyword>/<int:quantity>', methods=['GET'])
@cache.cached()
def search_general(keyword,quantity=10):
	url = f"{Config.GNEWS_URL}/search?q={keyword}&lang=en&country=us&max={quantity}&apikey={Config.API_KEY}"
	return init_request(url)

@app.route('/api/search/title/<string:title>', methods=['GET'])
@app.route('/api/search/title/<string:title>/<int:quantity>', methods=['GET'])
@cache.cached()
def search_title(title,quantity=10):
	url = f"{Config.GNEWS_URL}/search?q={title}&lang=en&country=us&in=title&max={quantity}&apikey={Config.API_KEY}"
	return init_request(url)

@app.route('/api/search/desc/<string:desc>', methods=['GET'])
@app.route('/api/search/desc/<string:desc>/<int:quantity>', methods=['GET'])
@cache.cached()
def search_desc(desc,quantity=10):
	url = f"{Config.GNEWS_URL}/search?q={desc}&lang=en&country=us&in=description&max={quantity}&apikey={Config.API_KEY}"
	return init_request(url)

@app.route('/api/search/content/<string:content>', methods=['GET'])
@app.route('/api/search/content/<string:content>/<int:quantity>', methods=['GET'])
@cache.cached()
def search_content(content,quantity=10):
	url = f"{Config.GNEWS_URL}/search?q={content}&lang=en&country=us&in=content&max={quantity}&apikey={Config.API_KEY}"
	return init_request(url)

def init_request(url):
	with urllib.request.urlopen(url) as url:
		source_data = url.read()
		source_resp = json.loads(source_data)
		return [source_resp]

	return ['Nothing found.']