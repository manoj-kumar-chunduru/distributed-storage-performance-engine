FROM python:3.11-slim
WORKDIR /app
RUN useradd --create-home --uid 10001 appuser
COPY pyproject.toml README.md ./
COPY src ./src
COPY benchmarks ./benchmarks
RUN pip install --no-cache-dir .
USER appuser
EXPOSE 8000
CMD ["uvicorn","storage_engine.api.app:app","--host","0.0.0.0","--port","8000"]
