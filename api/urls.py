from django.urls import path
from . import views

urlpatterns = [
    path('get-users/', views.get_users, name='get_users'),
    path('get-user/<int:user_id>/', views.get_user, name='get_user'),
    path('create-user/', views.create_user, name='create_user'),

    path('get-expenses/', views.get_expenses, name='get_expenses'),
    path('get-expense/<int:expense_id>/', views.get_expense, name='get_expense'),
    path('create-expense/user/<int:user_id>/split-type/<str:split_type>/', views.create_expense, name='create_expense'),
]