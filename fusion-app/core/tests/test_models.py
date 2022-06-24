# coverage run manage.py test
# coverage report
# coverage html
# cd htmlcov && python -m http.server
# access 0.0.0.0:8000 on browser or localhost:8000

import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_path


class GetFilePathTestCase(TestCase):
  def setUp(self):
    self.filename = f'{uuid.uuid4()}.png'
    
  def test_get_file_path(self):
    file = get_file_path(None, 'teste.png')
    self.assertTrue(len(file), len(self.filename))
    
    
class ServiceTestCase(TestCase):
  def setUp(self):
    self.service = mommy.make('Service')
    
  def test_str(self):
    self.assertEquals(str(self.service), self.service.service)
    
class RoleTestCase(TestCase):
  def setUp(self):
    self.role = mommy.make('Role')
    
  def test_str(self):
    self.assertEquals(str(self.role), self.role.role)
    

class EmployeeTestCase(TestCase):
  def setUp(self):
    self.employee = mommy.make('Employee')
    
  def test_str(self):
    self.assertEquals(str(self.employee), self.employee.name)
    
    
class FeatureTestCase(TestCase):
  def setUp(self):
    self.feature = mommy.make('Feature')
    
  def test_str(self):
    self.assertEquals(str(self.feature), self.feature.feature)