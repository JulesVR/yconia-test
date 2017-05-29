from django.conf.urls import url
from . import views

urlpatterns = [
    # /r/
    url(r'^$', views.index, name='index'),
    # /r/all/
    #url(r'^all/$', views.show_all, name='show_all'),
    # /r/popular/
    #url(r'^popular/$', views.show_popular, name='show_popular'),
    # /r/search/
    url(r'^searchsubs/$', views.search_subs, name='search_subs'),
    #/r/get_images/
    url(r'^get_images/$', views.get_images, name='get_images'),
    # # /r/subreddit/
    url(r'^(?P<name>[a-z]+)/$', views.toSubreddit, name='subreddit'),
    # /r/makeDB/
    url(r'^makeRedditDB/$', views.makeRedditDB, name='makeRedditDB'),
]