from flask import request
def shutdown_server():
    func = request.environ.get('localhost:5000')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    

@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'