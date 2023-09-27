from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect, render, Http404

from mailings.forms import *
from mailings.models import *
from mailings.services import send_email, my_job


class IndexView(TemplateView):
    template_name = 'mailings/index.html'
    extra_context = {
        'title': 'Главная'
    }


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'mailings/contact.html'
    success_url = reverse_lazy('/')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Свяжитесь с нами:'
        return context

    def form_valid(self, form):
        if form.is_valid():
            print(form.cleaned_data)
        return redirect('/')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:clients')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:clients')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:clients')


class MailSettingsListView(LoginRequiredMixin, ListView):
    model = MailSettings

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = super().get_queryset().filter(user=self.request.user)
        return queryset


class MailSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MailSettings
    form_class = MailSettingsForm
    success_url = reverse_lazy('mailings:list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        my_job()

        return super().form_valid(form)


class MailSettingsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = MailSettings
    form_class = MailSettingsForm
    permission_required = 'mailings.change_mailsettings'
    success_url = reverse_lazy('mailings:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user and not self.request.user.is_staff:
            raise Http404

        return self.object


class MailSettingsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = MailSettings
    permission_required = 'mailings.delete_mailsettings'
    success_url = reverse_lazy('mailings:list')

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['clients'] = Client.objects.all()
        context_data['mailings_pk'] = self.kwargs.get('pk')

        return context_data


class MessageListView(LoginRequiredMixin, ListView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    # permission_required = 'mailings.change_mailmessage'
    success_url = reverse_lazy('mailings:message_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('mailings:message_list')


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    pk_url_kwarg = 'pk'


class MailingLogListView(LoginRequiredMixin, ListView):
    model = Logs

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = Logs.objects.filter(mailings=self.kwargs.get('pk')).order_by('-last_try')
        return queryset

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailings'] = MailSettings.objects.get(pk=self.kwargs.get('pk'))
        return context_data


