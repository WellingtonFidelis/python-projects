from django import forms
from django.core.mail.message import EmailMessage


class ContactForm(forms.Form):
  name = forms.CharField(label='Name', max_length=100, min_length=3, required=True)
  email = forms.EmailField(label='E-mail', max_length=100, required=True)
  subject = forms.CharField(label='Subject', max_length=100, required=True)
  message = forms.CharField(label='Message', widget=forms.Textarea())
  
  def send_mail(self):
    name = self.cleaned_data['name']
    email = self.cleaned_data['email']
    subject = self.cleaned_data['subject']
    message = self.cleaned_data['message']
    
    content = f'Name: {name}\nE-mail: {email}\nAssunto: {subject}\nMessage: {message}'
    
    mail = EmailMessage(
      subject=subject,
      body=content,
      from_email="wellingtonf20@gmail.com",
      to=['wellingtonf20@gmail.com',],
      headers={
        'Reply-To': email,
      }      
    )
    
    mail.send(fail_silently=False)