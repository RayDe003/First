from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import UserProfile, Question, Choice


class SignUpForm(UserCreationForm):
    bio = forms.CharField(max_length=500, required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
            bio = self.cleaned_data.get('bio', '')
            avatar = self.cleaned_data.get('avatar', None)

            UserProfile.objects.create(
                user=user,
                bio=bio,
                avatar=avatar,
                username=user.username,
            )
        return user

class SignInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar', 'username']

class QuestionForm(forms.ModelForm):
    choice_texts = forms.CharField(label='Choice Texts', help_text='Enter choices separated by commas')

    class Meta:
        model = Question
        fields = ['question_text', 'short_description', 'full_description', 'image', 'pub_date', 'expiry_date'
        ]

    def save(self, commit=True):
        question = super().save(commit=False)
        question.save()

        choice_texts = [choice.strip() for choice in self.cleaned_data['choice_texts'].split(',')]

        for choice_text in choice_texts:
            Choice.objects.create(question=question, choice_text=choice_text)

        return question