from django.db import models
from django.urls import reverse
import uuid  # Required for unique post instances
from django.contrib.auth.models import User  # Import the User model

class b_post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.RESTRICT, null=True, related_name='posts')
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = models.CharField(max_length=255, blank=True)  # Optional comma-separated tags
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this post."""
        return reverse('post-detail', args=[str(self.id)])


class Author(models.Model):
    """Model representing an author."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, blank=True)
    # Other fields as needed

    def __str__(self):
        """String for representing the Model object."""
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey(b_post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username if self.user else 'Anonymous'} on {self.post.title}"


class ContentBlock(models.Model):
    post = models.ForeignKey(b_post, on_delete=models.CASCADE, related_name='content_blocks')
    ORDER_CHOICES = (
        ('paragraph', 'Paragraph'),
        ('image', 'Image'),
    )
    order_type = models.CharField(max_length=10, choices=ORDER_CHOICES)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True)
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Enter the order in which the block should appear")

    def __str__(self):
        return f"Content block for {self.post.title}"
