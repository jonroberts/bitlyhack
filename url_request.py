"""
URL request class

Handles HTTP requests for RESTful APIs
"""

__author__ = "Mike Caprio (mik3cap@gmail.com)"
__version__ = "$Revision: 0.2 $"
__date__ = "$Date: 2012/06/15 12:18:25 $"
__copyright__ = ""
__license__ = "Python"

#import errno
#import sys
#import string
import httplib2
import urllib
import time
#import urlparse

try:
    import json
except ImportError:
    import simplejson as json


def dorequest(url, method, params):
    for key in params:
        # Remove keys with no value
        if (key is None):
            del params[key]

    encodedparams = urllib.urlencode(params)

    conn = httplib2.Http()

    headers_dict = {}
    headers_dict["User-Agent"] = "USER AGENT HERE"
    headers_dict["Content-type"] = "application/x-www-form-urlencoded"
    headers_dict["Accept"] = "text/plain"

    request_source = "User-Agent:" + headers_dict["User-Agent"]

    if (method == "GET"):
        request_sent = method + " " + url + "?" + encodedparams + \
            " HTTP/1.1\n" + request_source + "\nContent-type: " + \
            headers_dict["Content-type"] + "\nAccept: " + \
            headers_dict["Accept"] + "\n"
    elif (method == "POST"):
        request_sent = method + " " + url + " HTTP/1.1\n" + \
            request_source + "\nContent-type: " + \
            headers_dict["Content-type"] + "\nAccept: " + \
            headers_dict["Accept"] + "\n\n" + encodedparams

    print request_sent

    # Keep trying until we get a successful response
    while True:
        if (method == "GET"):
            response = conn.request(url + "?" + encodedparams,
                                    method,
                                    headers=headers_dict)
        elif (method == "POST"):
            response = conn.request(url,
                                    method,
                                    encodedparams,
                                    headers_dict)

        if (response is not None):
            # Decode the JSON, load the string which can be evaluated
            response_dict = json.loads(response[1])

            # Check for error, wait two minutes and try again
            if ("error" in response_dict):
                time.sleep(120)
            else:
                break

    return response_dict
