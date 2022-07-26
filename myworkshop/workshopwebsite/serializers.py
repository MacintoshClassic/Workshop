from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car  # this is the model that is being serialized
        fields = ("number", "model", "year")


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("name", "phone")


class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = ("name", "phone")


class OrderInitialDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInitialDetails
        fields = (
            "client",
            "car",
            "mechanic",
            "issue_description",
            "price",
            "beginning_date",
            "finishing_date",
            "repair",
        )


class OrderAdditionalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAdditionalDetails
        fields = (("discount"),)
