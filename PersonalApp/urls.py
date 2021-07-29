
from django.urls import path

from .views import home, about, contact, post_detail, send_email,PostListView

urlpatterns = [
    path('',  home, name="home"),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('post_detail/<int:id>',post_detail, name='post_detail'),
    path('posts',PostListView.as_view(), name="posts"),
    path('send_mail', send_email, name="send_mail"),
   # path('thanks/', thanks, name="thanks"),
]
