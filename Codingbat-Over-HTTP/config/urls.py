"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
import app.views

urlpatterns = [
    path("", app.views.root, name="root"),
    path("warmup-2", app.views.Warmup_2, name="Warmup2"),
    path("logic-2", app.views.Logic_2, name="Logic2"),
    path("string-2", app.views.String_2, name="String2"),
    path("list-2", app.views.List_2, name="List2"),
    path("admin/", admin.site.urls),
]
