from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from .models import SignUp

# Create your views here.
def home(request):
    title = "Sign Up Now"
    form = SignUpForm(request.POST or None)

    if request.user.is_authenticated():
        title = "Welcome" %(request.user)

    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.full_name:
            instance.full_name = "No name was given"
        instance.save()
        print (instance.email)
        print (instance.timestamp)
        context = {
            "title": "Thank you!"
        }
    # if request.method == "POST":
    #     print (request.POST)

    if request.user.is_authenticated() and request.user.is_staff:
        #print(SignUp.objects.all())
        # i = 0
        # for instance in SignUp.objects.all():
        #     print(instance.full_name)
        #     i+=1
        # print(i)
        queryset = SignUp.objects.all().order_by('-timestamp').filter(email__icontains="mail")
        #you can use filter(xyz__iexact="desired term")
        context = {
            "queryset": queryset
        }
    return render(request, 'home.html', context)

def contact(request):

    title = 'Contact Us'
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_full_name = form.cleaned_data.get('full_name')
        form_message = form.cleaned_data.get('message')
        # print (full_name, email, message)
        subject = 'Site contact form'
        contact_message = '''
            %s:%s via %s
            ''' %(
                form_full_name,
                form_message,
                form_email
            )
        form_html_message = '''
            <h1>Hello World! This is a html email message!</h1>
            '''

        from_email = settings.EMAIL_HOS_USER
        to_email = [from_email, 'to_email2', 'to_emailn']


        send_mail(
            subject,
            contact_message,
            from_email,
            to_email,
            html_message = form_html_message,
            fail_silently=True
        )

    context = {
        "form": form,
        "title": title
    }
    return render(request, 'forms.html', context)
