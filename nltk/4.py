
Review1 =  '''
I'm really enjoying this book. 
I have a background in C but found the java coding in the book quite straightforward. 
Best to use an IDE an avoid my mistake of trying to extend the pom.xml. 
Also be aware that you will need to track down some dependencies for the repository that's cited in the book - jar's for classifier4j are not included, 
so don't expect to clone in and have everything build straight away.

I'm pretty sure the author stuffed up the first example in the book around Users Purchase History. 
Confusingly, he sort of disregards "Did purchase" in his entropy calculation example and uses "has account credit" to split an entropy calculation for "read reviews". 
We don't see some of the other working but the end results don't seem quite right [although don't take my word for it, I'm not a stats major by any means].
However, by looking at the data you can see that it's "previous customer" that is slightly better than either "has credit account" or "read reviews" for predicting a purchase 
(the two latter are both equal predictors). 
It would certainly take some argument to convince me that "Reads reviews" was so much better than "Has credit account" when in terms of raw data at predicting "Did purchase" they're exactly the same - 
so I just don't trust this example. 
Maybe the purpose of the exercise wasn't about predicting "Did purchase", but that would surely confuse everybody about why that column was there and what the whole point was?
'''


Review2 = '''

I am somewhat disappointed by this book. Today I'm feeling generous, 
but it was tough to bump this up from 2-stars because to me it at times created more confusion than anything else.

First off, this is an introduction certainly, probably at the sophomore college level. 
The math is there but not used especially well, 
and I believe the intention of the book is to sort of cater to those whose math backgrounds aren't very good. 
There is certainly a need for a book like this, but it shouldn't be used for more than supplementary material.

There are many errors in this book, sometimes typographical but other times a little more serious. T
he writing style puts a bit of stress on the reader and I find myself jumping around the paragraph sometimes trying to figure out what is being said. 
The tone is meant to be casual and simple, but coupled with the numerous errors in the book it really felt like this edition was rushed. 
This was the most disappointing aspect.

This book was useful to me for clarifying some things, 
but only because it was a different explanation that wasn't bogged down in mathematical rigor. 
I think it is a very good idea to have several books on the same subject for which you are studying seriously 
(I have three or four books on quantum mechanics, and even then it took many reads through them to really understand it). 
This book served its purpose in that sense. I also bought it because I was eagerly awaiting deep learning topics to find their way into ML texts. 
Sadly, this book didn't help me as I had been reading papers at this point, but I think it was a good introduction to deep learning and the 
types of neural networks typically used to build them and I applaud this initial effort by the author to include the material. 
I did find a few mistakes in the earlier chapters on Hopfield networks specifically, but I don't remember them being serious.

I'm a Python programmer who uses Numpy a lot, and this was the best feature of this book. 
Most of the time I could quickly glance at the code and see what was really happening, 
and looking over the included code clarified some things for me as well. 
For textbooks in computational areas nowadays there's no excuse for not providing code, 
and I'm very glad to have had that to look at.

Overall, this book could have been a lot better and has the potential to be a really great introduction to ML as its own textbook 
(at the underclass level, i.e. freshman and sophomore). 
The author simply didn't put in enough time to revising, 
or perhaps it was the editor's fault, not sure. The heavy usage of actual code was a big plus for me, 
and it covered some topics that aren't typically covered (deep neural networks) which was done well. 
For someone who is somewhat familiar with ML, this is a decent book to sprint through just to review and glean some bits and pieces. 
For the beginner, it can be a good introduction especially if you aren't as good at math as you'd like to be, 
but I'd recommend using it as a supplement to something at a higher level (perhaps Bishop's or Alpaydin's book, or even David Barber's book).

'''

Review3 = ''' gross , bad, garbage'''


Review4 = '''  '''



import sqlite3
import time

conn = sqlite3.connect('knowledgeBase2.db')
c = conn.cursor()
conn.text_factory = str

negativeWords = []
positiveWords = []
neutralWords = []

sql = "SELECT * from wordVals WHERE value = ?"



def loadWordsArrays():
    for negRow in c.execute(sql, [(-1)]):
        negativeWords.append(negRow[0])
    print 'Negative Words Loaded '

    for posRow in c.execute(sql, [(1)]):
        positiveWords.append(posRow[0])
    print 'Positive Words loaded '
    
    for posRow in c.execute(sql, [(0)]):
        neutralWords.append(posRow[(0)])
    print 'Neutral Words loaded '

def testing(review):
    
    WordcounterPos = 0
    WordcounterNeg = 0
    WordcounterNeutral = 0
    
    for eachPosWord in positiveWords:
        if eachPosWord in review:
            WordcounterPos += 1
            print 'Positive Words >> ', eachPosWord
            
            
    for eachNegWord in negativeWords:
        if eachNegWord in review:
            WordcounterNeg += 1
            print 'Negative Words >> ', eachNegWord
            
            
    for eachNeutralWord in neutralWords:
        if eachNeutralWord in review:
            WordcounterNeutral += 1
            print 'Neutral Words >> ', eachNeutralWord

    print '--'*50      
          
    if (WordcounterPos > WordcounterNeg) and (WordcounterPos > WordcounterNeutral):
        print 'Positive text ' 
        
    if (WordcounterNeutral > WordcounterPos) and (WordcounterNeutral > WordcounterNeg):
        print 'Neutral text'
    if (WordcounterNeg > WordcounterPos) and (WordcounterNeg > WordcounterNeutral):
        print 'Negative text'
    if WordcounterPos == WordcounterNeg:
        print 'Neutral text'
    
    
    
    words = review.split()
    
    print 'Negative Words found, ',WordcounterNeg , ' Positive Words found, ' , WordcounterPos, ' Neutral words found ', WordcounterNeutral  
    print 'Total chars processed ', [x for x in enumerate(words)]
    
    print '%%'*50
    
    

loadWordsArrays()
testing(Review3)    





