# syntax=docker/dockerfile:1

# Use Python 3.9 slim as the base image
ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app/voicebot

# Install necessary system dependencies for PyAudio and others
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a non-privileged user to run the app
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

# Copy the requirements file to the container
COPY requirements.txt . 

# Install dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt || { echo "Installation failed, check requirements"; exit 1; }

# Switch to the non-privileged user
USER appuser

# Copy the source code into the container
COPY ./voicebot/ ./voicebot/

# Command to run your voice assistant project
CMD ["python", "voicebot/main.py"]
