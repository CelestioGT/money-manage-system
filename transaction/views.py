#from moneymanagement.transaction.models import record
import datetime

from django.db.models import Sum
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import record
from .forms import recordForm

# Create your views here.
def Home(request):
    if request.POST:
        form = recordForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)



    form = recordForm()
    data = record.objects.all().order_by('-date')
    NumberOfTransaction = data.count()

    today = datetime.date.today()
    dataMonth = record.objects.filter(date__year=today.year,
                           date__month=today.month)
    
    balance = data.aggregate(Sum('amount'))
    DepositePerMonth = 0
    WithdrawPerMonth = 0
    # NumberOfTransaction = 0
    for resultsMonth in dataMonth:
        if resultsMonth.type == "deposite":
            DepositePerMonth += resultsMonth.amount
        if resultsMonth.type == "withdraw":
            WithdrawPerMonth -= resultsMonth.amount
    # for results in data:
    #     # NumberOfTransaction += 1
    #     if results.type == "deposite":
    #         balance += results.amount
    #     if results.type == "withdraw":
    #         balance -= results.amount
    #     if results.type == "transfer":
    #         balance -= results.amount
    context = {'records':data,
                'balance':balance,
                'DepositePerMonth':DepositePerMonth,
                'WithdrawPerMonth':WithdrawPerMonth,
                'NumberOfTransaction':NumberOfTransaction,
                'form':form
              }
    return render(request,'index.html',context)

def CreateTransaction(request):
    records = record() 
    records.title = request.POST.get('name')
    # amount=request.post['amount']
    # descript=request.post['descript']
    # type=request.post['type']
    records.save()
    return render(request,'index.html')

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
        context = {'form':form}
        return render(request,'edit.html',context)







    

