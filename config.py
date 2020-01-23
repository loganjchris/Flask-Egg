import os
 
app_dir = os.path.abspath(os.path.dirname(__file__))
 
class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asdkj2oi90cm2nx'

class DevelopementConfig(BaseConfig):
    DEBUG = True
    #Database info changes between configs (Future)
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or  \
    #    'mysql+pymysql://root:pass@localhost/flask_app_db'
    
 
class TestingConfig(BaseConfig):
    DEBUG = True
        
 
class ProductionConfig(BaseConfig):
    DEBUG = False
    