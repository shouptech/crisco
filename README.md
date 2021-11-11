# Crisco

Crisco is a service for _shortening_ URLs written in Python using FastAPI.

This is done by defining a YAML file with a list of URLs to "shorten". Shortening in
this context is really just redirecting a `key` to a `value`.

## Running

Create a config file defining the URLs you want. See
[`sample-config.yaml`](sample-config.yaml) for examples.
