from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserFormFields
from .forms import UserFormData


def fields(request):
    userformfields = UserFormFields()
    return render(request, "fields.html", {"formfields": userformfields})


def userdata(request):
    if request.method == "POST":
        user_form_data = UserFormData(request.POST)
        if user_form_data.is_valid():
            lastname = user_form_data.cleaned_data["lastname"]
            firstname = user_form_data.cleaned_data["firstname"]
            patronymic = user_form_data.cleaned_data["patronymic"]
            age = user_form_data.cleaned_data["age"]
            student_group = user_form_data.cleaned_data["student_group"]
            date_of_birth = user_form_data.cleaned_data["date_of_birth"]
            programming_language = user_form_data.cleaned_data["programming_language"]
            email = user_form_data.cleaned_data["email"]
            data = {"lastname": lastname, "firstname": firstname, "patronymic": patronymic, "age": age,
                    "student_group": student_group, "date_of_birth": date_of_birth, "programming_language":
                    programming_language, "email": email}

            return render(request, "student.html", context=data)
        else:
            return  HttpResponse("Invalid data")
    else:
        user_form_data = UserFormData()
        return render(request, "data.html", {"form": user_form_data})
