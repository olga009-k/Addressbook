from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from . import forms
from . import models
import phonebook


class HomePageView(TemplateView):
    template_name = 'phonebook/home.html'

    def get_context_data(self, **kwards):
        context = super().get_context_data(**kwards)
        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get('query')
        search_message = "All phones"
        if search_by in ['phone', 'first_name', 'last_name', 'address'] and query:
            if search_by == 'first_name':
                search_message = f'Searching by "first name" for "{query}"'
                persones = models.Person.objects.filter(first_name=query)
            elif search_by == 'last_name':
                search_message = f'Searching by "last name" for "{query}"'
                persones = models.Person.objects.filter(last_name=query)
            elif search_by == 'address':
                search_message = f'Searching by "address" for "{query}"'
                persones = models.Person.objects.filter(address__contains=query)
            else:
                persones = models.Person.objects.filter(phone=query)
                search_message = f'Searching by "phones" for "{query}"'
        else:
            persones = models.Person.objects.all()

        context["search_message"] = search_message
        context["persones"] = persones
        return context


class AddPhoneFormView(CreateView):
    template_name = 'phonebook/add_person.html'
    form_class = forms.PersonFrom
    success_url = reverse_lazy('home')


class DeletePhoneView(DeleteView):
    model = models.Person
    template_name="phonebook/delete_person.html"
    success_url = reverse_lazy('home')


class UpdatePhoneView(UpdateView):
    
    model = models.Person
    template_name="phonebook/edit_person.html"
    form_class = forms.PersonFrom
    success_url = reverse_lazy('home')
