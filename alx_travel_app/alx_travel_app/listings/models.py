"""
listings/models.py
------------------
Defines database tables for the *listings* app.

One Listing == one travel experience / package.
"""

from django.db import models

class Listing(models.Model):
    # Short name shown in list views, admin, etc.
    title = models.CharField(max_length=255)

    # Longer marketing description shown on detail pages.
    description = models.TextField()

    # City / country, or resort name (free text keeps us flexible for now).
    location = models.CharField(max_length=255)

    # Price per traveller OR per package – we’ll refine later.
    # max_digits=10 allows values up to 9 999 999.99.
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Timestamp automatically set on creation.  Use this for ordering queries.
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self) -> str:
        """Human‑readable representation in Django admin and shell."""
        return self.title