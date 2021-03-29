from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views import View
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView

from cats.models import Cat, Breed

class MainList(LoginRequiredMixin, View):
    def get(self, request):
        breed = Breed.objects.all()
        cat = Cat.objects.all()
        ctx = { 'breed_list' : breed, 'cat_list' : cat }
        return render(request, 'cats/main.html', ctx)


class CatList(LoginRequiredMixin, ListView):
    model = Cat


class BreedList(LoginRequiredMixin, ListView):
    model = Breed


class CreateCat(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:main')


class UpdateCat(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:main')


class DeleteCat(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:main')


class CreateBreed(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:main')


class UpdateBreed(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:main')


class DeleteBreed(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:main')
