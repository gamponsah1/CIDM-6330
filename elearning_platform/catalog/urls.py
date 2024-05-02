from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

]
urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.course_list, name='course-list'),
    path('instructors/', views.instructor_list, name='instructor-list'),
    path('courses/<int:course_id>/purchase/', views.purchase_course, name='purchase'),
    path('purchase-confirmation/', views.purchase_confirmation, name='purchase_confirmation'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # URL for login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # URL for logout page
    path('signup/', views.signup, name='signup'),  # URL for user registration page
]
