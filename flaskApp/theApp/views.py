from flask import render_template, flash, redirect, session, make_response
from theApp import app #, db -- no database yet, we can uncomment this, and the db setup in __init__.py when we need to add one

import json
from tools import valueFromRequest
import os
import calendar
from flask import request
import datetime
from bitlyCalls import *
from sociocast import get_content_profile
from rovi import get_rovi_data


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/get_phrases')
def get_phrases():

    results = getBurstingPhrases()

    socio_results_list = []
    song_results_list = []

    for each_item in results:
        for each_key in each_item.keys():
            if (each_key == "phrase"):
                phrase = each_item["phrase"]

                # Pass Sociocast results and Bit.ly phrase into Rovi to get
                # song results
                song_results_list.append(get_rovi_data("musicsearch", phrase))
            elif (each_key == "top_link"):
                # Pass top URL into sociocast to get classifications
                sociocast_url = each_item["top_link"]["aggregate_url"]

                socio_results_list.append(get_content_profile(sociocast_url))

                # Could combine titles into unique tokens and remove
                # stop words for additional search keywords
#            elif (each_key == "titles"):
#                url_response = each_item["titles"]

    response = make_response(json.dumps(song_results_list))
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/get_hot_phrases')
def get_hot_phrases():
    results = getHotPhrases()

    response = make_response(json.dumps(results))
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response
