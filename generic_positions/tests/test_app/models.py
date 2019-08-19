"""Dummy models to be used in test cases of the ``fields_positions`` app."""
from django.contrib.contenttypes import fields
from django.db import models


class DummyParentModel(models.Model):
    """Dummy to be used in test cases of the ``fields_positions`` app."""
    name = models.CharField(max_length=256, blank=True)

    fields_position = fields.GenericRelation(
        'fields_positions.ObjectPosition'
    )

    def __str__(self):
        return self.name


class DummyModel(models.Model):
    """Dummy to be used in test cases of the ``fields_positions`` app."""
    name = models.CharField(max_length=256, blank=True)
    parent = models.ForeignKey(DummyParentModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# We are just monkeypatching here for testing purposes. Of course you would add
# the GenericRelation directly to your model if it is part of your own app.
# The monkeypatching will only be used for models of third party apps.
DummyModel.add_to_class(
    'fields_position',
    fields.GenericRelation('fields_positions.ObjectPosition'),
)
