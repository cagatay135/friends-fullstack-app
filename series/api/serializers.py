from rest_framework import serializers
from series.models import Character, Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    quotes = QuoteSerializer(many=True, read_only=True)
    class Meta:
        model = Character
        fields = ['id','url', 'name','nickname','most_used_word','gender','number_episode','portrayed_by','date_of_birth','image','quotes']








"""
class CharacterSerializer(serializers.Serializer):
    url = serializers.HyperlinkedRelatedField(view_name="character-detail" , read_only=True)
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    gender = serializers.CharField()
    number_episode = serializers.IntegerField()
    portrayed_by = serializers.CharField()
    date_of_birth = serializers.DateField()
    image = serializers.ImageField(max_length=None, use_url=True)

    def create(self, validated_data):
        return Character.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.number_episode = validated_data.get('number_episode', instance.number_episode)
        instance.portrayed_by = validated_data.get('portrayed_by', instance.portrayed_by)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.image = validated_data.get('image', instance.image)
        return instance.save()
"""
