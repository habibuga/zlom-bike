from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic.detail import DetailView

from .forms import SearchOffer, NewUserForm, LoginForm, ResetPasswordForm, UpdateUserForm, UpdateProfileForm
from .models import Offer, Category


class StartView(View):
    def get(self, request):
        form = SearchOffer()
        categories = Category.objects.all()
        ctx = {
            "form": form,
            "categories": categories
        }
        return render(request=request, template_name="start_page.html", context=ctx)

    def post(self, request):
        pass


class OfferDetailView(DetailView):

    model = Offer
    template_name = "offer_details.html"
    context_object_name = "offer"


class CategoryContainView(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        offers = Offer.objects.filter(category=category)
        ctx = {
            "offers": offers,
            "category": category
        }
        return render(request=request, template_name="category_content.html", context=ctx)


class UserRegistrationView(View):
    def get(self, request):
        form = NewUserForm()
        ctx = {
            "form": form,
        }
        return render(request=request, template_name="user_registration.html", context=ctx)

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.location = form.cleaned_data.get('location')
            user.profile.tel_num = form.cleaned_data.get('tel_num')
            user.save()
            return redirect('start')
        else:
            form.add_error(None, 'Wprowadź poprwane dane!')
            ctx = {
                "form": form,
            }
            return render(request=request, template_name="user_registration.html", context=ctx)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        ctx = {
            "form": form
        }
        return render(request=request, template_name="login.html", context=ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_login = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=user_login, password=password)
            if user is not None:
                login(request, user)
                return redirect('start')
            else:
                form.add_error(None, 'Niepoprawny login lub hasło!')
                ctx = {
                    'form': form
                }
                return render(request=request, template_name='login.html', context=ctx)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


class ResetPasswordView(LoginRequiredMixin, FormView):
    template_name = 'reset_password.html'
    success_url = reverse_lazy('start')
    form_class = ResetPasswordForm

    def form_valid(self, form):
        password1 = form.cleaned_data['password']
        user = self.request.user
        user.set_password(password1)
        user.save()
        redirect_site = super().form_valid(form)
        return redirect_site


class UpdateUserView(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UpdateUserForm(initial={
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
        })
        profile_form = UpdateProfileForm(initial={
            "location": request.user.profile.location,
            "tel_num": request.user.profile.tel_num
        })
        ctx = {
            "user_form": user_form,
            "profile_form": profile_form
        }
        return render(request=request, template_name="update_user.html", context=ctx)

    def post(self, request):
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Twoje dane zmienione!")
            return redirect('start')
        else:
            user_form.add_error(None, 'Wprowadź poprwane dane!')
            ctx = {
                "user_form": user_form,
                "profile_form": profile_form
            }
            return render(request=request, template_name="update_user.html", context=ctx)
