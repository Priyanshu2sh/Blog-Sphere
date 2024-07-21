from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
import random

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
    
class Post(models.Model):
    
    CATEGORY = (
        ('Business','Business'),
        ('Technology','Technology'),
        ('Entertainment','Entertainment'),
        ('Sports','Sports')
    )

    SECTION = (
        ('Featured','Featured'),
        ('Popular','Popular'),
        ('Latest','Latest'),
        ('Trending','Trending')
    )

    featured_image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(choices=CATEGORY, max_length=200)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)
    section = models.CharField(choices=SECTION, max_length=200)

    def save(self, *args, **kwargs):
        if not self.section:
            self.section = random.choice(self.SECTION)[0]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Post)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.name} on {self.post.title}"