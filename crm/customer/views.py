from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse
from django.shortcuts import get_object_or_404


class CustomerListView(ListView):
    template_name = 'customer/customer_list.html'
    paginate_by = 5
    model = Customer
    queryset = Customer.objects.all()


class CustomerCreateView(CreateView):
    template_name = 'customer/customer.html'
    form_class = CustomerForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('customer:customer-list')


class CustomerUpdateView(UpdateView):
    template_name = 'customer/customer.html'
    form_class = CustomerForm

    def get_object(self):
        customer_id = self.kwargs.get('id')
        return get_object_or_404(Customer, id=customer_id)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('customer:customer-list')


class CustomerDeleteView(DeleteView):
    def get_object(self):
        customer_id = self.kwargs.get('id')
        return get_object_or_404(Customer, id=customer_id)

    def get_success_url(self):
        return reverse('customer:customer-list')
