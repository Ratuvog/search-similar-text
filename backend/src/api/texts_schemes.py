from marshmallow import Schema, fields


class AddTextSchema(Schema):
    text = fields.Str(required=True)


class SentenceSchema(Schema):
    id = fields.Integer(dump_only=True)
    text_id = fields.Integer(dump_only=True)
    sentence = fields.String()


class TextSchema(Schema):
    id = fields.Integer(dump_only=True)
    text = fields.String()
    sentences = fields.Nested(SentenceSchema, many=True)


class SearchResultSchema(Schema):
    text_id = fields.Integer()
    score = fields.Float()

