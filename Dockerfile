# Build stage: install dependencies
FROM python:3.10-slim as builder
WORKDIR /app

# Only copy requirements first to leverage caching
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Runtime stage: use a clean image
FROM python:3.10-slim
WORKDIR /app

# Copy installed packages and binaries from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the rest of your application code
COPY . .

EXPOSE 8503
ENV PYTHONUNBUFFERED=1

CMD ["streamlit", "run", "app.py", "--server.port", "8503", "--server.address", "0.0.0.0"]
