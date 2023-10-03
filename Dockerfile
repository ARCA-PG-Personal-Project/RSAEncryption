FROM python:3.8-slim

COPY ./app /app
COPY requirements.txt .
RUN apt-get update \	
   && apt-get install gcc -y \	
   && apt-get clean
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 8000
CMD ["python", "app/main.py"]


# FROM python:3.9-slim

# # Set the working directory in the container
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# RUN apt-get update \	
#     && apt-get install gcc -y \	
#     && apt-get clean
    
# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir  -r requirements.txt

# # Make port 8000 available to the world outside this container
# EXPOSE 8000

# # Run app.py when the container launches
# CMD ["python", "./main.py"]
