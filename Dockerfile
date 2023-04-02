FROM ubuntu:latest

# Install Python-related packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Install development tools
RUN apt-get update && \
    apt-get install -y vim git curl wget && \
    rm -rf /var/lib/apt/lists/*

# Install graphviz and other visualization tools
RUN apt-get update && \
    apt-get install -y graphviz && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the entire current directory into the container
COPY . .

# Build the package and install it using pip
RUN python3 setup.py sdist
RUN pip3 install dist/inception-0.1.tar.gz

# CMD command to run the desired script, e.g.:
# CMD ["python3", "your_script.py"]

