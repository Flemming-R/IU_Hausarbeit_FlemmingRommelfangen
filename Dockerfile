# Start from the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /

# Install system dependencies for Python packages
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY . /

# Install required packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install JupyterLab for running Jupyter Notebooks
RUN pip install --default-timeout=100 jupyterlab

# Install Ollama CLI using curl
RUN curl -fsSL https://ollama.com/install.sh | sh

# Expose the port Jupyter uses
EXPOSE 8888

# Default command to start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
