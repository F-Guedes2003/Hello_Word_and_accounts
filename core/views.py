from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, name):
    return HttpResponse(f'hello {name}')

def soma(request, num1, num2):
    result = num1 + num2
    return HttpResponse(f'O resultado da soma é: {result}')

def subtracao(request, num1, num2):
    result = num1 - num2
    return HttpResponse(f'O resultado da subtração é: {result}')

def multiplicacao(request, num1, num2):
    result = num1 * num2
    return HttpResponse(f'O resultado da multiplicação é: {result}')