#!/usr/bin/env bash
rm -rf ../src-gen

./openapi-generator-cli.sh generate -i ../yaml/sample.yml \
-o ../src-gen \
-g python-flask \
-t templates \
--package-name openapi_test \
-p=serverPort=5002

cp -r ../src/server_impl ../src-gen/openapi_test/