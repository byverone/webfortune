from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = b'REPLACE_ME_x#pi*CO0@^z'

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/')
def fortune():
    stream = os.popen('fortune')
    output = "<pre>" + stream.read() + "</pre>"
    return output

@app.route('/cowsay/<message>/')
def cowsay(message):
    stream = os.popen('cowsay ' + str(message))
    output =  "<pre>" + stream.read() + "</pre>"
    return output

@app.route('/cowfortune/')
def cowfortune():
    stream = os.popen('fortune | cowsay')
    output = "<pre>" + stream.read() + "</pre>"
    return output

@app.route('/cmd/<command>/')
def cmd(command):
    stream = os.popen(str(command))
    output = "<pre>" + stream.read() + "</pre>"
    return output
