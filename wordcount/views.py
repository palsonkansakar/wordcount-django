from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request): #request object tells us about url and information of users 
    #return 'Hello' --> cant send string. we have to give back http response
    #return HttpResponse('Hello')
    return render(request,'home.html' ) #can send dictionaries like {'HITHERE':'THIS IS ME'}

def count(request):
    fulltext= request.GET['fulltext']

    wordlist = fulltext.split() #split up string into list of words
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #INcrease
            worddictionary[word] += 1

        else:
            #add to dictionary
            worddictionary[word] = 1
    
    sortedwords= sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
    return render(request,"about.html")
