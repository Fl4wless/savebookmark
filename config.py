import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass