# Stage 1: Build dependencies
FROM ubuntu:latest AS build-deps

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv graphviz && \
    apt-get install -y gnupg && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

# Stage 2: Copy dependencies and run app
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 && \
    rm -rf /var/lib/apt/lists/*

# Copy dependencies from build-deps stage
COPY --from=build-deps /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

# Set the working directory
WORKDIR /app

# Copy the entire current directory into the container
COPY . .

# CMD command to run the desired script, e.g.:
# CMD ["python3", "your_script.py"]

