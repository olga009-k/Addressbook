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
        print('test', search_by)
        if search_by in ['phone', 'first_name', 'last_name', 'address'] and query:
            if search_by == 'first_name':
                search_message = f'Searching by "first name" for "{query}"'
                persones = models.Persone.objects.filter(first_name=query)
            elif search_by == 'last_name':
                search_message = f'Searching by "last name" for "{query}"'
                persones = models.Persone.objects.filter(last_name=query)
            elif search_by == 'address':
                search_message = f'Searching by "address" for "{query}"'
                print(search_message)
                persones = models.Persone.objects.filter(address__contains=query)
            else:
                persones = models.Persone.objects.filter(phones__phone__startswith=query)
                search_message = f'Searching by "phones" for "{query}"'
        else:
            persones = models.Persone.objects.all()

        context["search_message"] = search_message
        context["persones"] = persones
        return context


class AddPhoneFormView(CreateView):
    template_name = 'phonebook/add_persone.html'
    form_class = forms.CreatePersoneFrom
    success_url = reverse_lazy('home')

    def get_success_url(self) -> str:
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            models.Phone.objects.create(phone=phone_number, contact=self.object)
        return super().get_success_url()


class DeletePhoneView(DeleteView):
    model = models.Persone
    template_name="phonebook/delete_persone.html"
    success_url = reverse_lazy('home')


class UpdatePhoneView(UpdateView):
    
    model = models.Persone
    template_name="phonebook/edit_persone.html"
    form_class = forms.EditPersoneForm
    success_url = reverse_lazy('home')

    def get_success_url(self) -> str:
        phone_numbers = self.request.POST.get('phones')
        for phone_number in phone_numbers.split('\n'):
            models.Phone.objects.create(phone=phone_number, contact=self.object)
        return super().get_success_url()






