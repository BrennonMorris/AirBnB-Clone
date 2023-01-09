from app.models import db, User
import random

profile_pictures = ['https://cdn-icons-png.flaticon.com/512/4681/4681664.png', 'https://cdn-icons-png.flaticon.com/512/4681/4681414.png', 'https://cdn-icons-png.flaticon.com/512/4681/4681611.png', 'https://cdn-icons-png.flaticon.com/512/4681/4681561.png', 'https://cdn-icons-png.flaticon.com/512/4681/4681691.png', 'https://cdn-icons-png.flaticon.com/512/4681/4681769.png', 'https://cdn-icons-png.flaticon.com/512/4681/4681741.png', 'https://cdn-icons-png.flaticon.com/512/4681/4681673.png', 'https://cdn-icons-png.flaticon.com/512/4681/4681538.png', 'https://cdn-icons-png.flaticon.com/512/4681/4681628.png']


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(email='demo@user.io', password="password", profile_pic=profile_pictures[random.randrange(len(profile_pictures))], first_name='Demo', last_name='User')
      # 2
    owner1 = User(email="email1@user.io",
                  password="password",
                  profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                  first_name="George",
                  last_name="Smith" 
                  )
      # 3
    owner6 = User(first_name='Brennon',
                  last_name='Morris',
                  profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                  email='brennonmorris@user.io',
                  password='password'
                  )
      # 4
    owner9 = User(first_name='Paul',
                  last_name='Smith',
                  profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                  email='email2@user.io',
                  password='password'
                  )
      # 5
    owner10 = User(first_name='Jake',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email3@user.io',
                   password='password'
                   )
      # 6
    owner14 = User(first_name='Jessie',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email4@user.io',
                    password='password'
                   )
      # 7
    owner15 = User(first_name='Marie',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email5@user.io',
                      password='password'
                   )
      # 8
    owner16 = User(first_name='John',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email6@user.io',
                    password='password'
                   )
      # 9
    owner17 = User(first_name='Alex',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email7@user.io',
                   password='password'
                   )
      # 10
    owner18 = User(first_name='Noah',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email8@user.io',
                   password='password'
                   )
      # 11
    owner19 = User(first_name='Kyle',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email9@user.io',
                   password='password'
                   )
      # 12
    owner20 = User(first_name='Michael',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email10@user.io',
                   password='password'
                   )
      # 13
    owner21 = User(first_name='Jeff',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email11@user.io',
                password='password'
                   )
      # 14
    owner22 = User(first_name='Sam',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email12@user.io',
                  password='password'
                   )
      # 15
    owner23 = User(first_name='Ted',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email13@user.io',
                     password='password'
                   )
      # 16
    owner25 = User(first_name='Amanda',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email14@user.io',
                   password='password'
                   )
      # 17
    owner26 = User(first_name='Luke',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email15@user.io',
                  password='password'
                   )
      # 18
    owner27 = User(first_name='Gary',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email16@user.io',
                password='password'
                   )
      # 19
    owner28 = User(first_name='Joe',
                   last_name='Smith',
                   profile_pic=profile_pictures[random.randrange(len(profile_pictures))],
                   email='email17@user.io',
                   password='password'
                   )


    db.session.add(demo)
    db.session.add(owner1)
    db.session.add(owner6)
    db.session.add(owner9)
    db.session.add(owner10)
    db.session.add(owner14)
    db.session.add(owner15)
    db.session.add(owner16)
    db.session.add(owner17)
    db.session.add(owner18)
    db.session.add(owner19)
    db.session.add(owner20)
    db.session.add(owner21)
    db.session.add(owner22)
    db.session.add(owner23)
    db.session.add(owner25)
    db.session.add(owner26)
    db.session.add(owner27)
    db.session.add(owner28)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
