FROM python:3.10 AS builder
COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.10-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY ./pytelefy ./pytelefy

ENV PATH=/root/.local/bin:$PATH
ENV PYTELEFY_CONFIG_DIR=/etc/pytelefy
ENV PYTELEFY_DATA_DIR=/data

RUN mkdir -p $PYTELEFY_CONFIG_DIR $PYTELEFY_DATA_DIR

CMD [ "uvicorn", "pytelefy:app", "--host", "0.0.0.0" ]