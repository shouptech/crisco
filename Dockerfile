FROM python:3.9-slim

COPY . /tmp/crisco

RUN cd /tmp/crisco && \
  python3 setup.py install && \
  mkdir /config && \
  cp sample-config.yml /config/config.yml && \
  cd / && \
  rm -rf /tmp/crisco

EXPOSE 8000

ENV CRISCO_CONFIG_PATH=/config/config.yml

ENTRYPOINT ["uvicorn", "crisco.main:app"]
CMD ["--host", "0.0.0.0", "--port", "8000"]
