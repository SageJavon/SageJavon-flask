# Use an official Python runtime as a parent image, specifically the slim version to keep the image size down
FROM python:3.11-slim

# Set the working directory to /app inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 7000 available to the world outside this container
EXPOSE 7000

# Define the command to run on container start. This script starts the Flask application.
CMD ["python", "create_sqlite_db.py", "&&", "python", "rag_gpt_app.py"]
