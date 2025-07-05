"""
listings/views.py
-----------------
Request handlers for the /api/listings/ endpoint.

We start with DRF’s generic class‑based views so we get CRUD quickly.
"""

from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer