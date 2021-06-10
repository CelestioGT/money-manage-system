#from moneymanagement.transaction.models import record
import datetime
import logging

from django.db.models import Sum
from django.shortcuts import redirect, render
from django.http import HttpResponse


from .models import record, AllTeam, MyTeam
from .forms import recordForm, CreateTeamForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def Team(request):
    if request.POST:
        form = CreateTeamForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)    
    return render(request,'team.html')

@login_required

def Home(request,slug):
    #Create Transaction
    if request.POST:
        form = recordForm(request.POST,request.FILES) #recordForm from forms.py in app
        print(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    form = recordForm()
    #data = record.objects.all().order_by('-date')
    data = record.objects.filter(slug=slug)
    # NumberOfTransaction = data.count()

    today = datetime.date.today()
    dataMonth = record.objects.filter(date__year=today.year,
                           date__month=today.month)
    
    #balance = data.aggregate(Sum('amount'))
    balance = 0
    DepositePerMonth = 0
    WithdrawPerMonth = 0
    NumberOfTransaction = 0
    for resultsMonth in dataMonth:
        if resultsMonth.type == "deposite":
            DepositePerMonth += resultsMonth.amount
        if resultsMonth.type == "withdraw":
            WithdrawPerMonth -= resultsMonth.amount
    for results in data:
        NumberOfTransaction += 1
        if results.type == "deposite":
            balance += results.amount
        if results.type == "withdraw":
            balance -= results.amount
        if results.type == "transfer":
            balance -= results.amount
    context = { 'records':data,
                'balance':balance,
                'DepositePerMonth':DepositePerMonth,
                'WithdrawPerMonth':WithdrawPerMonth,
                'NumberOfTransaction':NumberOfTransaction,
                'form':form
              }
    return render(request,'index.html',context)

# @login_required
# def CreateTransaction(request):
#     if request.method == 'POST':
#         form = record(request.POST, request.FILES)
#         if form.is_valid():
#             SaveTrans = form.save(commit=False)
#             logger.info('Create New Transaction Success')
#             return redirect('/')

def DeleteTransaction(request,pk):
    myTransaction = record.objects.get(id = pk)
    myTransaction.delete()
    return redirect('/')

def EditTransaction(request,pk):
    myTransaction = record.objects.get(id = pk)
    if request.POST:
        form = recordForm(request.POST,instance = myTransaction)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = recordForm(instance = myTransaction)
        data = record.objects.all().order_by('-date')
        NumberOfTransaction = data.count()

        today = datetime.date.today()
        dataMonth = record.objects.filter(date__year=today.year,
                            date__month=today.month)
        
        #balance = data.aggregate(Sum('amount'))
        balance = 0
        DepositePerMonth = 0
        WithdrawPerMonth = 0
        # NumberOfTransaction = 0
        for resultsMonth in dataMonth:
            if resultsMonth.type == "deposite":
                DepositePerMonth += resultsMonth.amount
            if resultsMonth.type == "withdraw":
                WithdrawPerMonth -= resultsMonth.amount
        for results in data:
            # NumberOfTransaction += 1
            if results.type == "deposite":
                balance += results.amount
            if results.type == "withdraw":
                balance -= results.amount
            if results.type == "transfer":
                balance -= results.amount
        context = { 'records':data,
                    'balance':balance,
                    'DepositePerMonth':DepositePerMonth,
                    'WithdrawPerMonth':WithdrawPerMonth,
                    'NumberOfTransaction':NumberOfTransaction,
                    'form':form
                }        
        return render(request,'edit.html',context)
    








    

