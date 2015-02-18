import re
import datetime
import struct
import urllib
import feedparser
import requests
import bs4
from client.app_utils import getTimezone
from semantic.dates import DateService

from subprocess import call
call("clear")
import sys
import urllib2
import httplib
from xml.etree import ElementTree as etree

WORDS = ["WOLFRAM"]

def handle(text, mic, profile):
	mic.say("You are in the wolfram module")
	appid = '4J7JG7-AEVLAH86AP'
	query = sys.argv[1]
	print 'Querying: ', query
	w = wolfram(appid)
	w.search(query)


class wolfram(object):
	def __init__(self, appid):
		self.appid = appid
		self.base_url = 'http://api.wolframalpha.com/v2/query?'
		self.headers = {'User-Agent':None}
def isValid(text):
	if "WOLFRAM" in text:
		return True
	return False
