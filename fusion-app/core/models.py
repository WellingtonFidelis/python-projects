from django.db import models
from stdimage.models import StdImageField
import uuid


def get_file_path(_instance, filename):
  ext = filename.split('.')[-1]
  filename = f'{uuid.uuid4()}.{ext}'
  return filename

class Base(models.Model):
  created = models.DateField('Created', auto_now_add=True)
  modified = models.DateField('Modified', auto_now=True)
  is_active = models.BooleanField('IsActive', default=True)
  
  class Meta:
    abstract = True
    
    
class Service(Base):
  # tupla de tuplas
  ICON_CHOICES = (
    ('lni-cog', 'Engrenagem'),
    ('lni-stats-up', 'Gráfico'),
    ('lni-users', 'Usuários'),
    ('lni-layers', 'Design'),
    ('lni-mobile', 'Mobile'),
    ('lni-rocket', 'Foguete'),
  )
  
  service = models.CharField('Service', max_length=100)
  description = models.TextField('Description', max_length=200)
  icon = models.CharField('Icon', max_length=12, choices=ICON_CHOICES)
  
  class Meta:
    verbose_name = 'Service'
    verbose_name_plural = 'Services'
    
  def __str__(self):
    return self.service
  
class Role(Base):
  role = models.CharField('Role', max_length=100)
  
  class Meta:
    verbose_name = 'Role'
    verbose_name_plural = 'Roles'
    
  def __str__(self):
    return self.role
  
class Employee(Base):
  name = models.CharField('Name', max_length=100)
  role = models.ForeignKey(to='core.Role',verbose_name='Role', on_delete=models.CASCADE)
  biography = models.TextField('Biography', max_length=200)
  image = StdImageField('Image', upload_to=get_file_path, variations={
    'thumb': {
      'width': 480,
      'height': 480,
      'crop': True
    }
  })
  social_midia_facebook = models.CharField('SocialMidiaFacebook', max_length=100, default='#')
  social_midia_twitter = models.CharField('SocialMidiaTwitter', max_length=100, default='#')
  social_midia_instagram = models.CharField('SocialMidiaInstagram', max_length=100, default='#')

  class Meta:
    verbose_name = 'Employee'
    verbose_name_plural = 'Employees'
    
  def __str__(self):
    return self.name