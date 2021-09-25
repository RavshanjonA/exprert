from django.urls import path

from news.views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='home'),

]
