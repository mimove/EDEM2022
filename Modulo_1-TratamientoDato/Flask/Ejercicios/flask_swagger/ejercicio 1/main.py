from flask import Flask, redirect, url_for, render_template, request, flash
 
app = Flask(__name__,template_folder='templates')
 
app.debug = True


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return f'welcome to a POST of {user}'
   else:
      return 'welcome to a GET'


@app.route('/users/<user_id>', methods = ['GET', 'POST', 'DELETE'])
def user(user_id):
    if request.method == 'GET':
        return 'You are running GET method for '+ user_id + ' user'
    if request.method == 'POST':
        return 'You are running POST method for '+ user_id + ' user ' 
    if request.method == 'DELETE':
        return 'You are running DELETE method for '+ user_id + ' user '


@app.put('/users/<user_id>')
def putUser(user_id):
    return 'You are running PUT method for ' + user_id + ' user'



def shutdown_server():
    func = request.environ.get('localhost:5000')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    

@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
 
app.run(host='localhost', port=5000)