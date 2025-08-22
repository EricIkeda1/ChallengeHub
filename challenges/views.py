from django.shortcuts import render, get_object_or_404
from .models import Challenge
from .forms import SubmissionForm

def home(request):
    return render(request, 'challenges/home.html')

def challenges_list(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/challenges_list.html', {'challenges': challenges})

def challenge_detail(request, pk):
    challenge = get_object_or_404(Challenge, pk=pk)
    submitted = False
    correct = False

    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.challenge = challenge
            submission.correct = submission.code.strip() == challenge.solution_code.strip()
            submission.save()
            submitted = True
            correct = submission.correct
    else:
        form = SubmissionForm()

    return render(request, 'challenges/challenge_detail.html', {
        'challenge': challenge,
        'form': form,
        'submitted': submitted,
        'correct': correct
    })
