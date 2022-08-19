from django.urls import path
from . import views

app_name="pollos"

urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("<int:pk>",views.DetailView.as_view(),name="detail"),
    path("<int:pk>/results",views.ResultView.as_view(),name="results"),
    path("<int:question_idis>/votes",views.votes,name="votes")
]





