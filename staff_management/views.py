# from channels.auth import login, logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from staff_management.EmailBackEnd import EmailBackEnd


def home(request):
    return render(request, 'index.html')


def loginPage(request):
    return render(request, 'login.html')



def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'))
        if user != None:
            login(request, user)
            user_type = user.user_type
            #return HttpResponse("Email: "+request.POST.get('email')+ " Password: "+request.POST.get('password'))
            if user_type == '1':
                return redirect('admin_home')
                
            elif user_type == '2':
                # return HttpResponse("Staff Login")
                return redirect('staff_home')
                
            elif user_type == '3':
                # return HttpResponse("Finance Login")
                return redirect('finance_home')

            elif user_type == '4':
                # return HttpResponse("Ict Login")
                return redirect('ict_home')

            elif user_type == '5':
                # return HttpResponse("Hr Login")
                return redirect('hr_home')

            elif user_type == '6':
                # return HttpResponse("Registrar Login")
                return redirect('registrar_home')

            elif user_type == '7':
                # return HttpResponse("Transport Login")
                return redirect('transport_home')

            elif user_type == '8':
                # return HttpResponse("Academic Login")
                return redirect('academic_home')

            elif user_type == '9':
                # return HttpResponse("Library Login")
                return redirect('library_home')

            elif user_type == '10':
                # return HttpResponse("Medical Login")
                return redirect('medical_home')

            elif user_type == '11':
                # return HttpResponse("Research Login")
                return redirect('research_home')

            elif user_type == '12':
                # return HttpResponse("Planning Login")
                return redirect('planning_home')

            elif user_type == '13':
                # return HttpResponse("procurement Login")
                return redirect('procurement_home')

            elif user_type == '14':
                # return HttpResponse("Student Login")
                return redirect('student_home')

            else:
                messages.error(request, "Invalid Login!")
                return redirect('login')

        else:
            messages.error(request, "Invalid Login Credentials!")
            #return HttpResponseRedirect("/")
            return redirect('login')



def get_user_details(request):
    if request.user != None:
        return HttpResponse("User: "+request.user.email+" User Type: "+request.user.user_type)
    else:
        return HttpResponse("Please Login First")



def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


