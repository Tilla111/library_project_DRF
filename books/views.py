from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Books
from .serializers import BooksSerializer
from rest_framework import generics, status


# class BookListApiView(generics.ListAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BookListApiView(APIView):

    def get(self, request):
        books = Books.objects.all()
        serializer_data = BooksSerializer(books, many=True).data
        data = {
            'status': f"Returned {len(books)} books",
            'books': serializer_data
        }

        return Response(data)


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer


class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            # Attempt to retrieve the book
            book = Books.objects.get(pk=pk)

            # Serialize the book data
            serializer_data = BooksSerializer(book).data

            # Prepare the response data
            data = {
                'book': serializer_data
            }

            return Response(data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            # Handle the case where the book does not exist
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Handle other unexpected exceptions
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BookDeleteApiView(APIView):

    def delete(self, request, pk):
        try:
            # Attempt to retrieve the book
            book = Books.objects.get(pk=pk)

            # Serialize the book data before deleting it
            serializer_data = BooksSerializer(book).data

            # Delete the book
            book.delete()

            # Prepare the response data
            data = {
                'book': serializer_data
            }

            return Response(data, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            # Handle the case where the book does not exist
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Handle other unexpected exceptions
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BookUpdateApiView(APIView):

    def put(self, request, pk):
        try:
            book = Books.objects.get(pk=pk)
        except not Books:
            # Handle case where book with pk is not found
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Books.objects.all()
#     serializer_class = BooksSerializer

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BooksSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': "Successful",
                'message': "The book has been saved to the database.",
                'book': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        response_data = {
            'status': "Error",
            'message': "There was an error saving the book.",
            'errors': serializer.errors
        }
        return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookDetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

# @api_view(['GET'])
# def book_list_view(request, *args, **kwargs):
#     books = Books.objects.all()
#     serializer = BooksSerializer(books, many=True)
#     return Response(serializer.data)
