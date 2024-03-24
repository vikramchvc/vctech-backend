from django.contrib import admin
from django.urls import path, include
from accounts.views import GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('quicksense/', include('quicksense.urls')),
]
