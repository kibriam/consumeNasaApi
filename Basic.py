import json
import urllib.request
import requests

# test commit for github

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1> Hello World!</h1>"

##get rest call to nasa api and get the response in json



url = 'https://api.nasa.gov/planetary/apod?api_key='
params = 'NtJaIQi5cb2AvkEmJaBBq0YffTkcywVdtGzFFNVX'
@app.route('/apod')
def getApodHomePage():

    response = requests.get(url + params)

    return response.content

@app.route('/picture')
def getPicture():

    req = urllib.request.urlopen(url+params)
    req = req.read()
    req_obj = json.loads(req.decode('utf-8'))
    today_picture = req_obj['url']
    print(today_picture)
    return render_template('index.html', pic = today_picture)


if __name__ == '__main__':
    app.run(debug=True)
