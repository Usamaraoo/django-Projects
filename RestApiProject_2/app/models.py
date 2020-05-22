from django.db import models


# this model is OneToOne connetion example
class BookNo(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=50, blank=False, unique=True)
    description = models.CharField(max_length=300, blank=True)

    price = models.IntegerField(default=0)
    published = models.DateField()
    is_published = models.BooleanField(default=False)

    cover = models.ImageField(upload_to='covers/', blank=True)

    # field for One To One connection
    number = models.OneToOneField(BookNo, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# this model is example of one to many relation
class BookType(models.Model):
    type = models.CharField(max_length=20)
    # connecting this model with the  Book a
    # related_name will help us to  show data in Book model in the API
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='booktype')
    
    
# this model class is example of Many to Many relation
class Author(models.Model):
    name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book,related_name='Author')
    
    def __str__(self):
        return self.name
