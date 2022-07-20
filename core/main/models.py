from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='category')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['id']


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='post', related_name='posts')
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=13, decimal_places=2)
    img = models.ImageField()
    status = models.CharField(max_length=100, blank=True, choices=(('Owner', 'Owner'),
                                                                   ('Organization', 'Organization')))
    type = models.CharField(max_length=100, blank=True, choices=(('For sale', 'For sale'),
                                                                 ('Giveaway', 'Giveaway'),
                                                                 ('Wanted', 'Wanted'),
                                                                 ('Exchange', 'Exchange')))
    location = models.CharField(max_length=100, blank=True, choices=(('Yerevan', 'Yerevan'),
                                                                     ('Lori', 'Lori'),
                                                                     ('Tavush', 'Tavush'),
                                                                     ('Armavir', 'Armavir')))
    condition = models.CharField(max_length=100, blank=True, choices=(('New', 'New'),
                                                                      ('Used', 'Used')))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-time_create']
