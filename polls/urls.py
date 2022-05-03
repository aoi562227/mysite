from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', view.detail, name='detail'),
    path('<int:question_id>/results/', view.results, name='results'),
    path('<int:question_id/vote/', view.vote, name='vote'),
]
