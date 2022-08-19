from django.urls import path
from . import views

app_name="pollos"

urlpatterns = [
    path("",views.index,name="index"),
    path("<int:question_idis>",views.detail,name="detail"),
    path("<int:question_idis>/results",views.results,name="results"),
    path("<int:question_idis>/votes",views.votes,name="votes")
]



