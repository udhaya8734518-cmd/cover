from django.contrib import admin
from django.urls import path
from coverapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.coverapp),
]