# Heroku Server Status Badge
![](https://heroku-status-badges.herokuapp.com/heroku-status-badges)

Display your Heroku app's status on your README or other documents!

### Info
To let users know your server's status easily, this badge is extremely useful. Maybe you want to let people know your API is under maintanance, or your UI is experiences problems. Maybe you want to show your server is up and running as expected. If you answered yes to any of these questions, this badge is for you! Your badge will automatically be made based on your server's homepage's status code.

### Preview
If your app is alive and kicking (any response code other than 404 or 500-599):
![](badges/running.png)

If your app is returning an error (response codes 500-599):
![](badges/down.png)

If your app is not found (response code 404):
![](badges/not_found.png)

### Usage
You can get the image's url from here: `https://heroku-status-badges.herokuapp.com/{app name}`. \
So for example, let's say you had an app named "my-game". Your image url will be `https://heroku-status-badges.herokuapp.com/my-game`.

**Markdown**

    ![](https://heroku-status-badges.herokuapp.com/{app name})

**HTML**

    <img src="https://heroku-status-badges.herokuapp.com/{app name}">

### Warnings and Stuff
If your server is "not found" when it should be, make sure youre "home domain" doesn't return a 404.