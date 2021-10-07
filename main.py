from bs4 import BeautifulSoup

# Getting Data from the website. (The original website does not allow for webscraping anymore, so i'm using a local
# HTML version of it).
with open("100-movies.html") as file:
    movies = file.read()

# Parsing the content
soup = BeautifulSoup(movies, "html.parser")

# Finding all movie titles.
movie = [i.getText() for i in soup.find_all(name='h3', class_='jsx-2692754980')]

# Reformatting the movies into a TXT editor.
with open("movies.txt", "w") as file:
    file.write("\n".join(movie))
