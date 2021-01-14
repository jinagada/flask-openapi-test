#!/usr/bin/env bash
JAVA_HOME=`/usr/libexec/java_home -v 1.8`
OG_CLI="./openapi-generator-cli.jar"
${JAVA_HOME}/bin/java -jar ${OG_CLI} "$@"
