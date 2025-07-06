"""
listings/serializers.py
-----------------------
Turns Listing model instances into JSON (and back) for REST endpoints.
"""

from rest_framework import serializers
from .models import Listing
class ListingSerializer(serializers.ModelSerializer):
    """Simple ModelSerializer exposing *all* model fields."""
    
    class Meta:
        model = Listing
        fields = "__all__"   # Explicit list is safer for bigger projects.

