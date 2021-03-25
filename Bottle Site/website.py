from bottle import run, route, view, static_file, request
from datetime import date
import requests

@route('/')
@view('index')
def index():
    today = date.today()
    
    return dict(
      day = today.strftime('%A')
  )

@route('/age-form')
@view('age-form')
def age_form():
    pass


@route('/age-result', method='POST')
@view('age-result')
def age_result():
  first_name = request.forms.get('name')
  api_result = requests.get('https://api.agify.io/?name=' + first_name)
  agify_data = api_result.json()

  return dict(
    name = first_name,
    age = agify_data['age']
  )

@route('/static/<filepath:path>')
def load_static(filepath):
    return static_file(filepath, root='./static')


#start a website
run(host='0.0.0.0',port=8080, reloader=True, debug=True)