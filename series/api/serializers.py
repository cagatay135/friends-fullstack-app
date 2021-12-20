from rest_framework import serializers
from series.models import Character, Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    quotes = QuoteSerializer(many=True)
    class Meta:
        model = Character
        fields = ['id','url', 'name','nickname','most_used_word','gender','number_episode','portrayed_by','date_of_birth','image','quotes']

