from django import http
from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')

def calculator(request):
    num1 = float(request.POST.get('num1'))
    num2 = float(request.POST.get('num2'))
    operator = request.POST.get('operator')

    result = 0

    if(operator == '+'):
        result = num1+num2
    elif(operator == '-'):
        result = num1 - num2
    elif(operator == '*'):
        result = num1 * num2
    elif(operator == '/'):
        result = num1 / num2
    elif(operator == '^'):
        result = num1 ** num2

    data = {'result':result,'num1':num1,'num2':num2,'opcode':operator}

    return render(request,'index.html',data)
    
    
def resetValues(request):
    data = {'num1':"",'num2':"",'result':""}
    return render(request,'index.html',data)