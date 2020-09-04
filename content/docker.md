Title: Docker LAMP Stack Quick Start
Date: 2020-08-27 14:01
Category: IT Notes

#### Article's Purpose
This post is a reminder to myself on how to set up a docker LAMP stack container. I am using docker mainly for local development. I am tired of using web server desktop software solutions like XAMPP, AMPPS and MAMP. I want my local development to be similar to my production development. Plus containerization is a good skill to put on your resume.

#### PHP & Apache2 Set Up
Create below file structure for your website.
```
docker-php
|___src
|   |___index.php
|___Dockerfile
```
Next add the below code to the `Dockerfile`
```
FROM php:7.2-apache
RUN docker-php-ext-install mysqli
ENV CI=true
ENV PORT=3000
COPY src/ /var/www/html/
EXPOSE 80

# TODO: Add MYSQL configs
```
Lastly run the below two commands to finish creating a container for a basic PHP website.
```
docker build -t docker-php .
docker run -d -p 3000:80 --mount type=bind,source="$(pwd)/src",target=/var/www/html docker-php
```
If successful a web page <a href="https://kinsta.com/wp-content/uploads/2019/10/phpinfo-page-example.png" target="_blank">that looks like this</a> will be created. Since we've mounted our `src` directory to our container's `/var/www/html` directory, we will be able to see local changes applied on page refresh.

#### Sources
1. [How to mount local PHP changes to a Docker container](https://nelkinda.com/blog/apache-php-in-docker/#d11e96)
2. [How to create a MYSQL Docker container](https://medium.com/better-programming/setting-up-mysql-database-in-a-docker-d6c69a3e9afe)