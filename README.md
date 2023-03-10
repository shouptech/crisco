# Crisco

Crisco is a service for _shortening_ URLs written in Python using FastAPI.

This is done by defining a YAML file with a list of URLs to "shorten". Shortening in
this context is really just redirecting a `key` to a `value`.

## Running docker image

Create a config file defining the URLs you want. See
[`sample-config.yml`](sample-config.yml) for examples.

Run the docker image:

```shell
docker run -v /path/to/your/config.yml:/config/config.yml -p 8000:8000 registry.gitlab.com/shouptech/crisco:latest
```

Rejoice!

## Running in Kubernetes

The directory [manifests/](manifests) has some example Kubernetes manifests for running
Crisco. You'll want to modify them to suit your environment. Particularly you may need
changes to [`config.yml`](manifests/config.yml) and
[`ingress.yml`](manifests/ingress.yml).
