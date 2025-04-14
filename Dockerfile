# Use the latest Python 3.10 image
FROM python:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the local project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose a port (optional, depending on whether you want to serve the model via an API)
EXPOSE 5000

# Command to run the training script
CMD ["python", "src/train_model.py"]
