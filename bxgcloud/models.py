from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Member(models.Model):
    SEX_TYPE = (
        (1,'boy'),
        (2,'girl'),
    )
    mid = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    sex = models.SmallIntegerField(default=1,choices=SEX_TYPE)
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
        return self.mid + '.' +self.name