from django.urls import path
from django.http import HttpResponse
import os

from . import views

def serve_ads_txt(request):
    content = "google.com, pub-9964757532643280, DIRECT, f08c47fec0942fa0\n"
    return HttpResponse(content, content_type='text/plain')

urlpatterns = [
    path('ads.txt',          serve_ads_txt,      name='ads_txt'),
    path('welcome/',         views.welcome,      name='welcome'),
    path('about/',           views.about,        name='about'),
    path('contact/',         views.contact,      name='contact'),
    path('privacy/',         views.privacy,      name='privacy'),
    path('terms/',           views.terms,        name='terms'),
    path('blog/',            views.blog_list,    name='blog_list'),
    path('blog/how-to-build-daily-habits/',     views.blog1, name='blog1'),
    path('blog/best-productivity-tips-2026/',   views.blog2, name='blog2'),
    path('blog/how-to-stay-consistent/',        views.blog3, name='blog3'),
    path('blog/habit-tracking-for-students/',   views.blog4, name='blog4'),
    path('blog/morning-routine-tips/',          views.blog5, name='blog5'),
]
