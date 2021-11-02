FROM python:3.9-slim-bullseye as builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    gettext \
    python3-cffi \
    python3-brotli \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    wait-for-it && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /backend

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /backend/wheels -r requirements.txt

COPY . .


FROM python:3.9-slim-bullseye as prod

WORKDIR /backend

COPY --from=builder /backend/wheels /wheels
COPY --from=builder /backend/requirements.txt .
COPY --from=builder /usr/bin/wait-for-it /usr/bin/wait-for-it

RUN pip install --no-cache /wheels/*

COPY . .

EXPOSE 8000
