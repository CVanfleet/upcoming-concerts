# Overview

I have a goal to create applications that will be useful for me! This way I can further my learning and get something out of each project I work on!

The last couple weeks I have been working on this Upcoming Concerts web application! I thought it would be great to be able to search an band/artist and get all data on their upcoming concerts.

Check out the link below to see the short demo of my work!

[Software Demo Video](https://youtu.be/HMn7o-NXNx0)

# Web Pages
templates/

├─ base.html

├─ concerts.html

├─ saved.html

└─ upcoming-concerts.html


# Development Environment

Python's Django framework

Bootstrap

SQLite

Python

HTML

# Useful Websites

* [docs.djangoproject.com](https://docs.djangoproject.com/en/4.1/)
* [getbootstrap.com](https://getbootstrap.com/docs/4.0/getting-started/introduction/#starter-template)

# Future Work

* Implement cooler name for the app!
* Create model for a favorites table and include functionality for users to save their favorite concerts
* When querying the database tables, the strings are case sensitive which has been causing some issues
* Allow the user to click on a link to navigate where they can buy tickets


# ** Changed the Database! **

# Overview

The cloud is the future! I wanted to get some experience with NoSQL and try my luck with MongoDB!

This project was originally using the SQLite database that is provided by Django, and I was able to transfer all the data, and configure inserts for more data into my new MongoDB database.

I love the simplicity that MongoDB provides! It was a quick and painless (mostly) process!

[Software Demo Video](https://youtu.be/sC9jGnv_HkA)

# Cloud Database

I created a MongoDB database with two collections. 

1. Concerts
    - This contains concert documents
2. CoPerformers
    - This contains the coperformers at each concert

# Development Environment

Python's Django framework

Bootstrap

MongoDB

Python

HTML

# Useful Websites

- [Tutorials Point](https://www.tutorialspoint.com/mongodb/mongodb_quick_guide.htm#:~:text=If%20you%20want%20to%20check,use%20the%20command%20show%20dbs.&text=Your%20created%20database%20(mydb)%20is,least%20one%20document%20into%20it.)
- [Mongodb](https://www.mongodb.com/docs/mongodb-shell/)

# Future Work

- Fix display so all performers get displayed
- Add feature to delete old concert data
- Improve Search
- Format Date on page