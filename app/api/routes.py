from flask import current_app, Response

from app.api import bp as api_bp
from app import db

@api_bp.route('/user-avatar/<email_md5>')
def user_avatar(email_md5):
    user_avatar_dir = current_app.config['USER_AVATAR_DIR']
    user_avatar_path = user_avatar_dir + email_md5 + '.png'
    img = open(user_avatar_path, 'rb')
    resp = Response(img, mimetype="image/png")
    return resp