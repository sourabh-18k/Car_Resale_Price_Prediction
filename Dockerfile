# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app code
COPY app/ .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port used by Streamlit
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

