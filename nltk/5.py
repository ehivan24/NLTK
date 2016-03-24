'''
Created on May 25, 2015

@author: edwingsantos


from nltk.corpus import wordnet

sys = wordnet.synsets('walk')
print sys[0].lemmas()[0].name()

print sys[0].definition()
print sys[0].examples()

synonyms = []
antonyms = []

for sys in wordnet.synsets("good"):
    
    for l in sys.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
            
            
#print (set(synonyms))
#print (set(antonyms)) 

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')


print w1.wup_similarity(w2)

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')

print w1.wup_similarity(w2)

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')   
            
print w1.wup_similarity(w2)

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cactus.n.01')   
            
print w1.wup_similarity(w2)      


'''  