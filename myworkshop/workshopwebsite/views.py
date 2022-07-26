from unicodedata import name
from django.forms import NullBooleanField
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from . import views
from .models import *
from .forms import *
from datetime import datetime
from datetime import date
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


def index(request):
    return render(request, "workshopwebsite/index.html", {})


def add_client(request):
    if request.method == "POST":
        form = Addclient(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            client = Client(name=name, phone=phone)
            client.save()
        return HttpResponse("client succesfully added")
    else:
        form = Addclient()
    return render(request, "workshopwebsite/add_client.html", {"form": form})


def add_car(request):
    if request.method == "POST":
        form = Addcar(request.POST)
        if form.is_valid():
            number = form.cleaned_data["number"]
            model = form.cleaned_data["model"]
            year = form.cleaned_data["year"]
            car = Car(number=number, model=model, year=year)
            car.save()
        return HttpResponse("car succesfully added")
    else:
        form = Addcar()
    return render(request, "workshopwebsite/add_car.html", {"form": form})


# task 1
def add_order(request):
    if request.method == "GET":
        form = Addorder()
        return render(request, "workshopwebsite/add_order.html", {"form": form})
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        number = request.POST["number"]
        model = request.POST["model"]
        year = request.POST["year"]
        issue_description = request.POST["issue_description"]
        try:
            client = Client.objects.get(name=name, phone=phone)
        except Exception:
            client = Client(name=name, phone=phone)
            client.save()
        try:
            car = Car.objects.get(number=number, model=model, year=year)
        except Exception:
            car = Car(number=number, model=model, year=year)
            car.save()
        orderInitialDetailsrders = OrderInitialDetails(
            client=client,
            issue_description=issue_description,
            car=car,
            beginning_date=date.today(),
        )
        orderInitialDetailsrders.save()
        form = Addorder()
        return render(request, "workshopwebsite/add_order.html", {"form": form})


def check_button(request):
    form = Checkyourorder(request.GET)
    return render(request, "workshopwebsite/check_button.html", {"form": form})


def check_your_order(request):
    client = request.GET["client"]
    orders = OrderInitialDetails.objects.filter(client=client)
    info = []
    for order in orders:
        info.append(order)
    return render(request, "workshopwebsite/check_your_order.html", {"info": orders})


# task 2 (finish)
def choose_mechanic(request):
    orderInitialDetail = OrderInitialDetails.objects.filter(mechanic=None)
    return render(
        request,
        "workshopwebsite/choose_mechanic.html",
        {"orderInitialDetail": orderInitialDetail},
    )


# task 2 (button -> assign_mechanic.html)
def assign_mechanic(request):
    if request.method == "POST":
        id = request.POST["id"]
        mechanic_name = request.POST["mechanic"]
        try:
            mech = Mechanic.objects.get(name=mechanic_name)
            orderInitialDetail = OrderInitialDetails.objects.get(id=id)
            orderInitialDetail.mechanic = mech
            orderInitialDetail.save()
        except Exception:
            return render(request, "workshopwebsite/mechanic_restart.html", {})
        form = Choosemechanic()
        return render(request, "workshopwebsite/assign_mechanic.html", {"form": form})
    else:
        form = Choosemechanic()
        return render(request, "workshopwebsite/assign_mechanic.html", {"form": form})


# task 3 (finish)
def choose_finishing_date(request):
    orderInitialDetail = OrderInitialDetails.objects.filter(finishing_date=None)
    return render(
        request,
        "workshopwebsite/choose_finishing_date.html",
        {"orderInitialDetail": orderInitialDetail},
    )


# task 3 (button -> proceed_to_data_completion.html)
def proceed_to_data_completion(request):
    if request.method == "POST":
        id = request.POST["id"]
        price = request.POST["price"]
        finishing_date = request.POST["finishing_date"]
        try:
            orderInitialDetail = OrderInitialDetails.objects.get(id=id)
        except Exception:
            orders = OrderInitialDetails.objects.filter(finishing_date=None)
            return render(
                request,
                "workshopwebsite/errorid.html",
                {"orders": orders},
            )
        orderInitialDetail.finishing_date = finishing_date
        orderInitialDetail.price = price
        orderInitialDetail.save()
        form = ChooseFinishingDate()
        return render(
            request, "workshopwebsite/proceed_to_data_completion.html", {"form": form}
        )
    else:
        form = ChooseFinishingDate()
        return render(
            request, "workshopwebsite/proceed_to_data_completion.html", {"form": form}
        )


"""
filter(char=b, number=2)
-a1 
b2 
-c2 
-b4
bb2
return [b2, bb2]

"""

# task 4
def order_list(request):
    orderInitialDetail = OrderInitialDetails.objects.all()
    return render(
        request,
        "workshopwebsite/order_list.html",
        {"orderInitialDetail": orderInitialDetail},
    )


@api_view(["GET", "POST"])
def car(request):
    if request.method == "GET":  # user requesting data
        snippets = Car.objects.all()
        serializer = CarSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == "POST":  # user posting data
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def client(request):
    if request.method == "GET":
        snippets = Client.objects.all()
        serializer = ClientSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def mechanic(request):
    if request.method == "GET":
        snippets = Mechanic.objects.all()
        serializer = MechanicSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MechanicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def orderInitialDetails(request):
    if request.method == "GET":
        snippets = OrderInitialDetails.objects.all()
        serializer = OrderInitialDetailsSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = OrderInitialDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def orderAdditionalDetails(request):
    if request.method == "GET":
        snippets = OrderAdditionalDetails.objects.all()
        serializer = OrderAdditionalDetailsSerializer(snippets, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = OrderAdditionalDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
