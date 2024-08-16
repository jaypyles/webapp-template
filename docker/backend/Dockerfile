# Build python dependencies
FROM python:3.10-slim AS pybuilder

WORKDIR /project

RUN apt update && apt install -y uvicorn
RUN python -m pip --no-cache-dir install pdm
RUN pdm config python.use_venv false

COPY pyproject.toml pdm.lock /project/
COPY ./api /project/api/

RUN pdm install

# Create final image
FROM python:3.10-slim

WORKDIR /project

COPY --from=pybuilder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=pybuilder /project/ /project/
COPY --from=pybuilder /usr/local/bin /usr/local/bin

EXPOSE 8000


CMD [ "pdm", "run", "python", "-m", "uvicorn", "api.backend.app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
