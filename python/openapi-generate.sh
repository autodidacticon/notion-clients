#!/bin/bash
openapi-generator generate -i ./openapi.yaml -g python-nextgen \
-c ./openapi-config.json \
-o ./
