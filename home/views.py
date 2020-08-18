# from django.shortcuts import render, HttpResponse
#
# # Create your views here.
# def home(request):
#     djtext= request.POST.get('text','default')
#     removepunc = request.POST.get('removepunc','off')
#     fullcaps = request.POST.get('fullcaps', 'off')
#     newlineremover = request.POST.get('newlineremover', 'off')
#     extraspaceremover = request.POST.get('extraspaceremover', 'off')
#     charactercounter = request.POST.get('charactercounter', 'off')
#
#     analyzed = ""
#     if removepunc=='on':
#         punctuations = '''!@#$%^&*()<>?":{}|+_,./';][\=-'''
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#         params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
#
#     if(fullcaps == "on"):
#         analyzed = ""
#         for char in djtext:
#             analyzed = analyzed + char.upper()
#         params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
#         djtext = analyzed
#         # return render(request, 'analyze.html', params)
#
#     if(newlineremover == "on"):
#         analyzed = ""
#         for char in djtext:
#             if char != "\n" and char!="\r":
#                 analyzed = analyzed + char
#         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
#         djtext = analyzed
#
#         # Analyze the text
#
#         # return render(request, 'analyze.html', params)
#
#     if(extraspaceremover == "on"):
#         analyzed = ""
#         for index, char in enumerate(djtext):
#             if not (djtext[index] == " " and djtext[index + 1] == " "):
#                 analyzed = analyzed + char
#
#         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
#         djtext = analyzed
#
#         # Analyze the text
#         # return render(request, 'analyze.html', params)
#
#     if(charactercounter == "on"):
#         analyzed = ""
#         a = djtext.replace(" ","")
#         analyzed = len(djtext)
#         # for char in djtext:
#         #     if char != " ":
#         #         analyzed = len(djtext)
#         params = {'purpose': 'Characters Counted', 'analyzed_text': analyzed}
#         # djtext = analyzed
#         # return render(request, 'analyze.html', params)
#
#     return HttpResponse(request, 'analyze.html',params)
#
# def analyze(request):
#     return render(request,'index.html')
#     #return HttpResponse('''<a href="https://www.mixupworld.com"><h1>Click Here</h1></a><br><a href="https://www.mixupworld.com"><h1>Click Here</h1></a>''')

from django.http import HttpResponse
from django.shortcuts import render


def analyze(request):
    return render(request, 'index.html')


def home(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
