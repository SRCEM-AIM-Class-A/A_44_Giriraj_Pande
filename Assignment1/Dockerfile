# Use official Python image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 5000 (Flask default)
EXPOSE 5001

# Command to run the Flask application
CMD ["python", "app.py"]
