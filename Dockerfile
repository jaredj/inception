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

# Install Python dependencies
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip && \
    pip install pydeps --no-deps && \
    pip install pyasp && \
    pip install pydeps && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Copy the entire current directory into the container
COPY . .

# CMD command to run the desired script, e.g.:
# CMD ["python3", "your_script.py"]

