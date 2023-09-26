from django.shortcuts import render, redirect
from .models import Form

# Create your views here.
def index(request):
    obj = Form.objects.all()
    return render(request, "index.html", {'result': obj})

def form_details(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        dob = request.POST.get('dob', )
        age = request.POST.get('age', )
        gender = request.POST.get('gender', )
        mob_no = request.POST.get('mob_no', )
        email = request.POST.get('email', )
        address = request.POST.get('address', )
        department = request.POST.get('department', )
        courses = request.POST.get('courses', )
        purpose = request.POST.get('purpose', )
        mat_pro = request.POST.get('mat_pro', )





        form=Form(name=name,dob=dob,age=age,gender=gender,mob_no=mob_no,email=email,address=address,department=department,courses=courses,purpose=purpose,mat_pro=mat_pro)
        form.save()
        return redirect('collageapp:message')
    return render(request,'form.html')

def message(request):
    return render(request, "msg.html")


def index1(request):
    return render(request, "index1.html")