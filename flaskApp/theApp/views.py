from flask import render_template, flash, redirect, session, make_response
from theApp import app, db

import json
from tools import valueFromRequest
import os
import calendar
from flask import request
import datetime
from bitlyCalls import *

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/get_phrases')
def get_phrases():
	results=getBurstingPhrases()

	response=make_response(json.dumps(results))
	response.headers.add("Access-Control-Allow-Origin","*")
	return response

@app.route('/get_hot_phrases')
def get_phrases():
	results=getHotPhrases()

	response=make_response(json.dumps(results))
	response.headers.add("Access-Control-Allow-Origin","*")
	return response
