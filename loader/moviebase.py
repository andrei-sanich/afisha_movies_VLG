from base import Session, engine, Base
from movie import Movie


class MovieBase():

    def __init__(self):

#        Base.metadata.create_all(engine)
        self.s = Session()

    
    def get_urls(self):

        data = self.s.query(Movie.url).all()
        urls = [row[0] for row in data]
        return urls

    def remove_movies(self, url):

    	movie = self.s.query(Movie).filter(Movie.url == url).one()
    	self.s.delete(movie)
    	self.s.commit()

    def add_movies(self, movies):

        self.s.bulk_insert_mappings(Movie, movies)
        self.s.commit()
        self.s.close()
