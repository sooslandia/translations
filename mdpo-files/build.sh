#!/bin/bash
set -e
docker build -t build-mdpo .
mkdir -p wheels
docker run --rm --name build-mdpo -v ./wheels:/wheels build-mdpo $(id -u):$(id -g)
docker rmi build-mdpo
tar czf wheels.tar.gz wheels
rm -rf wheels
