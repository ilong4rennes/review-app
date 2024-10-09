from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_index, name='user_index'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('businesses/', views.business_index, name='business_index'),
    path('businesses/<int:business_id>/', views.business_detail, name='business_detail'),
]

urlpatterns += [
    path('businesses/<int:business_id>/reviews/', views.review_list, name='review_list'),
    path('businesses/<int:business_id>/reviews/new/', views.review_create, name='review_create'),
]
