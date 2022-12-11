from django.shortcuts import render
from .forms import myform
from .models import logform
# Create your views here.
from django.contrib import messages


def msg(request):
    if request.method == "POST":
        mydata = myform(request.POST)
        if mydata.is_valid():
            mydata.save()
            # messages.add_message(request, messages.SUCCESS,
            #                      'Your Data have been save successfully !!!')
            # we use this type instead of above
            messages.success(
                request, 'Your Data have been save successfully')

            messages.info(request, 'Now You can Login Easily !!')
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, "this is debug !! ")
            messages.error(request, 'this is error !! ')
            messages.warning(request, 'this is warning !! ')
    else:
        mydata = myform()
    return render(request, "msg/home.html", {"fm": mydata})
