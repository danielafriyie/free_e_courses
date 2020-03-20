from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/<str:name>/', views.course_detail, name='course_detail'),
    path('search/', views.search_course, name='search'),
    path('category/', views.category_filter, name='category'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms_condition, name='terms_condition'),
    path('privacy/', views.privacy, name='privacy')
]
