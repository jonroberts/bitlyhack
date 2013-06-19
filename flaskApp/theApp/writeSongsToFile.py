#!/Library/Frameworks/EPD64.framework/Versions/7.1/bin/python

import json

import requests
from bitlyCalls import *
from sociocast import get_content_profile
from rovi import get_rovi_data

def getCurrentSongsAndWriteToFile():
    results = getBurstingPhrases()

    #socio_results_list = []
    #song_results_list = []
    for each_item in results:
        for each_key in each_item.keys():
            if (each_key == "phrase"):
                phrase = each_item["phrase"]

                # Pass Sociocast results and Bit.ly phrase into Rovi to get
                # song results
                song_results=get_rovi_data("musicsearch", phrase)["searchResponse"]["results"]
                if song_results==None:
                    continue
                songs=[]
                for s in song_results:
				    try:
				        title=s["song"]["title"]
				        artist=s["song"]["primaryArtists"][0]["name"]
				    except TypeError:
				        continue
				    songs.append({"title":title,"artist":artist})
                
                each_item["songs"]=songs
	
	fout=open("./static/js/phrases.json",'w')
	json.dump(results,fout)
	fout.close()

if __name__ == '__main__':
	getCurrentSongsAndWriteToFile()


