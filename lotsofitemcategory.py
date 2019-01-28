from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///catalog.db',
                       connect_args={'check_same_thread': False})

# Bind the above engine to a session.
Session = sessionmaker(bind=engine)

# Create a Session object.
session = Session()

user1 = User(
    name='Maro Ashraf',
    email='maramashraf7@gmail.com',
    picture='https://img.com/sdf'
)

session.add(user1)
session.commit()

# --------------------------------Add category ---------------------------
category1 = Category(
    name='Football',
    user=user1
)

session.add(category1)
session.commit()

category2 = Category(
    name='soccer',
    user=user1
)

session.add(category2)
session.commit()

category3 = Category(
    name='Baseball',
    user=user1
)

session.add(category3)
session.commit()


# ---------------------------------------Items --------------------------

item1 = Item(
    name='Bat',
    description='It is an exciting bat for basketball players \
    you will feel awsome after using it ',
    category=category3,
    user=user1
)

session.add(item1)
session.commit()

item2 = Item(
    name='Bat',
    description='Premium Quality Childrens Safety Goggles\
     you will feel awsome after using it ',
    category=category1,
    user=user1
)

session.add(item2)
session.commit()

item3 = Item(
    name='foot ball',
    description='Premium Quality ball you will feel awsome after using it ',
    category=category1,
    user=user1
)

session.add(item3)
session.commit()


print('Finished populating the database!')
