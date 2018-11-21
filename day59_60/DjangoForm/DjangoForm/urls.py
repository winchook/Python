"""DjangoForm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from app01 import views
from app02 import views as v2
from app03 import views as v3


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users', views.users),
    url(r'^add_user', views.add_user),
    url(r'^edit_user-(\d+)$', views.edit_user),
    url(r'^test', v2.test),
    url(r'^skill', v2.skill),
    url(r'^ajax', v2.ajax),
    url(r'^serialization', v3.serialization),
    url(r'^get_data', v3.get_data),
]
