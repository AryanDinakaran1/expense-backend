# MODULE IMPORTS
import hashlib
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

# FILE IMPORTS
from . import models
from . import serializers

# GET ALL USERS
@api_view(['GET'])
def get_users(request):
    users = models.User.objects.all()
    usersSer = serializers.UserSerializer(users, many=True)

    return Response(usersSer.data)

# GET A SPECEFUC USER BY ID
@api_view(['GET'])
def get_user(request, user_id):
    user = models.User.objects.get(pk=user_id)
    userSer = serializers.UserSerializer(user, many=False)

    return Response(userSer.data)

# CREATE NEW USER
@api_view(['POST'])
def create_user(request):
    passwd = request.data['password']
    request.data['password'] = hashlib.sha256(passwd.encode()).hexdigest()
    UserSer = serializers.UserSerializer(data=request.data)

    if UserSer.is_valid():
        user = UserSer.save()

        return Response(serializers.UserSerializer(user).data, status=status.HTTP_201_CREATED)

    return Response(UserSer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET ALL EXPENSES
@api_view(['GET'])
def get_expenses(request):
    expenses = models.Expense.objects.all()
    expensesSer = serializers.ExpenseSerializer(expenses, many=True)

    return Response(expensesSer.data)

# GET SPECEFIC EXPENSE BY ID
@api_view(['GET'])
def get_expense(request, expense_id):
    expense = models.Expense.objects.get(pk=expense_id)
    expenseSer = serializers.ExpenseSerializer(expense, many=True)

    return Response(expenseSer.data)

# CREATE NEW EXPENSE
@api_view(['POST'])
def create_expense(request, user_id, split_type):

    request.data['user'] = user_id
    ExpenseSer = serializers.ExpenseSerializer(data=request.data)
    
    if ExpenseSer.is_valid():
        expense = ExpenseSer.save()
        return Response(serializers.ExpenseSerializer(expense).data, status=status.HTTP_201_CREATED)
    
    return Response(ExpenseSer.errors, status=status.HTTP_400_BAD_REQUEST)