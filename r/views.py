from django.http import HttpResponse
import praw

# Create your views here.


def index1(request):
    return HttpResponse("<h1>This is the subreddit category page.</h1>")


def index(request):
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

def makeDB(subredditname):
    # a = Subreddit(name=subredditname)
    # a.save()
    redditt = praw.Reddit(client_id='vxUUzUOoYk6JOw',
                          client_secret='l7XgxK-KpKbLwZZttWRefSeQXQA',
                          password='19121996',
                          username='mrsmirkface',
                          user_agent='r0596538')
    subredditt = redditt.subreddit(subredditname)
    submissions = subredditt.hot(limit=20)
    submissions_list = list(submissions)
    submissions_list2 = submissions_list.copy()
    for submission in submissions_list2:
        if not submission.url.endswith('.jpg'):
            submissions_list.remove(submission)
    # for submission in submissions_list:
    #     b = ImageObject(sub=subredditname, url=submission.url,caption=submission.title)
    #     b.save()


