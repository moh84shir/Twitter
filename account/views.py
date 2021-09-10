from django.shortcuts import render, redirect
from django.views import View
from . import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class SigninView(View):
    form_class = forms.SigninForm
    template_name = "account/signin.html"
    context = {}

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        signin_form = self.form_class(request.POST or None)
        self.context['signin_form'] = signin_form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        signin_form = self.form_class(request.POST or None)
        if signin_form.is_valid():
            user_name = signin_form.cleaned_data.get('user_name')
            password = signin_form.cleaned_data.get('password')

            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                signin_form.add_error(
                    field="user_name", error="Your user name or password is not ok")

        context = {'signin_form': signin_form}

        return render(request, self.template_name, context)


class SignupView(View):
    form_class = forms.SignupForm
    template_name = "account/signup.html"
    context = {}

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        signup_form = self.form_class(request.POST)
        self.context['signup_form'] = signup_form
        return render(request, self.template_name, self.context)

    def post(self, request):
        signup_form = self.form_class(request.POST)
        if not signup_form.is_valid():
            user_name = signup_form.cleaned_data.get('user_name')
            password = signup_form.cleaned_data.get('password')

            new_user = User.objects.create_user(username=user_name, password=password)
            new_user.save()
            return redirect('/account/signin/')

        self.context['signup_form'] = signup_form
        return render(request, self.template_name, self.context)
