from .media_mutation import MediaCreateUpload, MediaCreateUrl
import graphene


class MediaMutation(graphene.ObjectType):
    create_media_upload = MediaCreateUpload.Field()
    create_media_url = MediaCreateUrl.Field()