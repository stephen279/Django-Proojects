from django.contrib import admin

from . import models






admin.site.register(models.Course)
admin.site.register(models.Text)  # not a table class anymore
admin.site.register(models.Quiz)  # not a table class anymore
admin.site.register(models.Answer)
admin.site.register(models.Question)
admin.site.register(models.MultipleChoiceQuestions)
admin.site.register(models.TrueFalseQuestion)