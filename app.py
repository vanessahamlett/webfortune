import subprocess
from flask import (
    abort, Flask, jsonify, redirect, render_template, request,
    session, url_for
)

app = Flask(__name__)

@app.route('/')
def index():
    return fortune()

@app.route('/cowsay/<message>/')
def cowsay(message):
    output = subprocess.Popen(f'cowsay {message}', shell=True, stdout=subprocess.PIPE, universal_newlines=True).stdout.read()
    return '<pre>' + str(output) + '</pre>'

@app.route('/fortune/')
def fortune():
    message = subprocess.run('fortune', shell=True, stdout=subprocess.PIPE, universal_newlines=True).stdout
    return '<pre>' + str(message) + '</pre>'

@app.route('/cowfortune/')
def cowfortune():
    message = subprocess.run('fortune', shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    output = subprocess.run(f'cowsay {message.stdout}', shell=True, stdout=subprocess.PIPE, universal_newlines=True).stdout
    return '<pre>' + str(output) + '</pre>'
