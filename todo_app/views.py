# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Movie, Rating
# from .serializers import MovieSerializer, RatingSerializer

# @api_view(['POST'])
# def create_movie(request):
#     serializer = MovieSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_movie(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#         serializer = MovieSerializer(movie)
#         data = serializer.data
#         return Response(data, status=status.HTTP_200_OK)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
# @api_view(['POST'])
# def create_rating(request):
#         serializer = RatingSerializer(data=request.data)
#         if serializer.is_valid():
#             rating_value = serializer.validated_data['value']
#             if 1 <= rating_value <= 5:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(
#                 {"value": "Rating must be between 1 and 5"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer

class CreateMovieView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetMovieView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            movie = Movie.objects.get(id=id)
            serializer = MovieSerializer(movie)
            data = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class CreateRatingView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            rating_value = serializer.validated_data['value']
            if 1 <= rating_value <= 5:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"value": "Rating must be between 1 and 5"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
