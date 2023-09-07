from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    # rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields ='__all__'
        
    def to_representation(self, instance):
        data =  super().to_representation(instance)
        ratings = instance.ratings.all()
        data['rating'] =  sum(rating.value for rating in ratings)/len([rating.value for rating in ratings]) if ratings else None
        return data
    
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        