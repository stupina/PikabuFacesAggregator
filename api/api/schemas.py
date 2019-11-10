from marshmallow import fields, Schema, validate

from api.settings import MAX_LIMIT


class ArcticleSchema(Schema):
    title = fields.Str()
    images_urls = fields.List(fields.URL())
    author = fields.Str()
    external_id = fields.Str()
    post_url = fields.URL()
    date = fields.DateTime()


article_schema = ArcticleSchema(many=True)


class RequestParamsSchema(Schema):
    offset = fields.Int(
        validate=validate.Range(min=0),
    )
    limit = fields.Int(
        validate=validate.Range(min=0, max=MAX_LIMIT),
    )


request_params_schema = RequestParamsSchema()
