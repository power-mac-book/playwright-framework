FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements.txt first (for caching)
COPY app/backend/requirements.txt ./requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend app code
COPY app/backend ./backend

# Expose FastAPI's default port
EXPOSE 8000

# Start the FastAPI app using uvicorn
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
