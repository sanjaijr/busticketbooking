from django.shortcuts import render,redirect
from busapp.models import Driver
from busapp.form import DriverForm
# Create your views here.
# def index(request):
#     return render(request,"busapp/index.html")
#
#
# def detail(request):
#     return render(request,"busapp/details.html")
#
#
# def empDetails(request):
#     name="sanjai"
#     emp_data=Driver.objects.all()
#     emp_dict = {"emp_list":emp_data}
#     return render(request, "busapp/index.html", context =emp_dict)
#
#
# def create_view(request):
#     form=DriverForm()
#     if request.method =="POST":
#         form = DriverForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("home/")
#     return render(request,"busapp/details.html",{"form":form})


def empDetails(request):
    name="sanjai"
    emp_data=Driver.objects.all()
    emp_dict = {"emp_list":emp_data}
    return render(request, "busapp/index.html", context =emp_dict)
    #return HttpResponse("<h1 this is my application <h1>")

#u
def create_view(request):
    form=DriverForm()
    if request.method =="POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    return render(request,"busapp/create.html",{"form":form})

def delete_view(request,id):
    emp_data=Driver.objects.get(id=id)
    emp_data.delete()
    return redirect("/home")

def update_view(request,id):
    emp_data=Driver.objects.get(id=id)
    if request.method == "POST":
        drivername=request.POST["drivername"]
        age=request.POST["age"]
        contact_no=request.POST["contact_no"]
        bus_no=request.POST["bus_no"]

        emp_data.drivername=drivername
        emp_data.age=age
        emp_data.contact_no=contact_no
        emp_data.bus_no=bus_no
        emp_data.save()
        return redirect("/home")
    return render(request,"busapp/update.html",{"Driver":emp_data})



