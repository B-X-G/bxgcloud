from rest_framework import serializers
from models import *


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = (
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
