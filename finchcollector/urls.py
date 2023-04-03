"""finchcollector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.urls import path
from .views import about_view, snowboard_index, snowboard_detail

urlpatterns = [
    path('', snowboard_index, name='snowboard_index'),
    path('about/', about_view, name='about'),
    path('snowboards/', snowboard_index, name='all_snowboards'),
    path('snowboards/<int:pk>/', snowboard_detail, name='snowboard_detail'),
    path('create/', SnowboardCreateView.as_view(), name='snowboard_create'),
    path('<int:pk>/update/', SnowboardUpdateView.as_view(), name='snowboard_update'),
    path('<int:pk>/delete/', SnowboardDeleteView.as_view(), name='snowboard_delete'),
]
