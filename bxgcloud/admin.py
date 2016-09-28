from django.contrib import admin

from .models import *
# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ('mid', 'name', 'sex', 'birth', 'phone_number', 'email', 'wxunionid', 'bonus_point', 'living_city', 'profession', 'summary', 'web', 'picture', 'register_time')

admin.site.register(Member,MemberAdmin)