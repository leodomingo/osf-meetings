# TODO: Write tests!
# -*- coding:utf-8 -*-

#Core Django imports
from django.test import TestCase

#Third-party app imports
from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

# Relative imports of the 'app-name' package
from .models import Conference

class ConferenceTestModel(TestCase):

    def setUp(self):
        """
        Set up all the tests
        """
        self.conf = mommy.make(Conference)
