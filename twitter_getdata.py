#!/usr/bin/python
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#  - original from https://github.com/ideoforms/python-twitter-examples
#-----------------------------------------------------------------------

import codecs
import sys

from twitter import *

import unicodecsv

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://dev.twitter.com/rest/reference/get/search/tweets
#-----------------------------------------------------------------------
querystr = "#MontaAEaentae #klassikkotwiitti"
query = twitter.search.tweets(q = querystr)

#-----------------------------------------------------------------------
# How long did this query take?
#-----------------------------------------------------------------------
print "Search complete (%.3f seconds)" % (query["search_metadata"]["completed_in"])

#-----------------------------------------------------------------------
# Loop through each of the results, and print its content.
#-----------------------------------------------------------------------

id = ""
query = twitter.search.tweets(q = querystr, max_id = id, count=100)
#print "Nbr of results :", len (query["statuses"])

with open("monta_data.csv", "wb") as outfile:
	w = unicodecsv.writer(outfile,encoding="utf-8",delimiter=";",quoting=unicodecsv.QUOTE_MINIMAL)

	while len(query["statuses"]) >= 1:

		for result in query["statuses"]:
			
			if result["text"]!=None:
				puts = result["text"] 
			else:
				puts = ""

			name     = result["user"]["screen_name"].replace("\n"," ")
			id       = result["id_str"]
			rtcount  = result["retweet_count"]
			favcount = result["favorite_count"]
			twurl    = "%s/%s/status/%s" % ("https://twitter.com",str(name),id)

			print "%s;(%s);@%s;%s;%s;%s;%s" % (id, result["created_at"], name,  puts, rtcount, favcount, twurl)

			w.writerow([id, result["created_at"], name,  puts, rtcount, favcount, twurl ])



		#print "Last one from set"+id
		query = twitter.search.tweets(q = querystr, max_id = id)
		query["statuses"].pop(0)  #drop first as it was already in last set.


