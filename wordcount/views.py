from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request,'home.html',{'there':'hey hi'})

def count(request):
    fulltext=request.GET["fulltext"]
    wordcount=fulltext.split()
    worddict={}
    for word in wordcount:
        if word in worddict:
            worddict[word]=worddict[word]+1
        else:
            worddict[word]=1
    return render(request,'count.html',{'fulltext':fulltext,'Count':len(wordcount),'Worddictionary':worddict.items()})

def about(request):
    return render(request,"about.html")

def eggs(request):
    return HttpResponse("<h1>EGGS</h1>")
