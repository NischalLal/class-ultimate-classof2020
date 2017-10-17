from django.db import models

# Create your models here.

class Member(models.Model):
    full_name = models.CharField("Full Name", max_length = 150)
    image = models.ImageField(upload_to = 'members')
    phone_number = models.CharField('Phone Number', max_length = 10)
    email = models.CharField('Email', max_length = 150)
    hometown = models.CharField("Your HomeTown", max_length = 200)
    favourite_quote = models.CharField(max_length = 100, blank = True)
    bio = models.TextField()
    your_website = models.URLField(blank = True, null = True, default = 'https://pythonair.me')
    facebook_url = models.CharField('Facebook URL', max_length = 100,
                     blank = True)
    twitter_url = models.CharField('Twitter URL', max_length = 100,
                     blank = True)
    instagram_url = models.CharField('Instagram URL', max_length = 100,
     blank = True)
    github_url = models.CharField('Github URL', max_length = 100,
                     blank = True)
    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def __str__(self):
        return self.full_name