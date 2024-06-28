# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /code

# Install build dependencies
RUN apt-get update && apt-get install -y build-essential pkg-config libmariadb-dev

# Copy the requirements file
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the source code
COPY ./tim_events_api /code/tim_events_api

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "tim_events_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
