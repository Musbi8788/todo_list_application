from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create")
    
]

urlpatterns += staticfiles_urlpatterns()
