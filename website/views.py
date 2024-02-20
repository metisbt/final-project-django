from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.forms import ContactForm, NewsletterForm
from django.contrib import messages


def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "پیام شما با موفقیت ارسال شد.")
        else:
            messages.add_message(request, messages.ERROR, "پیام شما ارسال نشد!")

    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "ایمیل شما با موفقیت ثبت شد")
    else:
        messages.add_message(request, messages.ERROR, "ایمیل شما ثبت نشد!")
    
    form = NewsletterForm()
    return render(request, 'website/index.html', {'form': form})
