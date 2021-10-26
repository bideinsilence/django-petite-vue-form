from django.urls import path

from . import views

app_name = "test-form"
urlpatterns = [
    path("", views.test_petite_vue, name="test-form"),
]
