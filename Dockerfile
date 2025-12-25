# Define a imagem base
ARG PYTHON_VERSION=3.11.5
FROM python:${PYTHON_VERSION}-slim AS base

RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

# Rust compiler for LLM
RUN curl https://sh.rustup.rs -sSf | bash -s -- -y
ENV PATH="/root/.cargo/bin:${PATH}"

# Prevents Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Prevents Python from buffering stdout and stderr to avoid situations where
# the application crashes without issuing any logs due to buffering
ENV PYTHONUNBUFFERED=1

# Defines work dir
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app
COPY ./static ./static

# Defines the port on which the application receives connections
EXPOSE 3000

# Executes api
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3000"]
