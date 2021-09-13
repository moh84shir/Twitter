from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
                    field="user_name",
                    error="Your user name or password is not ok")

        self.context['signin_form'] = signin_form

        return render(request, self.template_name, self.context)


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
        import pdb
        pdb.set_trace()
        if signup_form.is_valid():
            user_name = signup_form.cleaned_data.get('user_name')
            first_name = signup_form.cleaned_data.get('user_first_name')
            last_name = signup_form.cleaned_data.get('user_last_name')
            email = signup_form.cleaned_data.get('user_email')
            password = signup_form.cleaned_data.get('user_password')
            re_password = signup_form.cleaned_data.get('re_password')
            is_user_exists = User.objects.filter(username=user_name).exists()
            print(
                user_name,
                first_name,
                last_name,
                email,
                password,
                re_password
            )

            if password != re_password:
                signup_form.add_error('re_password', "password != re_password")

            if is_user_exists:
                signup_form.add_error('user_name', "this user is exists")

            if len(password) < 8:
                signup_form.add_error('user_password', "password is not ok")

            if password == user_name:
                signup_form.add_error('user_password', "password is not ok")

            if password.lower() == password:
                signup_form.add_error('user_password', "password is not ok")

            if password.upper() == password:
                signup_form.add_error('user_password', "password is not ok")

            if password.isdigit():
                signup_form.add_error('user_password', "password is not ok")

            if password.isalpha():
                signup_form.add_error('user_password', "password is not ok")

            User.objects.create_user(
                username=user_name,
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email
            )

            return redirect('/account/signin/')

        self.context['signup_form'] = signup_form
        return render(request, self.template_name, self.context)


class SignoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/account/signin/')

    @method_decorator(login_required(login_url="account/signin"))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
