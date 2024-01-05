from django.shortcuts import render,HttpResponse
from home.models import Addemp
from django.views.generic.base import RedirectView
from django.shortcuts import redirect
# from django.views.generic import TemplateView,ListView
def ouremp(request):
    return render(request,'ouremp.html')
# Create your views here.
def addemp(request):
    if(request.method=="POST"):
        firstname=request.POST.get('firstName')
        lastname=request.POST.get('lastName')
        male=request.POST.get('male')
        female=request.POST.get('female')
        others=request.POST.get('other')
        address=request.POST.get('addresss')
        pancard=request.POST.get('pancard')
        salary=request.POST.get('salary')
        designation=request.POST.get('designation')
        email=request.POST.get('email')
        password=request.POST.get('passwordd')
        number=request.POST.get('number')
        addemp=Addemp(firstname=firstname,lastname=lastname,male=male,female=female,other=others,address=address,pancard=pancard,salary=salary,designation=designation,
        email=email,password=password,number=number)
        addemp.save()

    return render(request,'addemp.html')
def editemp(request):
    return render(request,'editemp.html')
def viewemp(request):
    queryset=Addemp.objects.all()
    context={"queryset":queryset}
    return render(request,'viewemp.html',context)
# >>> Addemp.objects.all().values()
# <QuerySet [{'yourid': 1, 'firstname': 'anuraag', 'lastname': '', 'male': None, 'female': None, 'other': None,
#  'address': '', 'pancard': '', 'salary': '', 'designation': '', 'email': '', 'password': '', 'number': ''}, 
#  {'yourid': 2, 'firstname': 'anuraag', 'lastname': 'nalam', 'male': None, 'female': None, 'other': None, 'address': '',
#   'pancard': '', 'salary': '', 'designation': '', 'email': '', 'password': '', 'number': ''}]>
# def addemp(request,id=None):
#     instance=get_object_or 404(Addemp,id=id)
#     instance.delete()
#     return redirect("computer list")
def delete(request,id):
    addemp=Addemp.objects.get(yourid=id)
    addemp.delete()
    return redirect("/viewemp")