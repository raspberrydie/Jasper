import re
import datetime
import struct
import urllib
import feedparser
import requests
import bs4
from client.app_utils import getTimezone
from semantic.dates import DateService

WORDS = ["BOSS"]

def handle(text, mic, profile):
	print("handling")

def isValid(text):
	if "BOSS" in text:
		return True
	return False
