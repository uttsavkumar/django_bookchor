from django.shortcuts import render,redirect
from book.models import *
from django.db.models import Q

def home(r):
    cat = Category.objects.all()
    book = Books.objects.all()
    data = {'book':book,'cat':cat}
    return render(r,'index.html',data)

def insertpage(r):
    if r.method == "POST":
        book = Books()
        book.title = r.POST.get('title')
        book.author = r.POST.get('author')
        book.original_price = r.POST.get('original_price')
        book.current_price = r.POST.get('current_price')
        book.description = r.POST.get('description')
        book.isbn = r.POST.get('isbn')

        cat = r.POST.get('category')
        newcat = Category.objects.get(pk=cat)
        book.category = newcat
        image = r.FILES.get('image')
        book.image = image

        print(image)
        book.save()

        return redirect(to='insert')

    cat = Category.objects.all()
    data = {'data': cat}
    return render(r,'insertpage.html',data)

def insertcategory(r):
    if r.method == "POST":
        cat = Category()
        cat.cat_title = r.POST.get('cat_title')
        cat.cat_description = r.POST.get('cat_description')
        cat.save()

        return redirect(to='insert')
        
def singlecat(r,id):
    cat = Category.objects.all()

    book = Books.objects.filter(category=id)
    category = Category.objects.get(pk = id)
    data = {'book':book,'cat':cat,'catdata':category}
    return render(r,'index.html',data)

def searchbook(r):
    cat = Category.objects.all()
    title = r.POST.get('search')
    book = Books.objects.filter(Q(title__contains=title) | Q(isbn = title) | Q(author__contains = title))
    data = {'book':book,'cat':cat}
    return render(r,'index.html',data)

def singlepage(r,id):

    cat = Category.objects.all()
    book = Books.objects.get(pk = id)
    data = {'cat':cat,'book':book}
    return render(r,'viewpage.html',data)