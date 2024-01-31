from django.urls import path
from headhunter_app.views import *
urlpatterns = [
    path('',StartPageView.as_view(), name='start_page'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('sign_up/',SignUpView.as_view(), name='sign_up'),
    path('list/', list_view, name='list'),
    path('detail/<int:pk>/', detail_view, name='detail'),
    path('create_vacancy/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('create_resume/',ResumeCreateView.as_view(), name='resume_create'),
    path('vacancy_update/<int:pk>/',VacancyUpdateView.as_view(), name='vacancy_update'),
    path('resume_update/<int:pk>/',ResumeUpdateView.as_view(), name='resume_update'),
    path('vacancy_delete/<int:pk>/',VacancyDeleteView.as_view(), name='vacancy_delete'),
    path('resume_delete/<int:pk>/',ResumeDeleteView.as_view(), name='resume_delete'),
]
