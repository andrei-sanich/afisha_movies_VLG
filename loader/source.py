from bs4 import BeautifulSoup
from selenium import webdriver


class WebSource():
    
   
    def __init__(self, url):

        self.url = url
        self.driver = webdriver.PhantomJS()
        
    def get_links(self):

        self.driver.get(self.url)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        movies = soup.find_all('div', {'class': 'name'})
        links = ["https://www.kinopoisk.ru" + movie.find('a').get('href') for movie in movies]
        return links
       
    def get_info_about_movie(self, link):

        self.driver.get(self.url)
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        items = soup.find_all('div', {'id': 'content_block'})
        for item in items:
            name_rus = item.find('h1', {'class': 'moviename-big'}).text
            name_eng = item.find('span', {'itemprop': 'alternativeHeadline'}).text
        table = soup.find('table', {'class': 'info'})
        movie_year = int(table.find('td', {'class': 'type'}, text = u'год').nextSibling.nextSibling.text[:5])
        genres = [x.text for x in table.find('span', {'itemprop': 'genre'}).find_all('a')]
        countries = [x.text for x in table.find('td', {'class': 'type'}, text = u'страна').nextSibling.nextSibling.find_all('a')]
        directors = [x.text for x in table.find('td', {'itemprop': 'director'}).find_all('a')]
        writers = [x.text for x in table.find('td', {'class': 'type'}, text = u'сценарий').nextSibling.find_all('a')]
        rus_prem = table.find('td', {'id': 'div_rus_prem_td2'}).find('a').text
        info = {
                'name_rus': name_rus,
                'name_eng': name_eng,
                'year': movie_year,
                'genres': genres,
                'countries': countries,
                'directors': directors,
                'writers': writers,
                'rus_prem': rus_prem,
                'url': link
                }
        return info
