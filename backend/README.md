Tech Stack Web Application Backend

Introduction
Tech Stack is a strong cross platform framework with modern architecture. A developer platform for building all kinds of web, mobile and desktop applications across different frameworks based on the requirement. It is a framework that help developers to kick-start their development with integrated back-end and frond-end templates.

o	How does it benefit your development?

It provides a fully customizable templates of your favourite front-end and back-end framework to start with. No need to install different libraries and dependencies, you can get here all in one.
We have already integrated the front-end client to the back-end server of the template. Necessary packages will be downloaded automatically with one simple command using docker.

User Guide 
Step1: Tech Stack is an open-source application for all kind of users. You just need to open the application using this url: https://frondend.d3eo2hilmaxlla.amplifyapp.com/.

Step2: Click on Get Started button.
 
Step 3:  You will be redirected to the template page where you need to select your desired framework from dropdown menu.

 
	
Step 4: After selecting your front-end framework, scroll down, similarly select your desired backend framework from the drop-down menu.
 
  

Step 5: Finally, just click on download button. Your template will be downloaded.
 

Step 6: Extract the downloaded zip file and read the READme.txt file. Follow the steps mentioned in it, and now you are ready to develop. Start coding!

How to use the downloaded templates

To use the downloaded template, you need to have docker installed on your computer.
If you do not have docker installed on your computer you may use the following link to download and install docker.
https://www.docker.com/products/docker-desktop/
# How To make build
cd <Project_Dir>
docker-compose build
Open your command terminal, and change your directory to the folder containing the files.
# How to run the application
docker-compose up
# How to stop the application
docker-compse stop or CTRL+C
How it works
The docker compose command create two docker containers to run the frontend (web) and backend (server). A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.
The web container download and install all the decencies automatically inside the container and run the web server. To allow user to make changes in the web application, a folder of the computer is mapped with that of docker container. Also, the port of the container is mapped with the local port of the computer to examine the changes and web application developed. Similar procedure is adopted to setup the server container and is mapped with the local folder.
•	To change local port of the web server, edit the docker-compose.yml file 














•	To change the web framework edit the App file under src folder in the web framework
•	To change the server framework edit the server file under server framework

Benefits of the Tech stack web application
