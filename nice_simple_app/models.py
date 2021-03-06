from django.db import models
from django.utils import timezone
# from nice_simple_app_site.settings import AUTH_USER_MODEL

# an object containing all the scraped data of a user's Facebook profile

class Profile(models.Model):

    owner = models.ForeignKey('auth.User', related_name='nice_simple_app')
    collected_date = models.DateTimeField(default=timezone.now)
    public_view = models.BooleanField(default=True)
    img_url = models.URLField()

    p_name = models.TextField(default='')
    p_phone = models.CharField(default='', max_length=10)
    p_city = models.CharField(default='', max_length=50)
    p_region = models.CharField(default='', max_length=50)
    p_country = models.CharField(default='', max_length=50)
    p_birthday = models.CharField(default='', max_length=50)
    p_birthyear = models.CharField(default='', max_length=4)
    p_relationship = models.CharField(default='', max_length=50)
    p_relationship_with = models.CharField(default='', max_length=50)
    p_job_title = models.CharField(default='', max_length=50)
    p_job_employer = models.CharField(default='', max_length=50)
    p_studying = models.CharField(default='', max_length=50)
    p_school = models.CharField(default='', max_length=50)
    p_friends = models.IntegerField(default=0)
    p_likes = models.IntegerField(default=0)
    p_groups = models.IntegerField(default=0)
    p_information = models.TextField(default='')
    p_quotes = models.TextField(default='')
    p_nickname = models.CharField(default='', max_length=50)

    def publish(self):
        self.collected_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)


# A viewable object that displays the results of one or two profiles

class Comparison(models.Model):

    profile_url = models.URLField()
    collected_date = models.DateTimeField(default=timezone.now)
    collected_by = models.ForeignKey('auth.User')
    l_profile = models.ForeignKey(Profile, null=True, related_name='l_profile')
    r_profile = models.ForeignKey(Profile, null=True, related_name='r_profile')

    def publish(self):
        self.collected_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.pk)
