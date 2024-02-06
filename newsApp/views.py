from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'newsAppTemplates/index.html')

def movieInfo(request):

    head_msg = 'latest Movie Information'
    msg1 = 'Sonaly slowelly getting cured'
    msg2 = 'Salman Going to marriage Soon'
    msg3 = 'Narendra Modi is going to act in some movie'

    dict = {

        'head_msg' : head_msg,
        'msg1' : msg1,
        'msg2' : msg2,
        'msg3' : msg3
    }
    return render(request, 'newsAppTemplates/news.html', context=dict)

def sportsInfo(request):

    head_msg = 'latest Movie Information'
    msg1 = 'Sonaly slowelly getting cured'
    msg2 = 'Salman Going to marriage Soon'
    msg3 = 'Narendra Modi is going to act in some movie'

    dict = {

        'head_msg' : head_msg,
        'msg1' : msg1,
        'msg2' : msg2,
        'msg3' : msg3
    }
    return render(request, 'newsAppTemplates/news.html', context=dict)

def politicsInfo(request):

    head_msg = 'latest Movie Information'
    msg1 = 'Sonaly slowelly getting cured'
    msg2 = 'Salman Going to marriage Soon'
    msg3 = 'Narendra Modi is going to act in some movie'

    dict = {

        'head_msg' : head_msg,
        'msg1' : msg1,
        'msg2' : msg2,
        'msg3' : msg3
    }
    return render(request, 'newsAppTemplates/news.html', context=dict)
