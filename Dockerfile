# Use an official Python 3.10 image as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt ./

# Install packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code into the container
COPY . .

# Expose the port your Streamlit app uses
EXPOSE 8503

# Ensure stdout/stderr is unbuffered
ENV PYTHONUNBUFFERED=1

# Command to run your Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port", "8503", "--server.address", "0.0.0.0"]
