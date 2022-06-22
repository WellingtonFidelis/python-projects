from django.views.generic import TemplateView, FormView
from core.models import Service, Employee, Feature
from core.forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages


class IndexView(FormView):
  template_name = 'index.html'
  form_class = ContactForm
  success_url = reverse_lazy('index')
  
  def get_context_data(self, **kwargs):
    context = super(IndexView, self).get_context_data(**kwargs)
    context['services'] = Service.objects.order_by('?').all()
    context['employees'] = Employee.objects.order_by('?').all()
    context['features'] = Feature.objects.order_by('?').all()[:6]
    return context
  
  
  def form_valid(self, form, *args, **kwargs):
    form.send_mail()
    messages.success(self.request, 'E-mail send successfully.')
    return super(IndexView, self).form_valid(form, *args, **kwargs)
  
  
  def form_invalid(self, form, *args, **kwargs):
    messages.error(self.request, 'Error when trying to send the e-mail.')
    return super(IndexView, self).form_invalid(form, *args, **kwargs)
    