from django.shortcuts import render

from oauth2client.service_account import ServiceAccountCredentials
from urllib.parse import urlparse, parse_qs
from urllib import parse as urlpars
from django.http import HttpResponse
from django.template import loader
import psycopg2 as postgres
import requests
import json
import os


#Postgresql configuration
'''
	Run the following command after having logged into heroku on your terminal to copy the current local database to heroku, that is assuming that you have a populated database.
	
	Add the addon
	heroku addons:create heroku-postgresql:hobby-dev
	
	Push local database to heroku
	heroku pg:push your_database_name DATABASE_URL --app your_appname

	Pull database from heroku
	heroku pg:pull database_name mylocaldb --app your_appname
	
	For more features and settings visit: https://devcenter.heroku.com/articles/heroku-postgresql
'''

#DB Connection
try:
	#Local database connection
	conn = postgres.connect(dbname = "heroku", host = "localhost", user = "postgres")
except:
	#Heroku database connection
	urlpars.uses_netloc.append("postgres")
	url = urlpars.urlparse(os.environ["DATABASE_URL"])

	conn = postgres.connect(
	    database=url.path[1:],
	    user=url.username,
	    password=url.password,
	    host=url.hostname,
	    port=url.port
	)

#Cursor
cur = conn.cursor()

#index
def index(request):

	template, title = loader.get_template('index.html'), "WCIWT"

	elements = {"title" : title, "value" : ""}
	return HttpResponse(template.render(elements))


#search
def search(request):

	query = request.GET.get('query').strip()
	services, array = ['prime', 'netflix', 'hotstar'], []

	#Get top 10 entries from tables
	for service in services:
		cur.execute("SELECT * FROM " + service + " WHERE title ~* '" + query.replace("'", "''") + "'")
		array.append(cur.fetchmany(10))


	#If zero entires are retured, run a Trigram/Trigraph query to fetch 10 top entires
	if len(array[0]) == 0 and len(array[1]) == 0 and len(array[2]) == 0:
		del array[:]
		array = []
		for service in services:

			#Trigram query
			cur.execute("SELECT title, similarity(title, '" + 
				query.replace("'", "''") + "') AS similarity FROM " + 
				service + " WHERE title % '" + query.replace("'", "''") + 
				"' ORDER BY similarity DESC;")

			array.append(cur.fetchmany(10))

		#If Trigram query returns zero entries, serve an empty JSON
		if len(array[0]) == 0 and len(array[1]) == 0 and len(array[2]) == 0:
			elements = {"title" : query, "value" : query, "notfound": query}

		else:
			elements = getjson(array, query)

	else:
		elements = getjson(array, query)

	template = loader.get_template('search.html')
	return HttpResponse(template.render(elements))


#Return a json element
def getjson(array, query):
	return ({"title" : query, "value" : query, "prime" : array[0], "netflix" : array[1], "hotstar" : array[2]})