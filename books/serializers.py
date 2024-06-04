from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Books



class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = ('id','title', 'subtitle','content', 'author', 'isbn', 'price')


    def validate(self, data):
        title = data.get('title', None)
        isbn = data.get('isbn', None)

        #Check that the title consists of only letters
        if not title.isalpha():
            raise ValidationError(
                {
                    'status': False,
                    'massage': 'The title of the book must consist of letters'
                }
            )

        #Check title and isbn from database existence
        if Books.objects.filter(title=title,isbn=isbn).exists():
            raise ValidationError(
                {
                    'status': False,
                    'massage': 'You cannot upload books with the same title and ISBN'
                }
            )

        #Check if the price is greater than 0
    def validate_price(self, price):
        if price < 0 or price > 99999999:
            raise ValidationError(
                {
                    'status': False,
                    'massage': 'Wrong price'
                }
            )

        return data