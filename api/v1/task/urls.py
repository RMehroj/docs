from django.urls import path
from . import views

urlpatterns = [
    path(
        'login/',
        views.UserLoginView.as_view(),
    ),
    path(
        'register/',
        views.UserRegistrationView.as_view(),
    ),
    path(
        'files/',
        views.FileListView.as_view(),
    ),
    path(
        'files/delete/<int:pk>/',
        views.FileUpdateDeleteView.as_view(),
    ),
    path(
        'files/<int:pk>/share/',
        views.FileShareView.as_view(),
    ),
    path(
        'files/group/',
        views.FileGroupView.as_view()
    ),
]