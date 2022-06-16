from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


class Meal(base):
    __tablename__ = "MealPrepp"
    day = Column(Integer, primary_key=True)
    weekday = Column(String)
    meal = Column(String)
    type = Column(String)
    need_to_shop = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

monday = Meal(
    day=1,
    weekday="Monday",
    meal="Fishsoup",
    type="Lunch",
    need_to_shop="Fish, Fishstock, selleriac"
)

mondayD = Meal(
    day=2,
    weekday="Monday",
    meal="Meatballs",
    type="Dinner",
    need_to_shop="Cream"
)

tuesday = Meal(
    day=3,
    weekday="Tuesday",
    meal="Fishsoup",
    type="Lunch",
    need_to_shop="Fish, Fishstock, selleriac"
)

tuesdayD = Meal(
    day=4,
    weekday="Tuesday",
    meal="Meatballs",
    type="Dinner",
    need_to_shop="Cream"
)

# session.add(monday)
# session.add(mondayD)
# session.add(tuesday)
# session.add(tuesdayD)

# session.commit()

meals = session.query(Meal)
for meal in meals:
    print(
        meal.weekday + " " +
        meal.type,
        meal.meal,
        meal.need_to_shop,
        sep=" | "
        )
        