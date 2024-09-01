<h1> Deploying a Flask Application with Docker </h1>

[Overview] (https://github.com/JioGraphy/Python-Dockerized?tab=readme-ov-file#-overview-)
[Getting-Started] (https://github.com/JioGraphy/Python-Dockerized?tab=readme-ov-file#-overview-)
[Objective] 
[Pre-requisites] (https://github.com/JioGraphy/Python-Dockerized?tab=readme-ov-file#-pre-requisites-)
  - [WSL] (https://learn.microsoft.com/en-us/windows/wsl/install)
  - [Flask] (https://flask.palletsprojects.com/en/3.0.x/installation/)
  - [Docker-Daemon] (https://docs.docker.com/engine/install/)
  - [Dockerhub] (https://hub.docker.com/)
[Procedures] (https://github.com/JioGraphy/Python-Dockerized?tab=readme-ov-file#-pre-requisites-)
[File-Structure] 
[Conclusion]

<h2> Overview </h2>
This project is a simple Flask-based Python application deployed using Docker containers. The setup leverages Docker Daemon, WSL (Windows Subsystem for Linux), and Flask to create a seamless development and deployment experience. The goal is to demonstrate how to build image, run and deploy application using containerization

<h2> Getting Started </h2>
Before you start, make sure you have necessary software installed in your local machine.

<h2> Objective </h2>
This project is a simple Flask-based Python application deployed using Docker containers. The setup leverages Docker Daemon, WSL (Windows Subsystem for Linux), and Flask to create a seamless development and deployment experience. The goal is to demonstrate how to build image, run and deploy application using containerization
Additionally, it aims to provide an understanding of the project’s file structure.

<h2> Pre-requisites </h2>
Before proceeding, make sure you have the following installed on your machine:
- **[WSL 2](https://learn.microsoft.com/en-us/windows/wsl/install)**: Required for running Linux-based containers on Windows.
- **[Docker Desktop/Daemon](https://docs.docker.com/engine/install/)**: The Docker Engine to build and run containers.
- **[Docker Hub Account](https://hub.docker.com/)**: For optionally pushing and pulling Docker images.

<h2> Procedures </h2>
Follow the instructions provided in 'instructions.txt' file

<h2> File-Structure </h2>
- **`app.py`**: The main entry point for the Flask application.
- **`Dockerfile`**: The configuration file used to build the Docker image for the application.
- **`Instructions.txt`**: A step-by-step guide on how to perform each action, from setup to deployment.
- **`README.md`**: A comprehensive overview of the project, including setup, usage, and other relevant information.
- **`requirements.txt`**: A list of required Python packages to be installed within the Docker container.

<h2> Conclusion </h2>
After following the instructions. You now have a simple Python web application running in a Docker container. This process covered creating a Python app, building, containerizing it with Docker, and optionally push/pull it to or from Docker Hub for distribution.




