from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):
  def setUp(self):
    self.data = {
      'name': 'Teste Testando',
      'email': 'test@gmail.com',
      'subject': 'Teste Testando',
      'message': 'Teste Testando'
    }
    
    self.client = Client()
    
  def test_form_valid(self):
    request = self.client.post(reverse_lazy('index'), data=self.data)
    self.assertEquals(request.status_code, 302)
    
  def test_form_invalid(self):
    data = {
      'name': 'Teste Testando',
      'email': 'test@gmail.com',
      'message': 'Teste Testando'
    }
    request = self.client.post(reverse_lazy('index'), data=data)
    self.assertEquals(request.status_code, 200)