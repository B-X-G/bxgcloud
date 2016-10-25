from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    # add the url for rest api
    # for example:
    url(r'^$', views.homepage),
    url(r'^api/member$', views.MemberList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
