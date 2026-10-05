import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021,
      "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
       "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020,
      "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024,
      "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118,
       "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# ЭТАП 1
def average_rating(movies):
    total = 0
    for movie in movies:
        total += movie['rating']
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = []
    for movie in movies:
        ages.append(current_year - movie['year'])
    return (max(ages), min(ages), math.ceil(sum(ages) / len(ages)))


def duration_in_hours(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f'{hours}ч {mins}м'


# ЭТАП 2
def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# ЭТАП 3
for movie in movies:
    if 'comedy' in movie['genres']:
        continue
    print(movie['title'])


i = 0
r = 0
while i < len(movies):
    r = movies[i]['rating']
    if r > 9:
        print(movies[i]['title'])
        break
    i += 1
else:
    print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie['duration_min'] > threshold:
            count += 1
    return count


# ЭТАП 4
def normalize_title(title):
    words = title.split()
    result = []
    for word in words:
        result.append(word[0].upper() + word[1:])
    return " ".join(result)


def make_slug(title):
    return title.lower().replace(" ", "-") 


def format_report_line(movie):
    return (
        f'"{movie["title"]}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, '
        f'{duration_in_hours(movie["duration_min"])}, '
        f'жанры: {", ".join(sorted(movie["genres"]))}'
)


# ЭТАП 5
def titles_sorted_by_rating(movies):
    sorted_movies = sorted(
        movies, key=lambda movie: movie['rating'], reverse=True
    )
    new = []
    for movie in sorted_movies:
        new.append(movie['title'])
    return new


def top_n_by_rating(movies, n=3):
    top_movies = sorted(
        movies, key=lambda movie: movie['rating'], reverse=True
    )
    top = []
    for movie in top_movies[:n]:
        top.append((movie['title'], movie['rating']))
    return top


# ЭТАП 6
def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts

def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography.setdefault(actor, []).append(movie["title"])
    return filmography

def above_average(movies):
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}


#ЭТАП 7
def all_genres(movies):
    genres = set()
    for movie in movies:
        genres.update(movie["genres"])
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    genres_a = set()
    genres_b = set()
    for movie in movies_a:
        genres_a.update(movie["genres"])
    for movie in movies_b:
        genres_b.update(movie["genres"])
    return genres_a - genres_b