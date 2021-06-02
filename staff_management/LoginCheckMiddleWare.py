from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.urls import reverse


class LoginCheckMiddleWare(MiddlewareMixin):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        # print(modulename)
        user = request.user

        #Check whether the user is logged in or not
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "staff_management.HodViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("admin_home")
            
            elif user.user_type == "2":
                if modulename == "staff_management.StaffViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("staff_home")
            
            elif user.user_type == "3":
                if modulename == "staff_management.FinanceViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("finance_home")

            elif user.user_type == "4":
                if modulename == "staff_management.IctViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("ict_home")

            elif user.user_type == "5":
                if modulename == "staff_management.HrViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("hr_home")

            
            elif user.user_type == "6":
                if modulename == "staff_management.RegistrarViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("registrar_home")

            elif user.user_type == "7":
                if modulename == "staff_management.TransportViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("transport_home")

            elif user.user_type == "8":
                if modulename == "staff_management.AcademicViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("academic_home")

            elif user.user_type == "9":
                if modulename == "staff_management.LibraryViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("library_home")

            elif user.user_type == "10":
                if modulename == "staff_management.MedicalViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("medical_home")  

            elif user.user_type == "11":
                if modulename == "staff_management.ResearchViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("research_home") 

            elif user.user_type == "12":
                if modulename == "staff_management.PlanningViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("planning_home") 

            elif user.user_type == "13":
                if modulename == "staff_management.ProcurementViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("procurement_home") 

            elif user.user_type == "14":
                if modulename == "staff_management.StudentViews":
                    pass
                elif modulename == "staff_management.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("student_home") 

            else:
                return redirect("login")

        else:
            if request.path == reverse("login") or request.path == reverse("doLogin"):
                pass
            else:
                return redirect("login")
