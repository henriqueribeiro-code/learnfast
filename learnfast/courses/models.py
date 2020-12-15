from django.db import models
from django.urls import reverse


# Create your models here.

class CoursesManager(models.Manager):
    def search(self, query):
        return self.get_queryset().filter(models.Q(name__icontains=query) or models.Q(description__icontains=query))


class Courses(models.Model):

    name = models.CharField(verbose_name="Name of Courses", max_length=150)
    slug = models.SlugField(verbose_name="Shortcut")
    description = models.TextField(verbose_name="Description of Courses", blank=True)
    about_course = models.TextField(verbose_name='About Course', blank=True)
    start_date = models.DateField(verbose_name="Date of Begin", null=True, blank=True)
    imagem_course = models.ImageField(upload_to="courses/images", verbose_name="Images of Courses", null=True, blank=True)
    create_at = models.DateTimeField(verbose_name="Create at", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="Update at",auto_now=True)

    class Meta:
        __tablename__ = 'Courses'
        verbose_name_plural ='Courses'
        verbose_name = 'Course'
        ordering = ['name']
    
    def __str__(self):
        return self.name
   
    def get_absolute_url(self):
        return reverse('course', kwargs={'slug': self.slug})
    
   

objects = CoursesManager()
