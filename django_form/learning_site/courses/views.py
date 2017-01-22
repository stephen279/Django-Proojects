from itertools import chain
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from . import forms
from . import models

from django.views.generic import TemplateView
from django.contrib.auth.models import User


def course_list(request):
    courses = models.Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)

    #get all steps that relate to coarse  use chain and sorted
    steps = sorted(chain(course.text_set.all(), course.quiz_set.all()),
                        key=lambda step: step.order)  #order by step
    return render(request, 'courses/course_detail.html', {
        'course': course,   #send out course
        'steps' : steps
    })


def text_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Text, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})


def quiz_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Quiz, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/quiz_detail.html', {'step': step})


@login_required
def quiz_create(request, course_pk):
    course = get_object_or_404(models.Course, pk=course_pk)
    form = forms.QuizForm()

    if request.method == 'POST':
        form = forms.QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.course = course
            quiz.save()
            messages.add_message(request, messages.SUCCESS,
                                 "Quiz added!")
            return HttpResponseRedirect(quiz.get_absolute_url())
    return render(request, 'courses/quiz_form.html', {'form': form, 'course': course})


@login_required
def quiz_edit(request, course_pk, quiz_pk):
    quiz = get_object_or_404(models.Quiz, pk=quiz_pk)
    form = forms.QuizForm(instance=quiz)# where starting from
    if request.method == 'POST':
        form = forms.QuizForm(instance=quiz, data=request.POST )
        if form.is_valid():
            # save back over with new data
            form.save()
            messages.success(request, "Updated {} ".format(form.cleaned_data['title']))
            return HttpResponseRedirect(quiz.get_absolute_url())


    return render(request, 'courses/quiz_form.html',{'form':form, 'course': quiz.course})





