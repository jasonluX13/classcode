from flask import Flask,request,url_for,redirect,render_template
import time
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/getstuff")
def getstuff():
    print "In getstuff"
    time.sleep(5)
    print "returning stuff"
    return "stuff"

@app.route("/getslow")
def getslow():
    print "in getslow"
    time.sleep(10)
    print "returning from slow"
    return "slowstuff"

@app.route("/getfast")
def getfast():
    print "in getfast"
    print "returning from fast"
    return "faststuff"

if __name__=="__main__":
   app.debug=True
   app.run(host="0.0.0.0",port=8000)
