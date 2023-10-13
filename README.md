# My MLOps Project

This project demonstrates the MLOps process for containerizing a machine learning model using Docker.

## Version Control (Step 1)

1. Create a new public GitHub repository for your MLops assignment.
2. Initialize the repository with a README file.
3. Write a simple Python script to train a machine learning model on a dataset of your choice.
4. Commit your code to the repository and push it to GitHub.

## Docker Containerization (Step 2)

### Dockerfile

1. We use a `Dockerfile` to define how to build a Docker image for our project.

   ```Dockerfile
   # Use an official Python runtime as a parent image
   FROM python:3.10

   # Set the working directory to /app
   WORKDIR /app

   # Copy the current directory contents into the container at /app
   COPY . /app

   # Install any needed packages specified in requirements.txt
   RUN pip install -r requirements.txt

   # Make port 80 available to the world outside this container
   EXPOSE 80

   # Define environment variable
   ENV NAME World

   # Run app.py when the container launches
   CMD ["python", "your_script.py"]
