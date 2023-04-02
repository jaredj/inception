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

# Create and activate virtual environment
RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

# Install Python dependencies
RUN pip install --upgrade pip
RUN apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

RUN ln -sf $(which python3) /usr/bin/python

# Copy the entire current directory into the container
COPY . .

# Install the package
RUN python setup.py sdist
RUN pip install dist/inception-0.1.0.tar.gz

# Start the container in detached mode
CMD ["sleep", "infinity"]

