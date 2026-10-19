# ELK Log Aggregation Pipeline

A local observability lab that collects JSON application logs with Filebeat, indexes them in Elasticsearch, and explores them in Kibana.

## Architecture

`log generator -> shared volume -> Filebeat -> Elasticsearch -> Kibana`

## Run locally

```bash
docker compose up --build
```

Open [http://localhost:5601](http://localhost:5601), create a data view for `portfolio-logs-*`, and use `@timestamp` as the time field.

## Verify ingestion

```bash
curl http://localhost:9200/portfolio-logs-*/_count
```

Stop the stack with `docker compose down -v`.

## What this demonstrates

- Structured JSON logging
- Log shipping decoupled from the application
- Searchable operational events for incident investigation

This repository is a local demonstration. Production deployments should add authentication, TLS, retention management, and resource limits.
