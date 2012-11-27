from dateutil import parser
import model
import csv
import time

def load_users(session):
    with open('seed_data/u.user') as csvfile:
        user_raw_data=csv.reader(csvfile, delimiter='|')
        for row in user_raw_data:
            age=row[1]
            email=None
            password=None

            new_user=model.User(email, password, age)
            session.add(new_user)
            session.commit()

# def load_movies(session):
#     with open('seed_data/u.item') as csvfile:
#         item_raw_data=csv.reader(csvfile, delimiter='|')
#         for row in item_raw_data:
#             title=row[1]
#             released_at=row[2]
#             imdb_url=row[4]

#             formatted_date=parser.parse(released_at)
#             formatted_title = title.decode("latin_1")

#             new_item=model.Movie(formatted_title, formatted_date, imdb_url)
#             session.add(new_item)
#             session.commit()

# def load_ratings(session):
#     with open('seed_data/u.data') as csvfile:
#         rating_raw_data=csv.reader(csvfile, dialect="excel-tab")
#         for row in rating_raw_data:
#             user_id=row[0]
#             movie_id=row[1]
#             rating=row[2]

#             new_rating=model.Rating(movie_id, user_id, rating)
#             session.add(new_rating)
#             session.commit()

def main(session):
    #load_users(session)
    #load_movies(session)
    load_ratings(session)

if __name__ == "__main__":
    s= model.connect()
    main(s)