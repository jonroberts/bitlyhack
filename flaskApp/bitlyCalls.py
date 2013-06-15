import requests
import json
import settings
import sys

def getStory(phrase):
	query_params = {'access_token': settings.BITLY_ACCESS_TOKEN,'phrases':phrase}

	endpoint = "https://api-ssl.bitly.com/v3/story_api/story_from_phrases"
	response = requests.get(endpoint, params = query_params)
	data = json.loads(response.content)

	return data["data"]["story_id"]
	
def getStoryMetaData(storyLink):

	# We can get the following
	# rates => Float, current clickrate of the story
	# titles => list of page titles
	# images => list of relevant images
	# related => list of related pages
	# shares => Integer, number of times the story has been shared
	# encoders => Integer, number of times the story have been encoded
	# clicks => Integer, total number of clicks on the story

	# meta_data *needs* a fields designator
	query_params = {'access_token': settings.BITLY_ACCESS_TOKEN,"story_id":storyLink,"field":["clicks","titles"]}

	endpoint = "https://api-ssl.bitly.com/v3/story_api/metadata"
	response = requests.get(endpoint, params = query_params)
	data = json.loads(response.content)

	return data["data"]

def getBurstingPhrases():
	query_params = {'access_token': settings.BITLY_ACCESS_TOKEN}

	endpoint = "https://api-ssl.bitly.com/v3/realtime/bursting_phrases"
	response = requests.get(endpoint, params = query_params)

	results_out=[]

	data = json.loads(response.content)

	phrases=data["data"]["phrases"]

	for i in range(len(phrases)):
		phrase=phrases[i]["phrase"]
		story_id=getStory(phrase)
		results=getStoryMetaData(story_id)

		out={"phrase":phrase,"top_link":phrases[i]["urls"][0],"story_id":story_id,"titles":results["titles"]}
		results_out.append(out)
	return results_out

def getHotPhrases():
	query_params = {'access_token': settings.BITLY_ACCESS_TOKEN}

	endpoint = "https://api-ssl.bitly.com/v3/realtime/hot_phrases"
	response = requests.get(endpoint, params = query_params)

	results_out=[]

	data = json.loads(response.content)

	phrases=data["data"]["phrases"]

	for i in range(len(phrases)):
		phrase=phrases[i]["phrase"]
		story_id=getStory(phrase)
		results=getStoryMetaData(story_id)

		out={"phrase":phrase,"top_link":phrases[i]["urls"][0],"story_id":story_id,"titles":results["titles"]}
		results_out.append(out)
	return results_out
	



if __name__ == '__main__':            
	getHotPhrases()


