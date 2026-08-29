FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Runtime dependencies only (requirements-dev.txt is deliberately not copied).
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY backend /app/backend
COPY scripts /app/scripts
COPY README.md /app/README.md

# Cloud Run injects PORT and expects the container to listen on it. The default
# is 8080 and is kept here so the image also runs unchanged under `docker run`
# and under ECS, which sets PORT explicitly.
ENV PORT=8080
EXPOSE 8080

# `exec` replaces the shell so uvicorn becomes PID 1 and receives SIGTERM
# directly. Without it the shell holds PID 1, swallows the signal, and every
# scale-to-zero shutdown waits for Cloud Run's kill timeout instead of exiting
# promptly.
CMD ["sh", "-c", "exec uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8080}"]
