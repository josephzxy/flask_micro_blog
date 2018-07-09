
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'cabMTFn1'

    DB_TYPE = 'mysql'
    DB_DRIVE = 'pymysql'

    db_conn_args = {
        'username': 'flask',
        'password': 'flask',
        'host': 'localhost',
        'port': 3306,
        'db_name': 'flask_blog_db',
        'charset': 'utf8mb4'
    }

    SQLALCHEMY_DATABASE_URI = '{db_type}+{db_drive}://{username}:{password}@{host}:{port}/{db_name}?charset={charset}'\
    .format(
        db_type=DB_TYPE,
        db_drive=DB_DRIVE,
        username=db_conn_args.get('username'),
        password=db_conn_args.get('password'),
        host=db_conn_args.get('host'),
        port=db_conn_args.get('port'),
        db_name=db_conn_args.get('db_name'),
        charset=db_conn_args.get('charset')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = Config()
print(config.SQLALCHEMY_DATABASE_URI)
