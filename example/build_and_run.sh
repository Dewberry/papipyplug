#!/bin/bash

python -m get_git_info
docker build . -t plugin-example
docker run --rm -it plugin-example:latest 