# Use the latest Ubuntu image as the base
FROM ubuntu:latest

# Add snakefood package repository to the list of sources
RUN echo "deb http://ppa.launchpad.net/jeremysanders/ppa/ubuntu focal main" >> /etc/apt/sources.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 0FF405B2B7F6FEA707DCB5DB87D9D6E7AEFDC3D3

# Update the package list and install necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv graphviz && \
    apt-get install -y flake8 snakefood && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the entire current directory into the container
COPY . .

# Install Python dependencies
RUN python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

# Optional: Run flake8 to check for code style issues
# RUN flake8 .

# CMD command to run the desired script, e.g.:
# CMD ["python3", "your_script.py"]

