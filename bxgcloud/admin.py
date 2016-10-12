from django.contrib import admin

from .models import *
# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'member_id',
        'name',
        'sex',
        'birth',
        'phone_number',
        'email',
        'wxunionid',
        'bonus_point',
        'living_city',
        'profession',
        'summary',
        'web',
        'picture',
        'register_time')


class ClassifyAdmin(admin.ModelAdmin):
    list_display = ('classify_id', 'classify_name')


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'blog_id',
        'author',
        'title',
        'content',
        'label',
        'create_time')


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('column_id', 'column_author', 'column_name')


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question_id',
        'question_author',
        'question_title',
        'question_classify',
        'description',
        'create_time',
        'solve_status')


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'answer_id',
        'answer_author',
        'content',
        'question_answer',
        'create_time',
        'adopt_status')


class FollowAdmin(admin.ModelAdmin):
    list_display = ('follower', 'be_follower', 'follow_time')


class FollowQuestionAdmin(admin.ModelAdmin):
    list_display = ('question_follower', 'question_id', 'follow_time')


class AnswerScoreAdmin(admin.ModelAdmin):
    list_display = (
        'score_person',
        'score_answer',
        'score_points',
        'score_time')

admin.site.register(Member, MemberAdmin)
admin.site.register(Classify, ClassifyAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Column, ColumnAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(FollowQuestion, FollowQuestionAdmin)
admin.site.register(AnswerScore, AnswerScoreAdmin)
