# Base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy dependencies first (better for caching)
COPY docker/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create necessary directories
RUN mkdir -p processed embeddings

# Copy application code and data
COPY scripts/ ./scripts/
COPY data/ ./data/
COPY docker/run.sh ./run.sh

# Make run.sh executable
RUN chmod +x run.sh

# Command to run when container starts
CMD ["./run.sh"]
