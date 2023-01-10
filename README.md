<img width="893" alt="clonebnb" src="https://user-images.githubusercontent.com/103297104/210884733-befcfe27-dbbc-4ade-b3e4-dcf712a264f4.png">

Looking for vacation rentals, cabins, beach houses, and/or unique homes around the world? CloneBnB is where you can find all these things!
(Inspired by the popular website, [airbnb](https://www.airbnb.com/))

**🚀 Live site: [clonebnb](https://clonebnb.herokuapp.com/) **

# 🖱 Wiki Links

[API Documentation](https://github.com/BrennonMorris/AirBnB-Clone/wiki/API-Documentation)

[Database Schema](https://github.com/BrennonMorris/AirBnB-Clone/wiki/Database-Schema)

[Feature List](https://github.com/BrennonMorris/AirBnB-Clone/wiki/Feature-List)

[Redux Store Shape](https://github.com/BrennonMorris/AirBnB-Clone/wiki/Redux-Store-Shape)

[User Stories](https://github.com/BrennonMorris/AirBnB-Clone/wiki/User-Stories)

[Wireframes](https://github.com/BrennonMorris/AirBnB-Clone/wiki/Wireframes)

# 🧑‍💻 Under the Hood

## 🤖 Integrated Web Technologies

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)

## 💾 Database

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## ☁️ Hosting

![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

# 🛬 Landing Page

<img width="1914" alt="Screenshot 2023-01-05 at 1 41 00 PM" src="https://user-images.githubusercontent.com/103297104/210885375-6b927394-a2a3-47cd-a3fd-2e9a9548fda5.png">

## 💡 Features

### Create a Listing

<img width="1912" alt="Screenshot 2023-01-05 at 1 42 15 PM" src="https://user-images.githubusercontent.com/103297104/210885652-e40b0796-5bcc-4dfc-9169-f0337dd1a1cc.png">
<img width="1912" alt="Screenshot 2023-01-05 at 1 46 10 PM" src="https://user-images.githubusercontent.com/103297104/210886110-db5f0833-b562-4423-ac9d-475d1a480832.png">
<img width="1909" alt="Screenshot 2023-01-05 at 1 47 43 PM" src="https://user-images.githubusercontent.com/103297104/210886372-4b8b3e31-18c9-4070-9bcb-27b5e343687f.png">

### View individual Listings

<img width="1911" alt="Screenshot 2023-01-05 at 1 53 52 PM" src="https://user-images.githubusercontent.com/103297104/210887318-fae6aeb6-1caf-4374-85cc-0a6d96d62679.png">

### Update and/or Delete your Listings

<img width="1910" alt="Screenshot 2023-01-05 at 1 55 36 PM" src="https://user-images.githubusercontent.com/103297104/210887593-64e7ffef-9d5a-48d3-b078-62da3fa40a62.png">

### Create a Review

<img width="1910" alt="Screenshot 2023-01-05 at 1 56 59 PM" src="https://user-images.githubusercontent.com/103297104/210887759-84519972-465c-4649-929c-f108bfedff89.png">

### View Reviews for specific Listings

<img width="1916" alt="Screenshot 2023-01-05 at 2 01 06 PM" src="https://user-images.githubusercontent.com/103297104/210888462-e9e48f99-7f74-4591-844f-1287df2f197b.png">

### Update and/or Delete your Reviews

<img width="1912" alt="Screenshot 2023-01-05 at 2 02 38 PM" src="https://user-images.githubusercontent.com/103297104/210888648-38e5d70a-d96b-4fee-accb-d1556fc92501.png">

# 🚧 To do list

1. Complete CRUD functionality for Bookings
2. Complete filter/search functionality based on location, type, and max guests
3. Complete CRUD functionality for Wishlists

# 📲 Setup locally

1. Clone this repository

   ```bash
   git clone https://github.com/BrennonMorris/AirBnB-Clone
   ```

2. Install dependencies

   ```bash
   pipenv install
   cd react-app
   npm install
   ```

3. Create a **.env** file based on the example and set the environment variables for SECRET_KEY and DATABASE_URL for your
   development environment

4. Get into your pipenv, migrate your database, seed your database, run your Flask app, and start your React app

   ```bash
   pipenv shell
   flask db upgrade
   flask seed all
   flask run
   cd react-app
   npm start
   ```
