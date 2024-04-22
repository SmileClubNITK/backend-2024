from django.db import models
from django.urls import reverse
import uuid  # Required for unique post instances
from django.contrib.auth.models import User  # Import the User model
from cloudinary.models import CloudinaryField

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Author(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    # Other fields as needed
    image = CloudinaryField('image')
    # image = models.ImageField(upload_to='author_images/', blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name
class b_post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    cover_image = CloudinaryField('image')
    abstract = models.CharField(max_length=200, null=True)
    authors = models.ManyToManyField(Author, related_name='posts',blank = True)    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = models.ManyToManyField(Tag, blank = True)  # Many-to-many relation with Tag model
        
    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this post."""
        return reverse('post-detail', args=[str(self.id)])




# class Comment(models.Model):
#     post = models.ForeignKey(b_post, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
#     content = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Comment by {self.user.username if self.user else 'Anonymous'} on {self.post.title}"


class ContentBlock(models.Model):
    post = models.ForeignKey(b_post, on_delete=models.CASCADE, related_name='content_blocks')
    ORDER_CHOICES = (
        ('paragraph', 'Paragraph'),
        ('image', 'Image'),
    )
    order_type = models.CharField(max_length=10, choices=ORDER_CHOICES)
    text = models.TextField(blank=True)
    image = CloudinaryField('image')
    caption = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Enter the order in which the block should appear")

    def __str__(self):
        return f"Content block for {self.post.title}"


class Team(models.Model):
    """Model representing an author."""
    name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    # Other fields as needed
    CATEGORY = (
        ('core', 'core'),
        ('member', 'member'),
        ('cordinators', 'codinators')
        
    )
    post = models.CharField(max_length=50, blank=True)
    image = CloudinaryField('image')
    category = models.CharField(max_length=50, choices=CATEGORY)
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Event(models.Model):
    """Model representing an event."""
    name = models.CharField(max_length=70, blank=True)
    about = models.TextField(max_length=1000, blank=True)
    event_date = models.DateTimeField()
    event_time = models.TimeField(blank=True, null=True)
    image = CloudinaryField('image')
    lunar_date = models.CharField(max_length=70, blank=True, null=True)
    tagline = models.CharField(max_length=150, blank=True, null=True)
    venue = models.CharField(max_length=70, blank=True, null=True)
    contact_email = models.EmailField(max_length=150, blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    form_link =  models.URLField(null=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
class Achievements(models.Model):
    """Model representing an event."""
    name = models.CharField(max_length=70, blank=True)
    about = models.TextField(max_length=1000, blank=True)
    image = CloudinaryField('image')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Quote(models.Model):
        quote = models.TextField(max_length=10000, blank=False)
        
class Yvideos(models.Model):
    
    title = models.CharField(max_length=50, blank=True, null=True)
    
    link = models.URLField()

class ImgGrp (models.Model):
    title = models.CharField(max_length=100)
    cover_image = CloudinaryField('image',null=True)


    def __str__(self):
        return self.title

class Image(models.Model):
    heading = models.ForeignKey(ImgGrp, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    alt = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return  self.alt