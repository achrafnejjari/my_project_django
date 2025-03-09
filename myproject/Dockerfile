FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Installer les dépendances système requises
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Expose the port that Django will run on
EXPOSE 8081

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8081", "--noreload"]































# FROM python:3.10-slim

# # Set working directory
# WORKDIR /app

# # Copy requirements file
# COPY requirements.txt /app/

# # Install Python dependencies (This installs all the Python dependencies listed in the requirements.txt file into the container.The --no-cache-dir option ensures that pip does not store cached copies of the packages, keeping the image size smaller.)
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application files
# COPY . /app/

# # Expose the port that Django will run on
# EXPOSE 8081

# # Command to run the Django development server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8081", "--noreload"]



#--noreload : katkhli django may3axd i download rasso fi7alat dart chi modification