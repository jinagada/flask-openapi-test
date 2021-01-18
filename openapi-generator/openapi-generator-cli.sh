#!/usr/bin/env bash
OG_CLI="./openapi-generator-cli.jar"
JAVA_HOME=`/usr/libexec/java_home -v 1.8 2> /dev/null`
if [ $JAVA_HOME ] ;then
        ${JAVA_HOME}/bin/java -jar ${OG_CLI} "$@"
else
        /bin/java -jar ${OG_CLI} "$@"
fi
