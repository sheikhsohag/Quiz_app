from django.contrib import admin
from .models import Question,solve_question,choice

# Register your models here.
admin.site.register(Question)
admin.site.register(solve_question)
admin.site.register(choice)
