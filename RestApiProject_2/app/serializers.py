from rest_framework import serializers
from .models import Book, BookNo, BookType, Author


class BookNoSerialzier(serializers.ModelSerializer):
    class Meta:
        model = BookNo
        fields = '__all__'


class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields = ['type']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    # this var will make One To One relation
    number = BookNoSerialzier(many=False)
    # this var will make One TO Many relation and need to be as model related_name
    booktype = BookTypeSerializer(many=True)
    # this var will make Many TO Many relation
    Author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['title', 'description', 'price', 'published', 'is_published', 'cover', 'number', 'booktype',
                  'Author']
