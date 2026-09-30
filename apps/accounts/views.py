from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model, authenticate, login, logout
from apps.accounts.forms import LoginForm, RegistrationForm, ProfileForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import CustomUser


# Create your views here.

User = get_user_model()

class RegisterView(TemplateView):
    template_name = 'accounts/registration.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, 'You are already logged in.')
            return redirect('news:home')

        context = self.get_context_data(**kwargs)
        context['form'] = RegistrationForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(
                request,
                "Successfully registeredi!"
            )
            return redirect('accounts:login')    

        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)        

class LoginView(TemplateView):
    template_name = 'accounts/login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect ("news:home")
        context = self.get_context_data(**kwargs)
        context['form'] = LoginForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')


            user = authenticate(request, email = email, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in successfully.')
                return redirect('news:home')
            else:
                form.add_error(None, 'Invalid email or password.')

            context = self.get_context_data(**kwargs)
            context['form'] = form
            return   self.render_to_response(context) 

class LogoutView(TemplateView, LoginRequiredMixin):
    # template_name = 'accounts/logout.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        messages.success(request, 'You have been logged out successfully.')

        return redirect('news:home')



class ProfileView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = 'accounts/profile.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user