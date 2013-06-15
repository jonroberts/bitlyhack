from flask import render_template, flash, redirect, session, make_response
from theApp import app, db

import json
from tools import valueFromRequest
import os
import calendar
from flask import request
import datetime


import random

@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")

@app.route('/api_call')
def get_estimate():
	"""This is an API call"""
	""""
	today = datetime.date.today()

	this_month=today.month
	this_year=today.year
	day=1
	
	ip_address=request.remote_addr
	zipcode = int(valueFromRequest(key="zip_in", request=request))
	num_in_house = int(valueFromRequest(key="num_in_house", request=request))

	recording=False
	try:
		record_data=int(valueFromRequest(key="record_data", request=request))
	except:
		pass
	if record_data>0:
		recording=True
	
	months=the_months()
	monthly_data={}

	for month in months:
		try:
			d=float(valueFromRequest(key=month, request=request))
			monthly_data[month]=d
		except:
			continue

	
	# store the data
	if recording:
		user = User.query.filter_by(ip = ip_address).first()
		# add the user if they don't exist
		if user is None:
			
			user = User(name = "", email = "", ip = ip_address, zip=zipcode, state="NY", num_in_house=num_in_house)
			db.session.add(user)
			db.session.commit()
	
		# run through the last 12 months. If there's a data entry, then check for a bill object. If one doesn't exist, add it.
		for i in range(1,13):
			t_year=this_year
			t_month=this_month-i
			if t_month<=0:
				t_month+=12
				t_year-=1
			
			month_str=months[t_month-1]
			if month_str not in monthly_data.keys():
				continue
				
			date=datetime.date(day=day, month=t_month, year=t_year)
			bill = Bill.query.filter_by(month = date).filter_by(user_id = user.id).first()
	
			if bill is None:
				bill=Bill(month=date,user_id=user.id,kwh=monthly_data[month_str])
				db.session.add(bill)
			else:
				bill.kwh=monthly_data[month_str]
			db.session.commit()



	ratio, average_ratio, normalized_ratio, metric, annual_usage = analyze_user(monthly_data, usage_by_unit, US_norm)
	pred_use, pred_uncert = predict_all_months(monthly_data, US_norm)
	"""
	response=make_response(json.dumps({"error":"doesn't do anything yet"}))
	response.headers.add("Access-Control-Allow-Origin","*")
	return response

