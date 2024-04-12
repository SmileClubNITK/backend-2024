from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from .models import b_post, Comment, ContentBlock,Team ,Event # Import ContentBlock model

class PostDetailView(DetailView):
    model = b_post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the post object
        post = self.object
        # Retrieve content blocks ordered by 'order' field
        content_blocks = ContentBlock.objects.filter(post=post).order_by('order')
        # Add post and content blocks to the context
        context['post'] = post
        context['content_blocks'] = content_blocks
        return context

def add_comment_to_post(request, pk):
    post = get_object_or_404(b_post, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(post=post, user=request.user, content=content)
        return redirect('post-detail', pk=pk)
    # Pass the post object to the template with a valid ID
    return render(request, 'post_detail.html', {'post': post})

def blog_list(request):
    """View function to display a list of blog posts."""
    posts = b_post.objects.filter(status='published')  # Get all published blog posts
    context = {'posts': posts}
    return render(request, 'blog_list.html', context)
def post_detail(request, post_id):
    # Retrieve the post object or return 404 if not found
    post = get_object_or_404(b_post, id=post_id)

    # Render the template with the post object
    return render(request, 'post_detail.html', {'post': post})
def team_list_view(request):
    team_members = Team.objects.all()
    return render(request, 'about.html', {'team_members': team_members})

def event_list(request):
    """View function to display a list of events sorted by event_date."""
    events = Event.objects.order_by('event_date')  # Fetch events sorted by event_date
    context = {'events': events}
    return render(request, 'timeline.html', context)