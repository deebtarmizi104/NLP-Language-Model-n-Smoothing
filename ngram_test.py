#This program demonstrates steps to extract n-grams and save it in a file
import re
import os
import math
#from math import log10

def ngram():

    os.chdir("C:/Users/User5/Desktop/NLP/Codes Dataset")
    #create an empty dictionary for unigrams, bigram, trigram   
    unigram = {}  
    bigram = {}
    trigram = {}
    #using "with" will close the file immediately after last call
    with open("text-ngram.dat","r") as rfile:
        infile = rfile.readlines()

    unifile = open("unigram.dat","w")
    bifile = open("bigram.dat","w")
    trifile = open("trigram.dat","w")   
    
   
    
    sent = [s for s in infile[0].split(".")]
    
    for line in sent: 
        
        
                
        for j in range(len(line.split())-1):
            
            
            uni = line.split()[j]
            #example of storing frequency counts of unigrams
            if uni not in unigram.keys():
            	unigram[uni] = 1
            else:
                unigram[uni] += 1

            bi = line.split()[j]+" "+line.split()[j+1]
            
            #storing frequency of bigrams
            if bi not in bigram.keys():
                bigram[bi] = 1
            else:
                bigram[bi] += 1
          
            unidict = dict(unigram)
            bidict = dict(bigram)
            
            
            

        for k in range(len(line.split())-2):
            tri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]
            
            #storing frequency of trigrams
            if tri not in trigram.keys():
                trigram[tri] = 1
            else:
                trigram[tri] += 1
            
            tridict = dict(trigram)
   
    unifile = open("unigram.dat","a")
    bifile = open("bigram.dat","a")            
            
    #unifile.write(str(uni) + ":" + str(unigram[uni]) + ",")
    unifile.write(str(unidict))
    bifile.write(str(bidict))            
            
    unifile.close()
    bifile.close()
    
    trifile = open("trigram.dat","a") 
    
    trifile.write(str(tridict))
            
    trifile.close()

    #print(unigram, "\n")
    #print(bigram)
    #print(trigram)

    test_trigram = {}
       
    text = "Most mental disorders can is treatable through early detection of signs or symptoms"
    
    split_test = text.split(".")
    
    V = len(unigram) 
    
    log10_likehood = 0
    loge_likehood = 0
    
    for line in split_test:
                
                
        for k in range(len(line.split())-2):
            test_tri = line.split()[k]+" "+line.split()[k+1]+" "+line.split()[k+2]
            
            #storing frequency of the tested trigrams
            if test_tri not in test_trigram.keys():
                test_trigram[tri] = 1
            else:
                test_trigram[tri] += 1
            
            test_tri_prob = (len(re.findall(line.split()[k]+' '+line.split()[k+1]+' '+line.split()[k+2], str(sent))) + 1) / (len(re.findall(line.split()[k]+' '+line.split()[k+1], str(sent))) + V)
            
            print("P(",line.split()[k+2],"|", line.split()[k],"",line.split()[k+1],") = log10" , round(test_tri_prob, 4), " = ", round(math.log10(test_tri_prob), 4), "or loge",round(test_tri_prob, 4),"=" ,round(math.log(test_tri_prob), 4))
            
            log10_likehood += math.log10(test_tri_prob)
            loge_likehood += math.log(test_tri_prob)
            
    print("\nTrigram log base 10 likehood probability = ", round(log10_likehood, 4))
    print("\nTrigram log base e likehood probability = ",  round(loge_likehood, 4))

    
    
ngram()



