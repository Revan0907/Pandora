from flask import render_template, session, request, redirect, url_for
from website import app
import time
from website.chatbotgen import cbinteraction 
from flask_gtts import gtts
from gtts import gTTS
import os, sys


@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route("/about", methods=['GET','POST'])
def about():
    return render_template('about.html')

@app.route("/chatpage", methods=['GET','POST'])
def chatpage():
    if ("users-msg" not in session) or ("bot-msg" not in session):
        session["users-msg"] = []
        session["bot-msg"] = []
        session["audio"] = []
    if request.method == 'POST':
        user_in = request.form.get('user_in')
        return redirect(url_for('chatpageint',user_in = user_in))
    return render_template('chatpage.html')
    
@app.route("/chatpageint", methods=['GET','POST'])
def chatpageint():
    if request.method == 'POST':
        user_int = request.form.get('user_int')
        res = cbinteraction(user_int)
        u_msg = res[0]
        c_msg = res[1]
        session["users-msg"].append(u_msg)
        session["bot-msg"].append(c_msg)
        tts = gTTS(text = c_msg, slow = False, lang = 'en')
        savef = "website/static/audio"+str(len(session["bot-msg"])-1)+".mp3"     
        tts.save(savef)
        audiof = ("/static/audio")
        audiof = audiof+str(len(session["bot-msg"])-1)+".mp3"
        return render_template('chatpageint.html',u_msg=u_msg,c_msg=c_msg,audiof=audiof)
    else: 
        user_in = request.args.get('user_in')
        res = cbinteraction(user_in)
        u_msg = res[0]
        c_msg = res[1]
        session["users-msg"].append(u_msg)
        session["bot-msg"].append(c_msg)
        tts = gTTS(text = c_msg, slow = False, lang = 'en')  
        savef = "website/static/audio"+str(len(session["bot-msg"])-1)+".mp3"     
        tts.save(savef)
        audiof = ("/static/audio")
        audiof = audiof+str(len(session["bot-msg"])-1)+".mp3"
        return render_template('chatpageint.html',u_msg=u_msg,c_msg=c_msg,audiof=audiof)