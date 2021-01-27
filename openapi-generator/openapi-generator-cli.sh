#!/usr/bin/env bash
OG_CLI="./openapi-generator-cli.jar"
JAVA_HOME=`/usr/libexec/java_home -v 1.8 2> /dev/null`
if [ $JAVA_HOME ] ;then
    ${JAVA_HOME}/bin/java -jar ${OG_CLI} "$@"
else
    if [ -f "/usr/lib/jvm/java-1.8.0/bin/java" ] ;then
        /usr/lib/jvm/java-1.8.0/bin/java -jar ${OG_CLI} "$@"
    else
        /usr/local/jdk1.8.0_111/bin/java -jar ${OG_CLI} "$@"
    fi
fi