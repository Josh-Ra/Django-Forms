from django.shortcuts import render
from django.http import HttpRequest
from .forms import Warmup2Form, Logic2Form, String2Form, List2Form


# Create your views here.
def root(request: HttpRequest) -> render:
    return render(request, "root.html")


def Warmup_2(request: HttpRequest) -> render:
    form = Warmup2Form(request.GET)
    if form.is_valid():
        word = form.cleaned_data["word"]
        number = form.cleaned_data["number"]
        new_word = word[:3]
        for i in range(number - 1):
            new_word += word[:3]
        return render(request, "Warmup2.html", {"form": form, "new_word": new_word})
    else:
        form = Warmup2Form()
    return render(request, "Warmup2.html", {"form": form, "new_word": None})


def Logic_2(request: HttpRequest) -> render:
    form = Logic2Form(request.GET)
    if form.is_valid():
        number1 = form.cleaned_data["number1"]
        number2 = form.cleaned_data["number2"]
        number3 = form.cleaned_data["number3"]
        total = 0
        for num in [number1, number2, number3]:
            if num in range(13, 20):
                if num == 15 or num == 16:
                    total += num
                else:
                    pass
            else:
                total += num
        return render(request, "Logic2.html", {"form": form, "total": total})
    return render(request, "Logic2.html", {"form": Logic2Form(), "total": None})


def String_2(request: HttpRequest) -> render:
    form = String2Form(request.GET)
    if form.is_valid():
        word = form.cleaned_data["word"]
        if ".xyz" not in word and "xyz" in word:
            return render(request, "String2.html", {"form": form, "word": True})
    else:
        form = String2Form()
    return render(request, "String2.html", {"form": form, "word": False})


def List_2(request: HttpRequest) -> render:
    listOfNum = []
    average = None
    form = List2Form(request.GET)
    if form.is_valid():
        for i in range(7):
            if form.cleaned_data[f"Number{i}"] is not None:
                listOfNum.append(form.cleaned_data[f"Number{i}"])
        listOfNum.remove(max(listOfNum))
        listOfNum.remove(min(listOfNum))
        average = round(sum(listOfNum) / len(listOfNum))
    else:
        form = List2Form()
    return render(request, "List2.html", {"form": form, "average": average})
