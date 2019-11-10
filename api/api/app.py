from flask import abort, jsonify, Flask, request
from marshmallow import ValidationError

from api.database import get_pikabu_posts
from api.schemas import article_schema, request_params_schema


app = Flask(__name__)


@app.route('/articles')
def articles():
    """
    Endpoint for articles
    """
    try:
        args = request_params_schema.load(request.args)
    except ValidationError as e:
        abort(400, e.messages)

    articles = get_pikabu_posts(
        limit=args.get('limit', 0),
        offset=args.get('offset', 0),
    )
    return jsonify(article_schema.dump(articles))
