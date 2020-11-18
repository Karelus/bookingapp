class Config:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://karel:password@localhost/booking'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
