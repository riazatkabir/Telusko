from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.


def home(request):
     return render (request, "home.html")
# def divO(request):
#    return render(request, 'divides.html')

def calculation(request):
   res = 0
   if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')
        
        if operation == 'add':
            res = num1 + num2
        elif operation == 'subtract':
            res = num1 - num2
        elif operation == 'multiply':
            res = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                res = num1 / num2
            else:
                res = 'Cannot divide by zero'
                # redirect(request,'myapp/templates/divides.html', {'res' : res} )
   else:
    res = 'Invalid operation'
        
   return render(request, 'home.html', {'res': res})
    
   
   
   
   
   
   # try:
   #    val1 = int(request.POST['num1'])
   #    val2 = int(request.POST['num2'])
   #    res = val1 +val2
   # # except(KeyError, ValueError):
   # #    res= "Invalid input"
      

   #      return render (request, 'result.html', {'result' : res})

