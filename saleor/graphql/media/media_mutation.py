import graphene
from ..core.types import SeoInput, Upload
from django.core.files.storage import default_storage

class MediaCreateUpload(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)

    success = graphene.Boolean()

    def mutate(self, info, file, **kwargs):
        print(file)
        return MediaCreateUpload(success=True)

class MediaCreateUrl(graphene.Mutation):
    class Arguments:
        url = graphene.String(required=True)
    success = graphene.Boolean()

    def mutate(self, info, url, **kwargs):
        print(url)
        return MediaCreateUrl(success=True)