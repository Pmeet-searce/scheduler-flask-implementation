from flask import Flask,render_template,request
from flask import make_response,jsonify,redirect,url_for
import json
import scheduler as sc
import datetime

app=Flask(__name__)


    
@app.route('/')
def index():
    return render_template("index.htm")

@app.route('/posting',methods=["POST"])
def hello():
    user=request.form['user']
    profile=request.form['profile']
    startdate=request.form['startdate']
    enddate=request.form['enddate']
    user_date=[user,profile,startdate,enddate]
    sc.insert(user_date)
    return redirect('/display')

@app.route('/reset')
def reset():
    users={}
    u="u1"
    p="p1"
    day,month,year=map(int,"01-01-2020".split("-"))
    sDate=str(datetime.date(year,month,day))
    day,month,year=map(int,"10-01-2020".split("-"))
    eDate=str(datetime.date(year,month,day))
    users[u]=[{"profile":p,"startDate":sDate,"endDate":eDate}]
    f_write=open("users.json","w")
    json.dump(users,f_write)
    f_write.close()    
    f_read=open("users.json","r")
    userdata = json.load(f_read)
    f_read.close()
    
    return render_template("display.htm",data=userdata)
    

@app.route('/display',methods=["GET"])
def display():
    f_read=open("users.json","r")
    userdata = json.load(f_read)
    f_read.close()
    return render_template("display.htm",data=userdata)
    

if __name__ == "__main__":
    app.run(debug=True)