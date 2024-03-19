FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY src/backend/requirements.txt .


RUN apt-get update --fix-missing && apt-get install -y --fix-missing build-essential
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire contents of the current directory into the container
COPY . .

# Run pytest command when the container starts
CMD ["pytest"]