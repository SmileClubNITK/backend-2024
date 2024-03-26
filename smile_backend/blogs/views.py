from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from .models import b_post, Comment, ContentBlock  # Import ContentBlock model

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
