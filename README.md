# django-meta

To create and view a form in Django, follow these steps:

1. Create a Form:
   In your app's forms.py file.
   Python

```from django import forms

class ContactForm(forms.Form):
name = forms.CharField(max_length=100)
email = forms.EmailField()
message = forms.CharField(widget=forms.Textarea)

```

2. Create a View:
   In your app's views.py file.
   Python

```
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
if request.method == 'POST':
form = ContactForm(request.POST)
if form.is_valid(): # Process the form data
name = form.cleaned_data['name']
email = form.cleaned_data['email']
message = form.cleaned_data['message'] # ... do something with the data
return render(request, 'success.html')
else:
form = ContactForm()

    return render(request, 'contact.html', {'form': form})
```

3. Create a Template:
   Create a template file named contact.html in your app's templates directory:
   Code

```
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
</head>
<body>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>

```

4. Configure URL:
   Add a URL pattern in your app's urls.py file:
   Python

```

from django.urls import path
from . import views

urlpatterns = [
path('contact/', views.contact_view, name='contact'),
]

```

5. Access the Form in Browser:
   Run your Django server.
   Navigate to the URL you defined in your urls.py (e.g., http://localhost:8000/contact/).
   You should see the form rendered on the page.
