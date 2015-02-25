import re
import datetime
import struct
import urllib
import feedparser
import requests
import bs4
from client.app_utils import getTimezone
from semantic.dates import DateService
import urllib2
import httplib
from xml.etree import ElementTree as etree
 
WORDS = ["WOLFRAM"]

def handle(text, mic, profile):
	#mic.say("You are in the wolfram module")
    appid = '4J7JG7-AEVLAH86AP'
    query = text
    w = wolfram(appid)
    w.search(query)

def isValid(text):
    if text != "":
	print("checking wolf")
        return True

    print("skipping wolf")
    return False

class wolfram(object):
    def __init__(self, appid):
        self.appid = appid
        self.base_url = 'http://api.wolframalpha.com/v2/query?'
        self.headers = {'User-Agent':None}
 
    def _get_xml(self, ip):
        url_params = {'input':ip, 'appid':self.appid}
        data = urllib.urlencode(url_params)
        req = urllib2.Request(self.base_url, data, self.headers)
        xml = urllib2.urlopen(req).read()
        return xml
 
    def _xmlparser(self, xml):
        data_dics = {}
        tree = etree.fromstring(xml)
        #retrieving every tag with label 'plaintext'
        for e in tree.findall('pod'):
            for item in [ef for ef in list(e) if ef.tag=='subpod']:
                for it in [i for i in list(item) if i.tag=='plaintext']:
                    if it.tag=='plaintext':
                        data_dics[e.get('title')] = it.text
        return data_dics
 
    def search(self, ip):
        xml = self._get_xml(ip)
        result_dics = self._xmlparser(xml)
        #return result_dics 
        #printXml(result_dics)
        print result_dics
        #print result_dics['Result']

    def printXml (result):
        for item in result:
            print item
