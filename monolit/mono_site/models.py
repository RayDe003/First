from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    username = models.CharField(max_length=100, default='qqq')

    def __str__(self):
        return self.user.username

    def get_user_questions(self):
        return self.user_profile.question_set.all() if hasattr(self, 'user_profile') else []


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    full_description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='poll_images/', blank=True, null=True)
    pub_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions', null=True, default=None)

    def get_created_by(self):
        return self.created_by.username if self.created_by else None

    def is_active(self):
        return self.expiry_date is None or self.expiry_date > timezone.now()

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    voters = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.choice_text