from rest_framework import serializers

from my_app.models import Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'email', 'url']


class BookSerializer(serializers.ModelSerializer):  # noqa
    book_title = serializers.CharField(max_length=255, source='title')

    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Publisher.objects.all(),
    #     view_name='first_app:publisher-detail'
    # )

    class Meta:
        model = Book
        fields = ['book_title', 'description', 'isbn', 'price', 'publisher']
        # exclude = ['date_published', 'genre']
