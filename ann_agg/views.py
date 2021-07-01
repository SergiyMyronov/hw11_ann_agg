from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Author, Book, Publisher, Store


def index(request):
    return HttpResponse("Hello, world. You're at the Annotate-Aggregate index.")


def author(request):
    authors = Author.objects.all()
    return render(request, 'ann_agg/author.html', {'authors': authors})


def book(request):
    books = Book.objects.all()
    return render(request, 'ann_agg/book.html', {'books': books})


def book_details(request, num):
    bk = get_object_or_404(Book, id=num)
    return render(request, "ann_agg/book_details.html", {"bk": bk})


def pub(request):
    pubs = Publisher.objects.all()
    return render(request, 'ann_agg/pub.html', {'pubs': pubs})


def store(request):
    stores = Store.objects.all()
    return render(request, 'ann_agg/store.html', {'stores': stores})
