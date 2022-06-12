from django.urls import reverse
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from . forms import UrlForm, CustomUserForm
from . models import UrlShortener, CustomUser
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class CreateUrl(CreateView):
    model = UrlShortener
    form_class = UrlForm
    template_name = "shortener/create_url.html"

    def get_success_url(self):
        return reverse("shortener:url_detail", kwargs={"pk":self.object.pk})

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            messages.error(self.request, "Unauthorized, Login first to proceed...!!")
            return redirect("/")
            
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, DetailView):
    """View authenticated user profile."""

    model = CustomUser
    template_name = 'shortener/user_profile.html'
    
    def get_object(self):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = CustomUser.objects.get(username = self.request.user)
        return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    """Update authenticated user profile."""

    model = CustomUser
    form_class = CustomUserForm
    template_name = 'shortener/edit_profile.html'
    success_url = reverse_lazy('shortener:profile')

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = CustomUser.objects.get(username = self.request.user)
        return context


class URLList(LoginRequiredMixin, ListView):
    """Get list of url created by authenticated user"""

    Model = UrlShortener
    context_object_name = "url_list"
    template_name = "shortener/url_list.html"

    def get_queryset(self):
        return UrlShortener.objects.filter(created_by = self.request.user)


class URLView(LoginRequiredMixin, DetailView):
    """View URL Details."""

    model = UrlShortener
    template_name = 'shortener/url_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url_detail"] = UrlShortener.objects.get(pk=self.object.pk)
        return context

class URLDeleteView(LoginRequiredMixin, DeleteView):
    """View URL Details."""

    model = UrlShortener
    context_object_name = "link"
    template_name = 'shortener/delete_url.html'
    success_url = reverse_lazy('shortener:url_list')
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["url_detail"] = UrlShortener.objects.get(pk=self.object.pk)
    #     return context


