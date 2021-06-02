from flask import Blueprint
from methods import one_image
from . import is_api


one_image_blueprint = Blueprint('One_image', __name__)


@one_image_blueprint.route('/upload', methods=['POST'])
@is_api(required_keys=['base64_str', 'extension'])
def upload_img(data):
    status, message = one_image.upload_one_img(**data)

    if not status:
        return {'error': message}, 500

    else:
        return {'success': True}, 200


@one_image_blueprint.route('/<int:img_num>', methods=['GET'])
@is_api()
def get_img(data, img_num):
    status, result = one_image.get_one_img(img_num)

    if not status:
        return {'error': 'no_images'}, 404

    else:
        return result
