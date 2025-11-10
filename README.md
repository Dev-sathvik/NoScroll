# NoScroll
<<<<<<< HEAD
#### Video Demo:  <[URL HERE](https://youtu.be/8WKmfnCfBfk)>
#### Description:


### Introduction
My project tries to solve the problem of doomscrolling. Doomscrolling is the process where a person scrolls down short video formats for fun without even noticing the time that is passing away. This is a problem that I myself have faced multiple times and I wanted to create a solution to stop this problem. Even though the short format platforms give the option to limit usage, it didn't work for me and i think everyone will agree. The main reason being it is not strict enough to stop me from watching more reels. I wanted to create web app that would unify all these people, where they would enroll to stop scrolling and provide their motivation for limiting their consumption. I believe after seeing this community of people expressing their thoughts, it would make anyone enroll and be part of this auspicious community.

I used the flask framework to handle server requests and used HTML, CSS, Javascript, Jquery, Bootstrap, jinja template in order to create this web app. For database i used the SQLite3 software. I have also used ZenQuotes API to display motivational quotes. Also used the bootswatch website themes and favicon generator.

-----

### Functionalities
#### app.py
* Routes

    **/** : This route fetches all the enrolled people details from the noscroll database and sends the data to the *index.html* file.

    **/register** : This route is responsible for registration of the web app users. If the request is *GET* it returns the *register.html* file. If it is a *POST* request, it will receIve username, password, and confirmation password. If any field is invalid, it will return a flask message to display the error. Provided all the details are correct, it should be stored in the database, and the hashed password is saved. The session is saved for the registered user and the user logs in. Uses *register.html* to display the form for entering the fields.

    **/login** : This route is responsible for logging in for registered users. Compares the username with the entered password in the database and provides access to use this app. Uses *login.html* to display the form to enter data.

    **/logout** : This route is responsible for log out feature of the web app. It clears the session and logs out the user.

    **/enroll** : This route is responsible for enrolling the users to noscroll community. if the request is *GET* it displays the HTML file for entering the details such as name, username on any of the scrolling platforms, motivation for enrolling as well as the daily average scrolling duration. The entered information is stored in the database.If the user is already enrolled, then it will provide the option for quitting using **/exit** and display a motivation quote from the zenquotes api functionality. Uses *enroll.html* to display the data.

    **/stats** : This route is responsible to display the statistics of the web app. It displays the total number of registered users, total number of enrolled users and people who have enrolled today. Uses *stats.html* to display the data.

    **/profile** : This route is responsible to display all the information of the enrolled users. It also displays the enrolled streaks as well as approximately saved time for the enrolled users.


#### helpers.py
* Functions

    **login required** : Ensures that some routes are available only after the user is logged in.

    **lookup** : This function fetches the motivational quotes from the zenquotes api. It performs the *GET* request to the specified url. It returns the data in json format from where the motivational quote and the author is fetched and displays it to the user when he wants to quit.

#### noscroll.db
* Tables

    **users** : Stores the username and the hashed value as password.

    **enrolled** : Stores the enrolled users name, username, motivation, time spent scrolling, as well as date of enrollment.

### Other Features
* Community view: This option in the homepage displays all the people who have enrolled as well as their other details such as motivation and username. This would make a user feel that he is not alone in this task.

* Animations: I have used the jquery's *slidetoggle()* method to create the sliding effect when viewing the community. Also when displaying stats, i have used javascript to create a nice animation when displaying the numbers. Looks great!

* Streak and time saved calculations: The streak calculation is done by finding the difference between today's date and the enrolled date found in the database.
Time saved calculation is done by multiplying the streak with the time spent scrolling from the database.
=======

A Web Application which focuses on reducing excessive scrolling on reels by forming a community of users who want to stay focused. Built as part of the Harvard CS50x course final project.
>>>>>>> 2f66ac3745979f3bf99fe02ac52eb4774d83aafd
