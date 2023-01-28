from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Comments


@registry.register_document
class CommentDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'elastic_comments'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Comments  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'email',
            'body',
        ]


