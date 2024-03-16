from django.db import models
from django.urls import reverse
import uuid # Required for unique book instances

# Create your models here.

class b_post(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)  
    title = models.CharField(max_length=200)
    author= models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    content = models.TextField(max_length=50000, help_text="Enter a brief description of the book")

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = models.CharField(max_length=255, blank=True)  # Optional comma-separated tags
    thumbnail = models.ImageField(upload_to='blog_thumbnail/')
    thumbnail_caption = models.CharField(
        max_length=100, default='')
    img = models.ImageField(upload_to='blog_images/', blank=True)  # Optional image
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])




class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

from django.contrib.auth.models import User  # Import the User model

class Comment(models.Model):
    post = models.ForeignKey(b_post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username if self.user else 'Anonymous'} on {self.post.title}"
