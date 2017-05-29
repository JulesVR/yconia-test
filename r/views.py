from django.http import HttpResponse, Http404
from .models import Subreddit, ImageObject
from django.shortcuts import render, render_to_response
from random import randint
import praw
import urllib.request
import io
from PIL import Image
import json

def index(request):
    all_subreddits = Subreddit.objects.all()
    context = {'all_subreddits' : all_subreddits}
    return render(request, 'r/index.html', context)


def index1(request):
    redditt = praw.Reddit(client_id='vxUUzUOoYk6JOw',
                          client_secret='l7XgxK-KpKbLwZZttWRefSeQXQA',
                          password='19121996',
                          username='mrsmirkface',
                          user_agent='r0596538')
    subredditt = redditt.subreddit("blackpeopletwitter")
    submissions = subredditt.hot(limit=20)
    submissions_list = list(submissions)
    submissions_list2 = submissions_list.copy()
    for submission in submissions_list2:
        if not submission.url.endswith('.jpg'):
            submissions_list.remove(submission)
    response = ''
    i = 0
    for submission in submissions_list:
        response += "<img src="+submissions_list[i].url+"><br><h1>"+submissions_list[i].title+"</h1>"
        i+=1
    return HttpResponse(response)


def makeRedditDB(request):
    all_subreddits= Subreddit.objects.all()
    all_subreddit_names = set()
    for subreddit in all_subreddits:
        all_subreddit_names.add(subreddit.name)
    subreddits_to_add = ['BlackPeopleTwitter',
                         'OldSchoolCool',
                         'DankMemes',
                         'Funny',
                         'EarthPorn',
                         'NoTitle',
                         'woahdude',
                         'Eyebleach',
                         'WTF',
                         'thingsforants',
                         'classiccars',
                         'interestingasfuck',
                         'musclecar',
                         'dogpictures']
    thumbnails_of_subreddits_to_add =['https://i.imgur.com/meaXyUys.jpg',
                                      'https://i.imgur.com/ikdldjas.jpg',
                                      'https://i.imgur.com/wfDHjISs.jpg',
                                      'https://i.imgur.com/lsoomRqs.jpg',
                                      'https://i.imgur.com/Nubk9vBs.jpg',
                                      'https://i.imgur.com/OvjydVns.jpg',
                                      'https://i.imgur.com/fwgGV3Gs.jpg',
                                      'https://i.imgur.com/m2RyXcos.jpg',
                                      'https://i.imgur.com/r8q4G9ts.jpg',
                                      'http://i.imgur.com/8AUC927s.jpg',
                                      'http://i.imgur.com/e8X40gvs.jpg',
                                      'http://i.imgur.com/9njIFuVs.jpg',
                                      'https://i.imgur.com/YnV3sGls.jpg',
                                      'https://i.imgur.com/FxRYpwfs.jpg']
    redditt = praw.Reddit(client_id='vxUUzUOoYk6JOw',
                          client_secret='l7XgxK-KpKbLwZZttWRefSeQXQA',
                          password='19121996',
                          username='mrsmirkface',
                          user_agent='r0596538')
    for subreddit in subreddits_to_add:
        #If the subreddit is not in the database, create it
        if subreddit not in all_subreddit_names:
            x = randint(2,200)
            y = ''
            if (x // 60) > 0:
                y = str(x//60)+"h"
            else:
                y = str(x)+"m"
            a = Subreddit(name=subreddit, thumbnail=thumbnails_of_subreddits_to_add[subreddits_to_add.index(subreddit)],
                          time_ago_of_last_update=y)
            a.save()
            subredditt = redditt.subreddit(subreddit)
            submissions = subredditt.hot(limit=20)
            submissions_list = list(submissions)
            submissions_list2 = submissions_list.copy()
            for submission in submissions_list2:
                if (not submission.url.endswith('.jpg') and not submission.url.endswith('.png')):
                    submissions_list.remove(submission)
            for submission in submissions_list:
                w, h = get_size(str(submission.url))
                b = ImageObject(sub=a, sub_name=subreddit, url=str(submission.url), caption=str(submission.title),
                                width=w, height=h)
                b.save()
        #If the subreddit is in the database, update it
        else:
            a = Subreddit.objects.filter(name=subreddit).first()
            subredditt = redditt.subreddit(subreddit)
            submissions = subredditt.hot(limit=20)
            submissions_list = list(submissions)
            submissions_list2 = submissions_list.copy()
            for submission in submissions_list2:
                if (not submission.url.endswith('.jpg') and not submission.url.endswith('.png')):
                    submissions_list.remove(submission)
            image_objects_from_subreddit = ImageObject.objects.filter(sub_name=subreddit)
            image_urls = list()
            for image_object in image_objects_from_subreddit:
                image_urls.append(image_object.url)
            for submission in submissions_list:
                if not image_urls.__contains__(str(submission.url)):
                    w, h = get_size(str(submission.url))
                    b = ImageObject(sub=a, sub_name=subreddit, url=str(submission.url), caption=str(submission.title),
                                    width=w, height=h)
                    b.save()
    return HttpResponse("<h1>Subreddits were added to the database.</h1>")


def toSubreddit(request, name):
    return HttpResponse("<h1>This is an image from the subreddit "+str(name)+ ".</h1>")


def search_subs(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    subs = Subreddit.objects.filter(name__contains=search_text)

    return render_to_response('r/ajax_search.html', {'subs' : subs})

def get_size(URL):
    with urllib.request.urlopen(URL) as url:
        f = io.BytesIO(url.read())
    im = Image.open(f)
    width, height = im.size
    return width, height

# def get_images(request):
#     if request.method == "GET":
#         subreddit_name = request.GET['subreddit_name']
#     else:
#         search_text = ''
#     image_objects = ImageObject.objects.filter(subreddit_name=subreddit_name)
#
#     return render_to_response('r/get_images.html',{'image_objects' : image_objects})



def get_images(request):
    if request.method == "GET":
        subreddit_name = request.GET['subreddit_name']
        image_objects = ImageObject.objects.filter(sub_name=subreddit_name).values()
        image_objects_result = [entry for entry in image_objects]  # converts ValuesQuerySet into Python list
        data = json.dumps(image_objects_result)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404