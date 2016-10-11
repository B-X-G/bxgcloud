from django.shortcuts import render
import traceback

# Django and REST modules
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# custom modules
from .models import *
from .serializers import *


def homepage(request):
    return render(request, 'index.html')


# Create your views here.
class MemberList(APIView):
    '''
    the Member List about all member infomations
    '''

    def get(self, request):
        '''
        display all member informations
        :param request: none
        :return: serializer.data
        '''
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response({'result': 'ok', 'data': serializer.data})

    def post(self, request):
        '''
        add the member for Member table
        :param request: request.data
        :return: result
        '''
        serializers = MemberSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        else:
            result = {'result': 'the author post failed',
                      'reason': 'the message is not valid'}
            return Response(result, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, requset):
        '''
        delete the member from Member table
        :param requset:
        :return:
        '''
        try:
            Member.objects.all().delete()
        except:
            traceback.print_exc()
            return Response(status.HTTP_403_FORBIDDEN)
