class Configuration(object):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1@localhost:5432/movies'
	SQLALCHEMY_TRACK_MODIFICATIONS = False