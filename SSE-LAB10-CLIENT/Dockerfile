# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY app.py requirements.txt ./

# Create templates directory and copy HTML files into it
RUN mkdir -p templates
COPY templates/index.html templates/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask app port
EXPOSE 7070

# Command to run the application
CMD ["python", "app.py"]