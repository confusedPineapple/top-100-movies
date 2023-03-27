from bs4 import BeautifulSoup
import requests

#This is the website where the top 100 movies are gotten from
WEBSITE = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

#The requests page is used to communicate with the website and the response is saved
response = requests.get(WEBSITE)

#From the response obtained, the html data is saved into variable 'movies_page'
movies_page = response.text

#We then make soup from our movies page data with Beautiful Soup!
soup = BeautifulSoup(movies_page,'html.parser')

#We obtaine the title tag data by accessing the name and class where it exists
movies_title_tags = soup.find_all(name='h3', class_ = 'title')

#An empty list is created to hold all of the movie titles
movie_titles = []

#A loop is created to obtain each movie title and append to the movie_titles list
for title in movies_title_tags:
    movie_titles.append(title.get_text())

#Since the data is ordered from 100-1 instead of 1-100,
#We reverse the list
reversed_list = (list(reversed(movie_titles)))

#A new file is then created and data from the reversed list is written into
#the new file called 'movies.txt'
with open('movies.txt','w',encoding="utf-8") as file:
    for i in reversed_list:
        file.write(f'{i}\n')
