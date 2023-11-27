from django.shortcuts import render
from .forms import AgeInForm, HeyForm, OrderTotalForm


# Create your views here.
def root(request):
    return render(request, "root.html")


def Hey_You(request):
    form = HeyForm(request.GET)
    if form.is_valid():
        name = form.cleaned_data["name"]
        return render(request, "HeyYou.html", {"form": form, "name": name})
    else:
        form = HeyForm()
    return render(request, "HeyYou.html", {"form": form, "name": None})


def Age_In(request):
    form = AgeInForm(request.GET)
    if form.is_valid():
        birthyear = form.cleaned_data["birthyear"]
        end = form.cleaned_data["end"]
        answer = end - birthyear
        return render(
            request,
            "AgeIn.html",
            {"form": form, "x": birthyear, "y": end, "age": answer},
        )
    else:
        form = AgeInForm()
    return render(
        request, "AgeIn.html", {"form": form, "x": None, "y": None, "age": None}
    )


def Order_Total(request):
    form = OrderTotalForm(request.GET)
    if form.is_valid():
        burgers = form.cleaned_data["burgers"]
        fries = form.cleaned_data["fries"]
        drinks = form.cleaned_data["drinks"]
        total = (burgers*4.50) + (fries*1.50) + drinks
        return render(request, "OrderTotal.html", {"form":form, "total":total})
    else:
        form = OrderTotalForm()
    return render(request, "OrderTotal.html", {"form":form, "total":None})
