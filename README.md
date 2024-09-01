<h1> Deploying a Flask Application with Docker </h1>
<h2> Table of Contents </h2>

[Overview](https://github.com/JioGraphy/Python-Dockerized?tab=readme-ov-file#-overview-) <br>
[Getting Started](https://github.com/JioGraphy/Python-Dockerized?tab=readme-ov-file#-overview-) <br>
[Objective](https://github.com/JioGraphy/Python-Dockerized/edit/master/README.md#-objective-)<br>
[Pre-requisites](https://github.com/JioGraphy/Python-Dockerized?tab=readme-ov-file#-pre-requisites-)
  - [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) 
  - [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/)
  - [Docker-Daemon](https://docs.docker.com/engine/install/)
  - [Dockerhub](https://hub.docker.com/) <br>

[Procedures](https://github.com/JioGraphy/Python-Dockerized?tab=readme-ov-file#-pre-requisites-) <br>
[File Structure](https://github.com/JioGraphy/Python-Dockerized/edit/master/README.md#-file-structure-) <br>
[Conclusion](https://github.com/JioGraphy/Python-Dockerized/edit/master/README.md#-conclusion-) <br>

<h2> Overview </h2>

This project is a simple Flask-based Python application deployed using Docker containers. The setup leverages Docker Daemon, WSL (Windows Subsystem for Linux), and Flask to create a seamless development and deployment experience. The goal is to demonstrate how to build image, run and deploy application using containerization

<h2> Getting Started </h2>

Before you start, make sure you have necessary software installed in your local machine.

<h2> Objective </h2>

This project is a simple Flask-based Python application deployed using Docker containers. The setup leverages Docker Daemon, WSL (Windows Subsystem for Linux), and Flask to create a seamless development and deployment experience. The goal is to demonstrate how to build image, run and deploy application using containerization
Additionally, it aims to provide an understanding of the project’s file structure.

<h2> Pre-requisites </h2> 

Before proceeding, make sure you have the following installed on your machine: <br>

- [WSL-2](https://learn.microsoft.com/en-us/windows/wsl/install): Required for running Linux-based containers on Windows. <br>
- [Docker Desktop/Daemon](https://docs.docker.com/engine/install/): The Docker Engine to build and run containers. <br>
- [Docker Hub Account](https://hub.docker.com/): For optionally pushing and pulling Docker images. <br>

<h2> Procedures </h2>

Follow the instructions provided in *[instructions.txt](https://github.com/JioGraphy/Python-Dockerized/blob/master/instructions.txt)* file


<h2> File Structure </h2>

> - **`app.py`**: The main entry point for the Flask application. <br>
> - **`Dockerfile`**: The configuration file used to build the Docker image for the application. <br>
> - **`Instructions.txt`**: A step-by-step guide on how to perform each action, from setup to deployment. <br>
> - **`README.md`**: A comprehensive overview of the project, including setup, usage, and other relevant information. <br>
> - **`requirements.txt`**: A list of required Python packages to be installed within the Docker container. <br>

<h2> Conclusion </h2>

After following the instructions. You now have a simple Python web application running in a Docker container. This process covered creating a Python app, building, containerizing it with Docker, and optionally push/pull it to or from Docker Hub for distribution.
