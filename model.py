from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from flask.views import MethodView


USER_COLS = ["id", "email", "password", "age"]

engine = create_engine("sqlite:///ratings.db", echo=False)
# Base.metadata.create_all(engine)
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

Base = declarative_base()
Base.query = session.query_property()


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key = True)
    email = Column(String(64), nullable=True)
    password = Column(String(64), nullable=True)
    age = Column(Integer, nullable=True)

    def __init__(self, email = None, password = None, age=None):
        self.email = email
        self.password = password
        self.age = age

class Rating(Base):
    __tablename__ = "Ratings"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    recipient_id = Column(Integer, nullable = True)
    star1 = Column(Integer, nullable = True)
    text1 = Column(String(150), nullable=True)
    star2 = Column(Integer, nullable = True)
    text2 = Column(String(150), nullable=True)
    star3 = Column(Integer, nullable = True)
    text3 = Column(String(150), nullable=True)

    def __init__(self, user_id, recipient_id, star1, text1, star2, text2, star3, text3):

        self.user_id = user_id
        self.recipient_id = recipient_id
        self.star1 = star1
        self.text1 = text1
        self.star2 = star2
        self.text2 = text2
        self.star3 = star3
        self.text3 = text3

class Feedback(Base):
    __tablename__ = "Feedback"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer)
    rater_id = Column(Integer)
    star1 = Column(Integer, nullable = True)
    text1 = Column(String(150), nullable=True)
    star2 = Column(Integer, nullable = True)
    text2 = Column(String(150), nullable=True)
    star3 = Column(Integer, nullable = True)
    text3 = Column(String(150), nullable=True)

    def __init__(self, user_id, rater_id, star1, text1, star2, text2, star3, text3):

        self.user_id = user_id
        self.rater_id = rater_id
        self.star1 = star1
        self.text1 = text1
        self.star2 = star2
        self.text2 = text2
        self.star3 = star3
        self.text3 = text3

def new_user(email, password, age):          
    session.add(User(email, password, age))
    session.commit()

# recipient_id taken out in session & paramenters
def new_rating(user_id, recipient_id, star1, text1, star2, text2, star3, text3):
    session.add(Rating(user_id, recipient_id, star1, text1, star2, text2, star3, text3))
    session.commit()

def feedback(user_id, rater_id, star1, text1, star2, text2, star3, text3):
    session.add(Feedback(user_id, rater_id, star1, text1, star2, text2, star3, text3))
    session.commit()


def make_user(row):
    fields = ["id", "email", "password", "username"]
    return dict(zip(fields, row))

# def new_rating(user_id, recipient_id, q1, feed1, q2, feed2, q3, feed3):
#     session.add(Ratings(user_id, recipient_id, q1, feed1, q2, feed2, q3, feed3))
#     session.commit()


def insert_into_table(db, table, columns, values):
    c = db.cursor()
    query_template = """INSERT into %s values (%s)"""
    num_cols = len(columns)
    q_marks = ", ".join(["NULL"] + (["?"] * (num_cols-1)))
    query = query_template%(table, q_marks)
    res = c.execute(query, tuple(values))
    if res:
        db.commit()
        return res.lastrowid

def get_profile():
    pass


def main():
    pass

if __name__ == "__main__":
    main()