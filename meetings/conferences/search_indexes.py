import datetime
from haystack import indexes
from .models import Conference
from django.contrib.auth.models import User


class ConferenceIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=False)
    created = indexes.DateTimeField(model_attr='created')
    modified = indexes.DateTimeField(model_attr='modified')
    title = indexes.CharField(model_attr='title')
    city = indexes.CharField(model_attr='city')
    state = indexes.CharField(model_attr='state')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Conference

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(created__lte=datetime.datetime.now())