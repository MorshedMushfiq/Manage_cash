
from django.urls import path
from .views import *

urlpatterns = [
    path('',loginPage,name="loginPage"),
    path("register/", register, name="register"),
    path("homePage/", homePage, name="homePage"),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("ProfilePage/", profilePage, name="profilePage"),
    path("editProfile/", editProfile, name="editProfile"),
    path("add_cash/", addCash, name="addCash"),
    path("cash_management/", cashManagement, name="cashManagement"),
    path("cashDelete/<int:id>", cashDelete, name="cashDelete"),
    path("cash_edit/<int:id>", cashEdit, name="cashEdit"),
    path("cash_view/<int:id>", cashView, name="cashView"),
    path("add_expense/", addExpense, name="addExpense"),
    path("expense_management/", expenseManagement, name="expenseManagement"),
    path("expenseDelete/<int:id>", expenseDelete, name="expenseDelete"),
    path("expense_edit/<int:id>", expenseEdit, name="expenseEdit"),
    path("expense_view/<int:id>", expenseView, name="expenseView"),
    
]
