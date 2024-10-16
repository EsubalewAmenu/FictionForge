# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirement.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirement.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Copy the entrypoint script
COPY entrypoint.sh /app/

# Expose port 8080 to the outside world
EXPOSE 8080

# Set the entry point script
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
