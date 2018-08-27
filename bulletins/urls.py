from django.urls import path, re_path
from .views import bulletin_search, searched, searchfor, get_community_bulletin, get_not_found, join_community
from .views import create_bulletin
urlpatterns = [
    path('search/', bulletin_search, name='searchpage'),
    path('search/results', searchfor, name='searchfor'),
    #path('search/results/', searched, name='searched')
    path('create_bulletin/<slug:commname>', create_bulletin, name='create_bulletin'),
    path('search/results/<slug:searchname>/<int:pg>', searched, name='searched'),
    path('community/<slug:commname>', get_community_bulletin, name='bullet'),
    path('subscribe/<slug:commname>', join_community, name='join_community'),
    path('community/not_found/<slug:notfound>', get_not_found, name='not-found'),
]
