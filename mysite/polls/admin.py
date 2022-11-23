from django.contrib import admin

from .models import Question,Choice
# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.site_header="postler Admin"
admin.site.site_title="postler Admin page"
admin.site.index_title="Welcome to postler"

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['question_text']}),
    ('Date Information',{'fields':['pub_date'],
    'classes':['collapse']}),]
    inlines= [ChoiceInline]

admin.site.register(Question,QuestionAdmin)