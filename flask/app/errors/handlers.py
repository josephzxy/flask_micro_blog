from app import db
from app.errors import bp

from flask import render_template

@bp.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@bp.errorhandler(500)
def internel_error(error):
    db.session.rollback()
    return render_template('500.html'), 500