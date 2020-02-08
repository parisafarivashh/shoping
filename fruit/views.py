from django.shortcuts import render
from .models import Fruit
def home(request):
  return render(request,'home.htm')

def fruitt(request):
  Fruit = Fruit.object.all()
  context ={
    "fruit":Fruit
  }
  return render(request,'fruit.htm',context) 
