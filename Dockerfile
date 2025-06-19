# Stage 1: Build stage
FROM python:3.10-slim AS builder

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies to a separate directory
COPY requirements.txt .

RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --prefix=/install -r requirements.txt

# Copy app source code
COPY ./app ./app

# Stage 2: Final minimal image
FROM python:3.10-slim

# Create a non-root user to run the app
RUN useradd --create-home appuser

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /install /usr/local

# Copy app code
COPY --from=builder /app ./app

# Change ownership of /app to the non-root user
RUN chown -R appuser:appuser /app

USER appuser

# Expose port your FastAPI app runs on (default 8000)
EXPOSE 8000

# Start the app with Uvicorn, binding to all interfaces
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
