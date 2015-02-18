import re
import datetime
import struct
import urllib
import feedparser
import requests
import bs4
from client.app_utils import getTimezone
from semantic.dates import DateService

WORDS = ["WOLFRAM"]

def handle(text, mic, profile):
	mic.say("You are in the wolfram module")

def isValid(text):
	if "WOLFRAM" in text:
		return True
	return False
