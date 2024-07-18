from . import views
from django.urls import path
from .views import home, download, show_available_download, my_view


urlpatterns=[
    path('home/', home, name="home"),
    path('available-downloads/', show_available_download, name="show_available_download"),
    path('download/', download, name="download"),
    path('my-view/<str:param1>/<str:param2>/', views.my_view, name='my_view'),

]

