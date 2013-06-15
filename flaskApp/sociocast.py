"""
Sociocast integration

usage: python sociocast.py
Options and arguments:
-d : debug output (also --debug)
-h : print this help message and exit (also --help)

"""

__author__ = "Mike Caprio (mik3cap@gmail.com)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/06/15 13:33:00 $"
__copyright__ = ""
__license__ = "Python"


#import errno
#import sys
#import os
#import getopt
import datetime
import hashlib

#from database.mysql_config import *
#from utilities.datetimeutil import gettime
#from utilities.log import log
from url_request import dorequest


def get_content_profile(url_string):
    api_secret = "VOfAoG4HAc7RX4qlgXTsOvzWvV4eFtvJi19OPfZh"
    api_key = "g89dv60LlS0QPERttJiI4yht"
#    client_id = ""

    server = "http://api-sandbox.sociocast.com/"
#    server = "http://api.sociocast.com/"
    version = "1.0/"
    url = server + version + "content/profile"
    request_type = "GET"

    ### Options for content/profile
    # The URL for which the content's profile should be retrieved, passed
    # as a parameter above: url_string

    # By default, each classification category is represented in the profile by
    # its ID (a String). If you send true you will instead receive the
    # human-readable names.
    humread_bool = "1"

    future = datetime.datetime.now()
    epoch_ts = future.strftime("%s")

    message = "apikey=" + api_key + "&apisecret=" + api_secret + "&ts=" + \
        epoch_ts
    SHA_sig = hashlib.sha256(message).hexdigest()

    response_dict = {}

    # Params will be encoded in the dorequest function
    params = {"url": url_string,
              "humread": humread_bool,
              "apikey": api_key,
              "ts": epoch_ts,
              "sig": SHA_sig}

    # Process the result from the search query, parse JSON
    # into a dictionary of results
    response_dict = dorequest(url, request_type, params)

    # Find the data list and paging dict in the response dictionary
    return response_dict
#     data_list = response_dict[""]

#     for each_key in data_list.keys():
#         url_response = data_list[each_key]["url"]
#         classification_reponse = data_list[each_key]["classification"]

    # Insert into a DB?
