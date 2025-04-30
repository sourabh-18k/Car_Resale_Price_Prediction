# Using a base image
FROM python:3.10-slim


WORKDIR /app


COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8502

# Running Streamlit
CMD ["streamlit", "run", "app/app.py", "--server.port=8502", "--server.address=0.0.0.0"]
