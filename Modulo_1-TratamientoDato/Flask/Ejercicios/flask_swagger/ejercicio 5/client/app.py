from flask import Flask, redirect, url_for, render_template, request, flash
import requests
import json 
app = Flask(__name__,template_folder='templates')
 
app.debug = True


@app.route('/getLastSensorMeasurement/<sensor>')
def success(sensor):
        try:
            ret=requests.get("http://localhost:8080/v2/getLastMeassureBySensor/"+sensor)
            if ret.status_code != 200:
                return response(400,f"Host not available please check ip and port localhost:8080")
        except Exception as e:
            return response(400,f"Exception {e}: Host not available please check ip and port localhost:8080")

        if ret.status_code != 200:
            return response(400,f"Server not available, or ip incorrect localhost:8080")
        else:
            return response(200,json.loads(ret.content))

def response(code,message):
    ret={}
    ret["message"]=message
    ret["error_code"]=code
    return ret



 
app.run(host='localhost', port=99)