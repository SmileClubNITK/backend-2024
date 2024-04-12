# urls.py

from django.urls import path
from .views import PostDetailView, add_comment_to_post,team_list_view
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('teams/', team_list_view, name='team-list'),
    path('post/<uuid:pk>/comment/', add_comment_to_post, name='add-comment'),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='home'),
    
    # Other URL patterns as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
