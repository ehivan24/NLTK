'''
Created on May 14, 2015

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

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

conn = sqlite3.connect('knowledgeBase.db')
conn.text_factory = str # the fetched data will be printed out as string not unicode
c = conn.cursor()

visitedLinks=[]

def createTable():
    c.execute('''CREATE TABLE  IF NOT EXISTS knowledgeBaseTable (unix text, dateStamp text, namedEntity text, relatedWord text)''')
    conn.commit()

def processor(data):
    try:
        tokenized = nltk.word_tokenize(data)
        tagged = nltk.pos_tag(tokenized)
        namedEnt = nltk.ne_chunk(tagged, binary=True)
       
        #print namedEnt
       
        entities = re.findall(r'VB\s(.*?)/', str(namedEnt))
        
        descriptives = re.findall(r'\(\'(\w*)\',\s\'JJ\w?\'', str(tagged)) #finds all the adjectives
        #print entities
        
        if len(entities) > 1:
            pass
        elif len(entities) == 0:
            pass
        else:
            print '__'*15
            print 'Named: ', entities
            print "Descriptions:[adjetives_] "
            for eachDesc in descriptives:
                print eachDesc
                
                currentTime = time.time()
                dateStamp = datetime.datetime.fromtimestamp(currentTime).strftime('%Y -%m-%d %H:%M:%S')
                namedEntity = entities[0]
                relatedWord = eachDesc
                
                c.execute("INSERT INTO knowledgeBaseTable (unix, dateStamp, namedEntity, relatedWord) VALUES (?,?,?,?)", 
                          (currentTime, dateStamp, namedEntity, relatedWord))
                          
                print 'data added to the database... ' 
                conn.commit()
            
            print '__'*15
    
    except Exception, e:
        #print 'filed on the processor first loop'
        print str(e)


    
def checkItems():
    for row in c.execute('SELECT * FROM knowledgeBaseTable'):
        
        
        #prints the parsed unix time 
        print datetime.datetime.fromtimestamp(float(row[0]))
        print row[2], row[3]
            
def main():
    try:
        page = 'http://www.myajc.com/'
        sourceCode = opener.open(page).read().decode('latin1')
        
        try:
        
            links = re.findall(r'<link.*?href=\"(.*?)\"', sourceCode)
            for link in links:
                if '.rdf' in link:
                    
                    pass
                elif link in visitedLinks:
                    print 'link already visited '
                
                else:
                    visitedLinks.append(link)
                    print 'Vistinting Link'
                    print '***'*15
                    
                    linkSource = opener.open(link).read()
                    linesOfInterest = re.findall(r'<p>(.*?)</p>',str(linkSource))
                    print 'Content: '
                    for eachLine in linesOfInterest:
                        if '<img width' in eachLine:
                            pass
                        elif '<a href=' in eachLine:
                            pass
                        elif '\xe2' in eachLine: # all the quotation marks 
                            pass
                        else:
                            print eachLine
                            processor(eachLine)
                        
                    #time.sleep(555)    
                    
        except Exception, e:
            print 'failed in the second loop'
            print str(e)
            
        
    except Exception, e:
        print 'failed in the main loop'
        print str(e)


def readDatabase(wordUsed):
    
    sql = "SELECT * FROM knowledgeBaseTable WHERE relatedWord =? "
    
    for row in c.execute(sql, [(wordUsed)]):
        print row




'''
while 1 < 2:
    currentTime = time.time()
    dateStamp = datetime.datetime.fromtimestamp(currentTime).strftime('%Y -%m-%d %H:%M:%S')
    main()
    time.sleep(5)
    print 'sleeping '
    print dateStamp
'''

#checkItems()

readDatabase('new')

