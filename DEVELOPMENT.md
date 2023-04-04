# Development Workflow

This document explains the methodology for testing changes to the Inception tool inside a Docker environment while keeping a stable version of the tool running outside of it.

## Prerequisites

1. Install [Docker](https://www.docker.com/products/docker-desktop) on your system.
2. Install the stable version of Inception in your non-Docker environment by running `pip install .`.

## Workflow

### 1. Update and test changes within the Docker environment

To test changes to the Inception tool, follow these steps:

1. Make changes to the codebase in your local environment.
2. Run `./run_in_docker.sh` to enter the Docker environment. This script will build a Docker image, start a container, and map your local repository to the `/app` directory inside the container.
3. Inside the Docker container, test the changes by running the Inception tool. Any changes you make in your local environment will be immediately reflected inside the Docker container, thanks to the volume mapping.

### 2. Exit the Docker environment

When you're done testing the changes inside the Docker environment, exit the container by typing `exit` or pressing `Ctrl-D`. The `run_in_docker.sh` script will automatically stop and remove the container when you exit the bash prompt.

## Benefits

This workflow allows you to test changes to the Inception tool in an isolated environment without affecting the stable version of the tool running outside of Docker. This way, you can continue to use the stable version for applying real changes to your codebase while testing and debugging the new changes in the Docker environment.
