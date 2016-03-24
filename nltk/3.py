'''
Created on May 17, 2015

@author: edwingsantos
'''

import sqlite3
import time
import urllib2
from urllib2 import urlopen
import re
import cookielib, urllib2
import datetime
from cookielib import CookieJar
import nltk
from bs4 import BeautifulSoup


cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

conn = sqlite3.connect('knowledgeBase.db')
conn.text_factory = str # the fetched data will be printed out as string not unicode
c = conn.cursor()

startingWord = 'ugly'
startingWordValue = -1

synArray = []


def main():
    try:
        page = 'http://thesaurus.com/browse/'+startingWord+'?s=t'
        sourceCode = opener.open(page).read()
        #print sourceCode
        try:
        
            
            soup = BeautifulSoup(sourceCode)
            
            print soup
            
            for a in soup.find_all('span', {'class','text'}):
                print '>> ', a.text
                query = "SELECT * FROM wordsVal WHERE word=?"
                c.execute(query, [(a.text)])
                data = c.fetchone()
                
                
                if data is None:
                    print 'Word not in the data base '
                    c.execute("INSERT INTO wordsVal(word, value) VALUES(?,?)", (a.text, startingWordValue))
                    conn.commit()
                
                else: 
                    print 'Word already exists'
                    
                
                
        except Exception, e:
            print 'Failed in second loop'
            print str(e)
            
    except Exception, e:
        print 'Failed in the main loop'
        print str(e)


def createTable():
    c.execute('''CREATE TABLE IF NOT EXISTS  wordsVal(word TEXT, value REAL)''')
    print 'Table Created'
    conn.commit()
    
def doneWord(startingWordQ, startingWordValueQ):
    c.execute("INSERT INTO doneSyn(word, value) VALUES(?,?)", (startingWordQ, startingWordValueQ))
    print 'Word ', startingWordQ, ' already in the database.'
    conn.commit()
    
#createTable()    

main()

doneWord(startingWord, startingWordValue)





