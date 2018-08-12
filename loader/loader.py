from apscheduler.schedulers.blocking import BlockingScheduler

from source import WebSource
from moviebase import MovieBase


def data_refreshing():

    urls_from_kinopoisk = []
    pattern = 'https://www.kinopoisk.ru/afisha/new/city/3/page/{}/'
    i = 0
    while True:

        url = pattern.format(str(i))
        part = WebSource(url).get_links()

        if part:
            urls_from_kinopoisk.extend(part)
            i += 1
            continue
        else:
            break
   
    urls_from_mybase = MovieBase().get_urls()
    old_urls = [url for url in urls_from_mybase if url not in urls_from_kinopoisk]

    for url in old_urls:
        MovieBase().remove_movies(url)

    movies = []
    new_urls = [url for url in urls_from_kinopoisk if url not in urls_from_mybase]

    for url in new_urls[:3]:
        movies.append(WebSource(url).get_info_about_movie(url)qex)

    MovieBase().add_movies(movies)


if __name__  == '__main__':

    scheduler = BlockingScheduler()
    scheduler.add_job(data_refreshing,
                     'cron',
                      day_of_week='mon-sun',
                      hour=6, minute=8)
    scheduler.start()
