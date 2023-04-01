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
    # First, we install pydeps without its dependencies
    pip install pydeps --no-deps && \
    # Then, we install pyasp with its dependencies
    #apt-get install -y libclingo-dev && \
    pip install pyasp && \
    # Finally, we install pydeps with all its dependencies
    pip install pydeps && \
    # Remove unnecessary packages and dependencies
    apt-get remove -y gnupg && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Stage 2: Copy dependencies and run app
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && \
    apt-get install -y python3 && \
    rm -rf /var/lib/apt/lists/*

# Copy dependencies from build-deps stage
COPY --from=build-deps /usr/local/lib/python3.10/dist-packages /usr/local/lib/python3.10/dist-packages
COPY --from=build-deps /usr/lib/python3/dist-packages /usr/lib/python3/dist-packages
COPY --from=build-deps /usr/lib/python3.10/dist-packages /usr/lib/python3.10/dist-packages

# Set the working directory
WORKDIR /app

# Copy the entire current directory into the container
COPY . .

# CMD command to run the desired script, e.g.:
# CMD ["python3", "your_script.py"]

