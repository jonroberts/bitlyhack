"""
Rovi integration

usage: python rovi.py
Options and arguments:
-d : debug output (also --debug)
-h : print this help message and exit (also --help)

"""

__author__ = "Mike Caprio (mik3cap@gmail.com)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/06/15 15:17:00 $"
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


def get_rovi_data(command, query_string=None):
    shared_secret = "QYDb7gXPXp"
    api_key = "tyh5tujv82t7jyf25y849p6n"

    server = "http://api.rovicorp.com/"
    version = "v2.1/"
    request_type = "GET"

    output_country = "US"
    output_lang = "en"
    output_format = "json"

    future = datetime.datetime.now()
    epoch_ts = future.strftime("%s")

    message = api_key + shared_secret + epoch_ts
    md5_sig = hashlib.md5(message).hexdigest()

    if (command == "musicmoods"):
    ### No options for descriptor/musicmoods
        endpoint_type = "data/"
        url = server + version + "descriptor/musicmoods"

        # Params will be encoded in the dorequest function
        params = {"country": output_country,
                  "language": output_lang,
                  "format": output_format,
                  "apikey": api_key,
                  "sig": md5_sig}
    elif (command == "musicsearch"):
    ### Options for song search
    # The URL for which the content's profile should be retrieved.
        endpoint_type = "search/"
        url = server + endpoint_type + version + "music/search"

        # Params will be encoded in the dorequest function
        params = {"entitytype": "song",
                  "query": query_string,
                  "rep": "1",
                  "size": "20",
                  "offset": "0",
                  "country": output_country,
                  "language": output_lang,
                  "format": output_format,
                  "apikey": api_key,
                  "sig": md5_sig}

    response_dict = {}

    # Process the result from the search query, parse JSON
    # into a dictionary of results
    response_dict = dorequest(url, request_type, params)

    # Find the data list and paging dict in the response dictionary
    return response_dict
