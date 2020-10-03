import requests
import re
from bs4 import BeautifulSoup
import csv

# 시작 코드 010001
# 끝 코드 196811

with open('data.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['title', 'genre', 'director']
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for i in range(10001, 196811):
        response = requests.get(
            f'https://movie.naver.com/movie/bi/mi/basic.nhn?code={i}')

        soup = BeautifulSoup(response.text, 'html.parser')

        movies_list = soup.select(
            'body>#wrap>#container>#content > .article > .mv_info_area > .mv_info')

        for movie in movies_list:
            title = movie.select_one('.h_movie > a')
            genre = movie.select_one(
                '.info_spec> dd:nth-of-type(1) > p > span')
            director = movie.select_one('.info_spec> dd:nth-of-type(2) > p')

            movie_title = title.text
                       
            if re.search('genre',str(genre)) is not None:
                movie_genre = re.sub(',', ' ', genre.text).split()
            else:
                movie_genre = ''

            if re.search('director',str(genre)) is not None:
                movie_director = director.text
            else:
                movie_director = ''                    

            movie_data = {
                'title': movie_title,
                'genre': movie_genre,
                'director': movie_director
            }
            w.writerow(movie_data)
           
