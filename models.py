from app import db


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column('id', db.Integer, primary_key=True)
    name_rus = db.Column('name_rus', db.String)
    name_eng = db.Column('name_eng', db.String)
    year = db.Column('year', db.Integer)
    genres = db.Column('genres', db.String)
    countries = db.Column('countries', db.String)
    directors = db.Column('directors', db.String)
    writers = db.Column('writers', db.String)
    rus_prem = db.Column('rus_prem', db.String(20))
    url = db.Column('url', db.String, unique=True)

    def to_json(self):
        return {
            'name_rus': self.name_rus,
            'name_eng': self.name_eng,
            'year': self.year,
            'genres':self.genres, 
            'countries': self.countries, 
            'directors': self.directors,
            'writers': self.writers,
            'rus_prem': self.rus_prem,
            'url':self.url 
        }