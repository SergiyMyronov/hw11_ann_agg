from django.db.models import Avg, Count, Max, Min, Prefetch, Sum
from django.db.models.functions import Round
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Author, Book, Publisher, Store


def index(request):
    return HttpResponse("Hello, world. You're at the Annotate-Aggregate index.")


def author(request):
    authors = Author.objects.all()
    aut_stat = Author.objects.aggregate(cnt=Count('id'),
                                        max_age=Max('age'),
                                        min_age=Min('age'),
                                        avg_age=Avg('age'))
    return render(request, 'ann_agg/author.html', {'authors': authors, 'aut_stat': aut_stat})


def author_details(request, num):
    aut = get_object_or_404(Author, id=num)
    bk_aut = Book.objects.filter(authors=aut)
    return render(request, "ann_agg/author_details.html", {"bk": aut, "bk_aut": bk_aut})


def book(request):
    books = Book.objects.select_related('publisher').all()
    return render(request, 'ann_agg/book.html', {'books': books})


def book_details(request, num):
    bk = Book.objects.select_related('publisher').prefetch_related('authors').get(id=num)
    bk_aut = bk.authors.all()
    return render(request, "ann_agg/book_details.html", {"bk": bk, "bk_aut": bk_aut})


def pub(request):
    pubs = Publisher.objects.all()
    return render(request, 'ann_agg/pub.html', {'pubs': pubs})


def pub_details(request, num):
    pb = get_object_or_404(Publisher, id=num)
    books = Book.objects.filter(publisher=pb.id).aggregate(cnt=Count('id'),
                                                           max_price=Round(Max('price')),
                                                           min_price=Round(Min('price')),
                                                           sum_price=Round(Sum('price')))
    return render(request, "ann_agg/pub_details.html", {"bk": pb, "books": books})


def store(request):
    stores = Store.objects.annotate(cnt=Count('books'))
    return render(request, 'ann_agg/store.html', {'stores': stores})


def store_details(request, num):
    st = Store.objects.prefetch_related(
        Prefetch('books', queryset=Book.objects.filter(price__gt=100))).get(id=num)
    books = st.books.all()

    return render(request, "ann_agg/store_details.html", {"bk": st, "books": books})
