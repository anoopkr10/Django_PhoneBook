from django.shortcuts import render, redirect

from contact.forms import ContactForm
from contact.models import Contact


def insert(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})


def show(request):
    contact = Contact.objects.all()
    return render(request, 'show.html', {'contact': contact})


def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect("/show")


def edit(request, id):
    contact = Contact.objects.get(id=id)
    form = ContactForm(instance=contact)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('/show')
    return render(request, 'edit.html', {'form': form})
