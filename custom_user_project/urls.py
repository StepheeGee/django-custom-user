# custom_user_project/urls.py
from django.contrib import admin
from django.urls import path, include

from custom_user.views import CustomHomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomHomeView.as_view(), name='home'),
    path('accounts/', include('custom_user.urls')),
]
