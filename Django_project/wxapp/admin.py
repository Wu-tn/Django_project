from django.contrib import admin

from .models import Question,Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#classes:collapse定义可折叠
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
    ]
    list_display = ('question_text','pub_date','was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
