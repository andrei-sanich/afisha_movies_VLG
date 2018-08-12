from sqlalchemy import Column, String, Integer

from base import Base


class Movie(Base):
    __tablename__ = 'moviesaaa'

    id = Column(Integer, primary_key=True)
    name_rus = Column(String)
    name_eng = Column(String)
    year = Column(Integer)
    genres = Column(String)
    countries = Column(String)
    directors = Column(String)
    writers = Column(String)
    rus_prem = Column(String(20))
    url = Column(String, unique=True)

    def __init__(self, name_rus, name_eng, year,
                 genres, countries, directors,
                 writers, rus_prem, url):
        self.name_rus = name_rus
        self.name_eng = name_eng
        self.year = year
        self.genres = genres
        self.countries = countries
        self.directors = directors
        self.writers = writers
        self.rus_prem = rus_prem
        self.url = url
