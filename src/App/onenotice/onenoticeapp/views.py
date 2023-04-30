from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.utils.html import escape
from django.utils.safestring import mark_safe

from .models import Numpy

from random import choice


def index(request):
    return render(request, "onenoticeapp/index.html")


def numpy(request):
    # maxFunctions = Numpy.objects.
    numpyDocUrl = str("https://numpy.org/doc/stable/reference/generated/")
    myFunc = Numpy.objects.get(id=choice(range(1, 2211, 1)))
    myFuncName = myFunc.function_name
    myFuncPath = myFunc.local_path + myFunc.filename
    officialDocUrl = numpyDocUrl + myFunc.filename

    # myFuncName = "numpy-hamming"

    with open(myFuncPath) as docFile:
        docToInsert = docFile.read()

    template = loader.get_template("onenoticeapp/numpy.html")
    # context = {"myFuncName": myFuncName}
    context = {
        "officialDocUrl": officialDocUrl,
        "funcDocText": mark_safe(docToInsert),
        "myFuncName": myFuncName,
    }

    return render(request, "onenoticeapp/numpy.html", context)
