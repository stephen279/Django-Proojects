from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Avg


DONT_UNDERSTAND_DESCRIPTION_CHOICES = (
    ('badly_explained','Badly Explained'),
    ('too_difficult', 'Too Difficult'),
    ('bad_material','Bad Material'),

)



class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField(blank=True, default='')


    def __str__(self):
        return self.title


#have text based steps , video based steps quizzes steps s make abstract
class Step(models.Model):
    title = models.CharField(max_length=255)


    description = models.CharField(max_length=26, choices=DONT_UNDERSTAND_DESCRIPTION_CHOICES)

    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course)
    version = models.IntegerField()


    class Meta:
        abstract = True
        ordering = ['order',]

    def __str__(self):
        return self.title


class Text(Step):
    content = models.TextField(blank=True, default='')

    #return a url String
    def get_absolute_url(self):
        return reverse('courses:text', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.id
        })


class Quiz(Step):
    rating = models.IntegerField(default='10')
   # color = models.CharField(max_length=6, choices=COLOR_CHOICES,
    #                         default='green')


    class Meta:
        verbose_name_plural = "Quizzes"

        # return a url String

    def get_absolute_url(self):
        return reverse('courses:quiz', kwargs={
            'course_pk': self.course_id,
            'step_pk': self.id
        })


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    order = models.IntegerField(default=0)
    prompt = models.TextField()

    class Meta:
        ordering = ['order']

    #good for 'VIEW ON SITE'
    def get_absolute_url(self):
        return self.quiz.get_absolute_url()

    #add for use in shell handy and good practice
    def __str__(self):
        return self.prompt


    #what about difffernet types of Question types
class MultipleChoiceQuestions(Question):
    shuffle_answers = models.BooleanField(default=False)

class TrueFalseQuestion(Question):
    pass

class Answer(models.Model):
    quiz = models.ForeignKey(Quiz)
    order = models.IntegerField(default=0)
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text



