# urls.py

from django.urls import path
from .views import PostDetailView, add_comment_to_post
from .views import team_list_view
urlpatterns = [
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('teams/', team_list_view, name='team-list'),
    path('post/<uuid:pk>/comment/', add_comment_to_post, name='add-comment'),
    
    # Other URL patterns as needed
]
