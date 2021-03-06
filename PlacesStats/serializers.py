import datetime
from rest_framework import serializers
from PlacesStats.models import PlaceStats, AcceptStats, RatingStats


class PlaceStatsSerializer(serializers.ModelSerializer):
    """
    Сериализватор для статы по местам
    """
    action = serializers.ChoiceField(choices=PlaceStats.ACTION_CHOICES)
    place_id = serializers.IntegerField(min_value=1)
    user_id = serializers.IntegerField(min_value=1, allow_null=True)

    class Meta:
        model = PlaceStats
        fields = [
            'id',
            'action',
            'place_id',
            'user_id',
            'action_dt',
        ]

    def validate(self, attrs):
        attrs = super().validate(attrs)
        if attrs['action'] in PlaceStats.action_statuses_for_registered_user() and attrs['user_id'] is None:
            raise serializers.ValidationError('Поле "user_id" может быть null только при действии OPENED')
        return attrs

    def create(self, validated_data):
        new = PlaceStats.objects.create(**validated_data)
        return new

    def update(self, instance, validated_data):
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        return instance


class AcceptStatsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для статы по подтверждениям
    """
    action = serializers.ChoiceField(choices=AcceptStats.ACTION_CHOICES)
    place_id = serializers.IntegerField(min_value=1)
    user_id = serializers.IntegerField(min_value=1)

    class Meta:
        model = AcceptStats
        fields = [
            'id',
            'action',
            'user_id',
            'place_id',
            'action_dt',
        ]

    def create(self, validated_data):
        new = AcceptStats.objects.create(**validated_data)
        return new

    def update(self, instance, validated_data):
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        return instance


class RatingStatsSerializer(serializers.ModelSerializer):
    """
    Сериализатор статы по рейтингу
    """
    place_id = serializers.IntegerField(min_value=1)
    user_id = serializers.IntegerField(min_value=1)
    old_rating = serializers.IntegerField(min_value=0, max_value=5)
    new_rating = serializers.IntegerField(min_value=0, max_value=5)

    class Meta:
        model = RatingStats
        fields = [
            'id',
            'place_id',
            'user_id',
            'old_rating',
            'new_rating',
            'action_dt',
        ]

    def create(self, validated_data):
        new = RatingStats.objects.create(**validated_data)
        return new

    def update(self, instance, validated_data):
        for attr, val in validated_data.items():
            setattr(instance, attr, val)
        instance.save()
        return instance
