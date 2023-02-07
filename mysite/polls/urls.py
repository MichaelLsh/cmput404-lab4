# # from django.urls import path
# # from . import views

# # urlpatterns = [
# #   path('', views.index, name='index'),
# # ]

# from django.urls import path

# from . import views

# app_name = 'polls'
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('api/questions/', views.get_questions, name='get_questions'),
    path('api/question/<int:pk>', views.update_question, name='update_question'),
]