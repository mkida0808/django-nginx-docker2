from django.urls import path,include
from rest_framework import routers
from django.conf.urls import url
from app.views.testapiview import seinotest

router = routers.DefaultRouter()
router.register(r'seinotest', seinotest,'')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
