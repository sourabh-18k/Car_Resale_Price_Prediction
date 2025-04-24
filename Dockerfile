# Use a base image
FROM python:3.10-slim

# Set working directory to /app
WORKDIR /app

# Copy the entire project directory contents into the container at /app
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port used by Streamlit
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
