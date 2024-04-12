# urls.py

from django.urls import path
from .views import PostDetailView, add_comment_to_post,team_list_view,event_list,blog_list,post_detail
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', team_list_view, name='team-list'),
    path('post/<uuid:post_id>/', post_detail, name='post-detail'),
    path('time/', event_list, name='event-list'),
    path('blogs/', blog_list, name='blogs-list'),
    path('post/<uuid:pk>/comment/', add_comment_to_post, name='add-comment'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('timeline/', TemplateView.as_view(template_name='timeline.html'), name='timeline'),
    
    # Other URL patterns as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
