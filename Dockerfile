FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 python3-pip vim && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y git vim wget curl && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the entire current directory into the container
COPY . .

# Install Python dependencies
RUN python3 -m pip install --upgrade pip

# Install the package
RUN pip install -e .

# Run a bash prompt by default
CMD ["/bin/bash"]

