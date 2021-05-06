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
    # Code that executes the fortune command goes here.
    # Capture its output and return the output surrounded by the# strings "<pre>" and "</pre>".

@app.route('/cowsay/<message>/')
def cowsay(message):
    stream = os.popen('cowsay ' + str(message))
    output =  "<pre>" + stream.read() + "</pre>"
    return output
    # Code goes here.

@app.route('/cmd/<command>/')
def cmd(command):
    stream = os.popen(str(command))
    output = "<pre>" + stream.read() + "</pre>"
    return output
