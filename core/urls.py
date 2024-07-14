from django.urls import path
from .views import home, download, show_available_download


urlpatterns=[
    path('home/', home, name="home"),
    path('available-downloads/', show_available_download, name="show_available_download"),
    path('download/', download, name="download"),
]
