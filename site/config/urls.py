"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .views import main_page  # ← 방금 만든 view
from django.urls import path
from prompt_engine.views import generate_virtual_patient

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', main_page, name='main'),  # ← 루트 주소로 연결
    path("api/generate/", generate_virtual_patient),
]
