'''
Created on May 28, 2015

@author: edwingsantos
'''

##
# extract the image from the coordinates letter
##


import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import time 
import sqlite3
from scipy.misc import *
import os
import re
import glob
from collections import Counter
from findertools import sleep

np.set_printoptions(threshold=np.nan) # display the entire array

conn = sqlite3.connect('pixels.db')
conn.text_factory = str # the fetched data will be printed out as string not unicode
c = conn.cursor()


def createTable():
    c.execute('''CREATE TABLE  IF NOT EXISTS alpha (name text, data text)''')
    conn.commit()
    print 'Table Created '

def checkValues():
    for row in c.execute('SELECT * FROM alpha'):
        print row[0], row[1]

##
##
##
def replaceVals(listIn, oldVal, newVal):
    while oldVal in listIn:
        inx = listIn.index(oldVal)
        listIn.pop(inx)
        listIn.insert(inx, newVal)
    
def drawImage(img):
    im2 = Image.fromarray(img)
    plotResults(im2, 'lower', 'Image')

def openImageIntoPixels(img): 
    try:
        i = imread('data/'+img)
            
        nameImage = str(img)
        
        air = np.array(i)
        
        (x,y,z) = np.shape(air)
        
        
    except Exception, e:
        print 'Error found ', e
        exit()
    
    data = [] 
    
    sql = 'SELECT data FROM alpha WHERE name = ?'
    
    for row in c.execute(sql, [(nameImage)]):
        data.append(row)

          
    air2 = re.findall(r'\d+' , str(data)) #the info retrived from the database
    air = re.findall(r'\d+', str(air))
            
    sql2 = 'SELECT name, data FROM alpha WHERE data = ?'
    
    for name, rows in c.execute(sql2, [(str(air))]):
        print 'name ', name
     
    
    results = map(int, air2 )
    
    
    print 'before ', results
     
   
    for eachPix in results:
        if results[eachPix] < 50: 
            results.pop(eachPix)
            results.insert(eachPix, 0)
                
        elif results[eachPix] > 200:
            results.pop(eachPix)
            results.insert(eachPix, 255)   
        
    print 'after  ', results

    results = np.reshape(results,(x, y, z))
    
    ims = Image.fromarray(np.uint8(results))
    
    #plotResults(ims, 'lower', 'from contructed array')
    #plotResults(i, 'upper', 'from image')
        
def plotResults(img, origin, title):
    fig = plt.figure()
    plt.title(title)
    plt.imshow(img, origin=origin)
    plt.show()
    
def checkiningDatabase():
    
    file = open('numbers.txt', 'a')
    try:
        
        sql = 'SELECT name, data from alpha'
        
        for name, row in c.execute(sql):
            row = re.findall(r'\d+', str(row))
            row = map(int, row)
            print row
            #print name , ' :::: ' , allLists
            file.write(name+':'+str(row)+'\n')
            time.sleep(1)
            
        file.close()
       
    except Exception, e:
        print e
    
def countImages():
    number = []
    for filename in glob.glob('data/*.png'):
        number.append(filename) 
    
    return len(number)
    

def main():

    img = 'digits.png'
    
    im = cv2.imread(img)
    
    img2 = im.copy()
    
    out = np.zeros(im.shape, np.uint8)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, 1,1,11,2)
    countors, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    
    increment = countImages()  # gets the number of Images and starts the count
    for cnt in countors:
        if cv2.contourArea(cnt)> 50:   
            [x,y,w,h] = cv2.boundingRect(cnt)
            if h > 28:
                cv2.rectangle(im,(x,y),(x+w, y+h), (0, 255,0),2)
                roi = thresh[y:y+h, x:x+w]
                roismall = cv2.resize(roi, (10, 10))
                roismall = roismall.reshape((1, 100))
                roismall = np.float32(roismall)
                
                mask = np.zeros(gray.shape, np.uint8)
                
                cv2.drawContours(mask, [cnt], -1, 255, -1)
                pixelpoints = np.transpose(np.nonzero(mask))
                
                croppedImage = img2[y:y+h, x:x+w]
                
                im = cv2.bitwise_and(img2, img2, mask = None)
                
                namePic = str(increment) + '.png' 
                
                cv2.imshow('data/'+namePic, croppedImage)   
                
                cv2.imwrite('data/'+namePic, croppedImage)
                
                i = Image.open('data/'+str(increment) + '.png')
                eir = np.array(i)
                
                eir = re.findall(r'\d+', str(eir)) #save the numbers
                
                
                c.execute("INSERT INTO alpha(name, data) VALUES(?,?)", (namePic, str(eir)))
                conn.commit()
                
                print 'Added to the data base: ', namePic
                increment += 1
                time.sleep(3)
                cv2.destroyWindow(namePic)
                
        
    cv2.imshow('im', im)
    cv2.waitKey(0)

'''
    find a way to compare the results from the database and the image to be analized.

'''
    
def compareImage(img):
    try:
        i = imread('data/'+img)
        air = np.array(i)
        air = re.findall(r'\d+', str(air))
        arraytoCompare = map(int, air)
    
        
        
        #print arraytoCompare
        databasefile = open('numbers.txt','r').read()
        databasefile = databasefile.split('\n')
        matchArray = []
        for line in databasefile:
            
            splitExample =  line.split(':')
            nameFile =  splitExample[0]
            dataArray = splitExample[1]
            dataArray = re.findall(r'\d+', dataArray)
            dataArray = map(int, dataArray)
            sum = 0

            for number in dataArray:
                
                #print number
                
                if number == 255:
                    sum =+ 1
            
            print sum ,' >> ', nameFile
            
            
        x = Counter(matchArray)
        print x
            
    except Exception, e:
        print e
    

compareImage('7.png')
print 'Total Images in database: ',  countImages()


#https://www.youtube.com/watch?v=-vVskDsHcVc&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL&index=12






