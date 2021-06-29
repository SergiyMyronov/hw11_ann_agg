import random
from datetime import datetime, timedelta

from ann_agg.models import Author, Book, Publisher, Store

from django.core.management.base import BaseCommand

import pandas


class Command(BaseCommand):
    """
    This command is for inserting Author, Publisher, Book, Store into database.
    Inserts all unique Authors, Publishers and Stores. Then inserts 100 Books.
    """

    help = 'Loading some data from file Title_List.xlsx'  # noqa

    def handle(self, *args, **kwargs):
        Author.objects.all().delete()
        Publisher.objects.all().delete()
        Book.objects.all().delete()
        Store.objects.all().delete()

        all_data = pandas.read_excel('Title_List.xlsx')
        excel_data = all_data.sample(frac=0.2)

        auth_col = excel_data['Author'].unique()
        authors = []
        for i in range(len(auth_col)):
            authors.append(Author(name=auth_col[i], age=random.randint(30, 85)))

        Author.objects.bulk_create(authors)

        pub_col = excel_data['Book Type'].unique()
        pubs = []
        for i in range(len(pub_col)):
            pubs.append(Publisher(name=pub_col[i] + ' Publisher'))

        Publisher.objects.bulk_create(pubs)

        st_col = excel_data['Subject Category'].unique()
        stores = []
        for i in range(len(st_col)):
            stores.append(Store(name=st_col[i] + ' Store'))

        Store.objects.bulk_create(stores)

        books = []
        for idx, row in excel_data.iterrows():
            dt = datetime.strptime(row['Expected Pub Date'], '%b-%y')
            if dt.year >= 2021:
                dt -= timedelta(days=730)
            b1 = Book(name=row['Title'],
                      pages=random.randint(100, 700),
                      price=round(random.randint(100, 700) / random.randint(2, 8), 2),
                      rating=round(random.randint(8, 20) / random.randint(2, 5), 1),
                      publisher=Publisher.objects.get(name=row['Book Type'] + ' Publisher'),
                      pubdate=dt,
                      )
            books.append(b1)
        Book.objects.bulk_create(books)

        for idx, row in excel_data.iterrows():
            b1 = Book.objects.get(name=row['Title'])
            b1.authors.add(Author.objects.get(name=row['Author']))
