from django.shortcuts import render
from django.views.generic import View
from user.forms import LogInForm,UserRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

# view for login
class LogInView(View):
    template_name = 'user/login.html'
    form_class = LogInForm
    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                return redirect('dashboard')
        return render(request,self.template_name,{'form': form,'message':'Login failed please enter correct username and password'})

# view for dashboard
class DashBoardView(TemplateView):
    template_name='user/dashboard.html'

# view for list of users
class ListOfUserView(ListView):
    model = User
    template_name = 'user/user_list.html'

# view for user logout
class UserLogoutView(View):  
    def get(self,request):
        logout(request)
        return render(request,'user/dashboard.html') 


# view for user registration
class UserRegistrationView(CreateView):
    template_name = 'user/user_registration.html'
    form_class = UserRegistrationForm
    success_url = '/login/'