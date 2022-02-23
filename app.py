# -*- coding: utf-8 -*-
from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from flask_cors import CORS

from db_connect import db
import config
    
def create_app():
    app = Flask(__name__)
    CORS(app)
    
    from apis.auth.authResolver import Auth
    from apis.liquor.liquorResolver import Liquor

    app.config.from_object(config)  # config 에서 가져온 파일을 사용합니다.

    db.init_app(app)  # SQLAlchemy 객체를 app 객체와 이어줍니다.
    Migrate().init_app(app, db)
    
    app.secret_key = config.SECRET_KEY #.env 사용
    app.config['SESSION_TYPE'] = 'filesystem' #Redis대신 filesystem사용

    # from . import models
    api = Api(app)
    api.add_namespace(Auth, '/auth')
    api.add_namespace(Liquor, '/liquor')
    
    return app

if __name__ == "__main__":
    create_app().run(host='0.0.0.0', debug=True, )
