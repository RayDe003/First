from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout

from .forms import SignUpForm, SignInForm, UserProfileForm, QuestionForm
from .models import Question, Choice, UserProfile
from django.db.models import Sum


def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    all_questions = Question.objects.all()
    return render(request, 'profile.html', {'user_profile': user_profile, 'all_questions': all_questions})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = SignInForm()
    return render(request, 'registration/signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')

def custom_logout(request):
    logout(request)
    return redirect('profile_unauthenticated')

def profile_unauthenticated(request):
    return render(request, 'profile_unauthenticated.html')



@login_required
def edit_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'edit_profile.html', {'form': form})


@login_required
def delete_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        logout(request)
        user_profile.delete()

        return redirect('signup')

    return render(request, 'delete_profile.html')


@login_required
def create_poll(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)

        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            return redirect('poll_detail', pk=question.pk)
    else:
        form = QuestionForm()

    return render(request, 'polls/create_poll.html', {'form': form})

@login_required
def poll_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)

    if not question.is_active():
        raise Http404("This poll is not active.")

    total_votes = question.choices.aggregate(Sum('votes'))['votes__sum']

    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')

        if selected_choice_id:
            selected_choice = get_object_or_404(Choice, pk=selected_choice_id)

            if request.user not in selected_choice.voters.all():
                selected_choice.votes += 1
                selected_choice.voters.add(request.user)
                selected_choice.save()
                return redirect('poll_detail', pk=question.id)
            else:
                pass

        return redirect('poll_detail', pk=question.id)
    else:
        return render(request, 'polls/poll_detail.html', {'question': question, 'total_votes': total_votes})
