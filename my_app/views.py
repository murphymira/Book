from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from my_app.models import Book, Publisher
from my_app.serializer import BookSerializer, PublisherSerializer


# # Create your views here.
# import Books
# from first_app.models import Book, Publisher
#
#
# def index(request):
#     name = "damilola"
#     return render(request, 'index.html', context={"name": name})
#
#
# def redirect(request):
#     return HttpResponseRedirect(reverse('first_app:hello'))
#
#
# def hello(request, name: str, num: int):
#     return HttpResponse(f"<h1>Hello {num}. {name.title()}, Welcome to Django</h1>")
#
#
# # Create your views here.
#
#
# def book_list(request):
#     with transaction.atomic():
#         p1 = Publisher.objects.create(name="thug")
#         b1 = Book.objects.create(title="")
#         books = Book.objects.raw()
#     return render(request, 'first_app/book-list.html', {'books': list(books)})
#
#
# def book_detail(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#         return render(request, '/book-details.html', {'book': book})
#     except Book.DoesNotExist:
#         return HttpResponse("Book does not exist")
#     # OR
#     # book = get_object_or_404(Book, pk=pk)
#     # return render(request, 'my_app/book-detail.html', {'book': book})
#
#
# def book_list_for_fiction(request):
#     books = Book.objects.filter(genre='FICTION')
#     return render(request, 'first_app/book-list-fiction.html', {'books': list(books)})
#
#
# def book_list_for_price(request):
#     books = Book.objects.filter(price__lt=80)
#     return render(request, 'first_app/book-list-price.html', {'books': list(books)})
#

class BookList(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetail(APIView):
    def get(self, request):
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def put(self, request):
        book = get_object_or_404(Book)
        serializer = BookSerializer(book, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        query_set = Book.objects.all()
        serializer = BookSerializer(query_set, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def book_detail(request, pk):
    # try:
    # book = Book.objects.get(isbn=pk)
    book = get_object_or_404(Book, isbn=pk, context={'request': request})
    if request.method == 'GET':
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)
    elif request.method == ('PUT', 'PATCH'):
        serializer = BookSerializer(book, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # except Book.DoesNotExist:
    # return Response('error: could not find resource', status=status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST"])
def publisher_list(request):
    if request.method == "GET":
        query_set = Publisher.objects.all()
        serializer = PublisherSerializer(query_set, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = PublisherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, isbn=pk, context={'request': request})
    if request.method == 'GET':
        serializer = PublisherSerializer(publisher, context={'request': request})
        return Response(serializer.data)
    elif request.method == ('PUT', 'PATCH'):
        serializer = PublisherSerializer(publisher, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)