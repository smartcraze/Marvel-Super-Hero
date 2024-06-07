from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('suraj/', views.suraj, name='suraj'),
    path('marvel/', include('Marvel.urls')),
    path("__reload__/", include("django_browser_reload.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
