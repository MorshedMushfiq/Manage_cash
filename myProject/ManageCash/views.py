from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import AddCash, Expense


def register(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
    
        
        if password==Confirm_password:
            
            
            user=User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            
            return redirect("loginPage")
            
    return render(request,"register.html")


def loginPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, email=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('loginPage')

        except User.DoesNotExist:
            return redirect('register')

    return render(request, 'login.html')

@login_required
def homePage(request):
    totalCash = AddCash.objects.aggregate(total_cash=Sum('amount'))['total_cash'] or 0
    totalExpense = Expense.objects.aggregate(total_expense=Sum('amount'))['total_expense'] or 0
    
    balance = totalCash - totalExpense
    
    return render(request,"homePage.html", {'totalCash':totalCash, 'totalExpense':totalExpense, "balance":balance })


def logoutPage(request):
    
    logout(request)
    
    return redirect('loginPage')

@login_required
def profilePage(request):
    totalCash = AddCash.objects.aggregate(total_cash=Sum('amount'))['total_cash'] or 0
    totalExpense = Expense.objects.aggregate(total_expense=Sum('amount'))['total_expense'] or 0
    
    balance = totalCash - totalExpense
    
    return render(request,"profilePage.html", {'totalCash':totalCash, 'totalExpense':totalExpense, "balance":balance })


@login_required
def editProfile(request):

    if request.method=='POST':
        
        current_user = request.user
        
        current_user.username=request.POST.get("username")
        current_user.email=request.POST.get("email")
        current_user.save()
        return redirect("profilePage")
    
    return render(request,"editProfile.html")


def addCash(req):
    if req.method == "POST":
        user = req.user
        source = req.POST.get("source")
        amount = req.POST.get("amount")
        description = req.POST.get("description")
        cash = AddCash(
            user=user,
            source=source,
            amount=amount,
            description=description
            
        )
        cash.save()
        return redirect('cashManagement')
    return render(req, "addCash.html")


def cashManagement(req):
    addCashData = AddCash.objects.filter(user=req.user)
    
    return render(req, 'cashManagement.html', {'addCashData': addCashData})


def cashDelete(req, id):
    deleteCash = AddCash.objects.get(id=id)
    deleteCash.delete()
    return redirect('cashManagement')


def cashEdit(req, id):
    editCash = AddCash.objects.get(id=id)
    
    if req.method == "POST":
        user = req.user
        cash_id = req.POST.get("cash_id")
        source = req.POST.get("source")
        amount = req.POST.get("amount")
        description = req.POST.get("description")
        cash = AddCash(
            user=user,
            id=cash_id,
            source=source,
            amount=amount,
            description=description
            
        )
        cash.save()
        return redirect('cashManagement')
    return render(req, "cashEdit.html", {'editCash': editCash})

def cashView(req, id):
    viewCash = AddCash.objects.get(id=id)
    return render(req, 'cashView.html', {'viewCash': viewCash})





def addExpense(req):
    if req.method == "POST":
        user = req.user
        amount = req.POST.get("amount")
        description = req.POST.get("description")
        expense = Expense(
            user=user,
            amount=amount,
            description=description
            
        )
        expense.save()
        return redirect('expenseManagement')
    return render(req, "addExpenses.html")


def expenseManagement(req):
    addexpenseData = Expense.objects.filter(user=req.user)
    
    return render(req, 'expensesList.html', {'addexpenseData': addexpenseData})


def expenseDelete(req, id):
    deleteExpense = Expense.objects.get(id=id)
    deleteExpense.delete()
    return redirect('expenseManagement')


def expenseEdit(req, id):
    editExpense = Expense.objects.get(id=id)
    
    if req.method == "POST":
        user = req.user
        expense_id = req.POST.get("expense_id")
        amount = req.POST.get("amount")
        description = req.POST.get("description")
        expense = Expense(
            user=user,
            id=expense_id,
            amount=amount,
            description=description
            
        )
        expense.save()
        return redirect('expenseManagement')
    return render(req, "expenseEdit.html", {'editExpense': editExpense})

def expenseView(req, id):
    viewExpense = Expense.objects.get(id=id)
    return render(req, 'expenseView.html', {'viewExpense': viewExpense})











