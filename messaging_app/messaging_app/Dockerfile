# Use base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# ✅ Create a non-root user
RUN adduser --disabled-password --gecos '' appuser

# Switch to non-root user
USER appuser

# Expose the port Django will use
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

