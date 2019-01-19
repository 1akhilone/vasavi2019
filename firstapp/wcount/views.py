from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#def homepage(requests):
#    return HttpResponse('<h1>Home Page</h1>')

#def about(requests):
#    return HttpResponse('<h1>About</h1>')

#def count(requests):
#    return HttpResponse('<h1>Count</h1>')

def homepage(request):
    return render(request,'wcount/homepage.html')

def about(request):
    return render(request,'wcount/about.html')

def count(request):
    fulltext = request.GET['text']
    counter = len(fulltext.split())
    word_dict = {}
    for w in fulltext.split():
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1

    word_list = [(c,word_dict[c]) for c in word_dict]
    return render(request,'wcount/count.html',{'text':fulltext,'count':counter,'word_dict':word_dict,'word_list':word_list})