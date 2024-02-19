from django.urls import path

from . import views

app_name = "analyze_texts_dashboard"

urlpatterns = [
    path("", views.index, name="index")
]