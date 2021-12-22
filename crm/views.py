from django.urls import reverse
from django.views.generic import CreateView
from .forms import SignUpForm


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = SignUpForm

    def get_success_url(self):
        return reverse('login')

