from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Member(models.Model):
    '''
    the model about Member
    '''
    SEX_TYPE = (
        (1, 'boy'),
        (2, 'girl'),
    )
    member_id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    sex = models.SmallIntegerField(default=1, choices=SEX_TYPE)
    birth = models.DateField()
    phone_number = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    wxunionid = models.CharField(max_length=128, blank=True, null=True)
    bonus_point = models.SmallIntegerField(blank=True, null=True)
    living_city = models.CharField(max_length=1024, blank=True, null=True)
    profession = models.CharField(max_length=256, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    web = models.URLField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    register_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = "Member"
        ordering = ['name', 'birth', 'bonus_point', 'register_time']
        unique_together = ('name', 'email', 'phone_number', 'wxunionid')

    def __unicode__(self):
        return self.name


class Classify(models.Model):
    '''
    the model about classify
    '''
    BLOG_TYPE = (
        (1, 'Python'),
        (2, 'Java'),
        (3, 'C'),
        (4, 'C++'),
        (5, 'Ruby'),
        (6, 'PHP'),
        (7, 'Javascript'),
        (8, 'Mysql'),
        (9, 'PostgreSQL'),
    )
    classify_id = models.SmallIntegerField(primary_key=True)
    classify_name = models.SmallIntegerField(default=1, choices=BLOG_TYPE)

    class Meta:
        managed = True
        db_table = 'Classify'

    def __unicode__(self):
        return str(self.classify_name)


class Blog(models.Model):
    '''
    the model about Blog
    '''
    blog_id = models.SmallIntegerField(primary_key=True)
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    content = models.TextField()
    classification = models.ForeignKey(Classify)
    label = models.CharField(max_length=128, blank=True, null=True)
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'Blog'
        ordering = ['author', 'title', 'label', 'create_time']
        unique_together = ('author', 'title')

    def __uncode__(self):
        return unicode(self.author) + '.' + unicode(self.title)


class Column(models.Model):
    '''
    the model about Column
    '''
    column_id = models.SmallIntegerField(primary_key=True)
    column_author = models.ForeignKey(Member)
    column_name = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'Column'
        ordering = ['column_author', 'column_name']
        unique_together = ('column_author', 'column_name')


class Question(models.Model):
    '''
    the model about Question
    '''
    SOLVE_STATUE = (
        (1, 'resolved'),
        (2, 'not resolved'),
    )
    question_id = models.SmallIntegerField(primary_key=True)
    question_author = models.ForeignKey(Member, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=128)
    question_classify = models.ForeignKey(Classify, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(auto_now=True)
    solve_status = models.SmallIntegerField(default=1, choices=SOLVE_STATUE)

    class Meta:
        managed = True
        db_table = 'Question'
        ordering = [
            'question_title',
            'create_time',
            'solve_status',
            'question_classify']
        unique_together = ('question_title', 'question_author', 'create_time')

    def __unicode__(self):
        return str(self.question_id)


class Answer(models.Model):
    '''
    the model about Answer
    '''
    ADOPT_STATUS = (
        (1, 'adopted'),
        (2, 'not adopted'),
    )
    answer_id = models.SmallIntegerField(primary_key=True)
    answer_author = models.ForeignKey(Member, on_delete=models.CASCADE)
    content = models.TextField()
    question_answer = models.ForeignKey(Question, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now=True)
    adopt_status = models.SmallIntegerField(default=1, choices=ADOPT_STATUS)

    class Meta:
        managed = True
        db_table = 'Answer'
        ordering = ['answer_author', 'create_time', 'adopt_status']

    def __unicode__(self):
        return str(self.answer_id)


class Follow(models.Model):
    '''
    the model about Follow
    '''
    follower = models.ForeignKey(
        Member,
        related_name='follower',
        on_delete=models.CASCADE)
    be_follower = models.ForeignKey(
        Member,
        related_name='be_follower',
        on_delete=models.CASCADE)
    follow_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'Follow'
        ordering = ['follower', 'be_follower', 'follow_time']


class FollowQuestion(models.Model):
    '''
    the model about follow_question
    '''
    question_follower = models.ForeignKey(Member, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    follow_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'FollowQuestion'
        ordering = ['question_follower', 'follow_time']
        unique_together = ('question_follower', 'question_id')


class AnswerScore(models.Model):
    '''
    the model about Answer_Score
    '''
    score_person = models.ForeignKey(Member, on_delete=models.CASCADE)
    score_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    score_points = models.CharField(max_length=128)
    score_time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'AnswerScore'
        unique_together = ('score_person', 'score_answer')
