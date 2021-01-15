# Anaconda3 설치
- CentOS 7 최신 버전 최소설치 기준

## 1. 필요 프로그램 설치

```bash
$ sudo yum install -y epel-release
$ sudo yum install -y wget
$ sudo yum install -y zip
$ sudo yum install -y unzip
$ sudo yum update
$ sudo yum groupinstall -y "Development Tools"
```

## 2. 다운로드

```bash
# 다운로드
$ wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh

# 실행 권한 설정
$ chmod +x Anaconda3-2020.07-Linux-x86_64.sh
```

## 3. Anaconda3 프로그램 설치

```bash
$ ./Anaconda3-2020.07-Linux-x86_64.sh
```

### 3-1. 설치 화면

```bash
Welcome to Anaconda3 2020.02

In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue
>>>
```

- ENTER

```bash
Do you accept the license terms? [yes|no]
[no] >>>
```

- yes

```bash
Anaconda3 will now be installed into this location:
/home/yelloweb/anaconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/home/yelloweb/anaconda3] >>>
```

- ENTER

```bash
Preparing transaction: done
Executing transaction: done
installation finished.
Do you wish the installer to initialize Anaconda3
by running conda init? [yes|no]
[no] >>>
```

- yes

```bash
no change     /home/yelloweb/anaconda3/condabin/conda
no change     /home/yelloweb/anaconda3/bin/conda
no change     /home/yelloweb/anaconda3/bin/conda-env
no change     /home/yelloweb/anaconda3/bin/activate
no change     /home/yelloweb/anaconda3/bin/deactivate
no change     /home/yelloweb/anaconda3/etc/profile.d/conda.sh
no change     /home/yelloweb/anaconda3/etc/fish/conf.d/conda.fish
no change     /home/yelloweb/anaconda3/shell/condabin/Conda.psm1
no change     /home/yelloweb/anaconda3/shell/condabin/conda-hook.ps1
no change     /home/yelloweb/anaconda3/lib/python3.7/site-packages/xontrib/conda.xsh
no change     /home/yelloweb/anaconda3/etc/profile.d/conda.csh
modified      /home/yelloweb/.bashrc

==> For changes to take effect, close and re-open your current shell. <==

If you'd prefer that conda's base environment not be activated on startup, 
   set the auto_activate_base parameter to false: 

conda config --set auto_activate_base false

Thank you for installing Anaconda3!

===========================================================================

Anaconda and JetBrains are working together to bring you Anaconda-powered
environments tightly integrated in the PyCharm IDE.

PyCharm for Anaconda is available at:
https://www.anaconda.com/pycharm

[yelloweb@localhost ~]$
```

### 3-2. 완료 후 계정 재접속(logout -> login)

```bash
(base) [yelloweb@localhost ~]$
```

## 4. Test 용 가상환경 생성

```bash
(base) $ conda create -n flask-openapi-test python=3.7 anaconda
```

### 4-1. 환경 생성 처리

```bash
zstd               pkgs/main/linux-64::zstd-1.4.5-h0b5b093_0

Proceed ([y]/n)?
```

- y

```bash
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
# To activate this environment, use
#
#     $ conda activate bi-dashboard
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) $
```

## 5. Test 용 가상환경으로 변경

```bash
(base) $ conda activate flask-openapi-test
(flask-openapi-test) $
```

## 6. 프로젝트 소스 디렉토리 생성

```bash
$ mkdir -p anaconda3/envs/flask-openapi-test/project/flask-openapi-test
```

## 7. 추가 모듈 설치
### 7-1. 모듈 업데이트

```bash
$ conda update --prefix /home/yelloweb/anaconda3/envs/flask-openapi-test anaconda
$ conda update --all
$ conda update -c anaconda --all
$ conda update -c conda-forge --all
```

### 7-2. Connexion 설치

```bash
$ conda install -c conda-forge connexion
$ conda remove connexion
```

### 7-3. Werkzeug 설치

```bash
$ conda install -c anaconda werkzeug
$ conda remove werkzeug
```

### 7-4. Swagger-ui-bundle 설치

```bash
$ conda install -c conda-forge swagger-ui-bundle
$ conda remove swagger-ui-bundle
```

### 7-5 gunicorn 설치

```bash
$ conda install -c anaconda gunicorn
$ conda remove gunicorn
```

### 7-6 flask-cors 설치

```bash
$ conda install -c anaconda flask-cors
$ conda remove flask-cors
```

## 8. logrotate 설정
- LOG BASE : /home/yelloweb/logs/flask-openapi-test
- LOG 디릭토리 생성

```bash
$ mkdir -p logs/flask-openapi-test
```

```bash
$ sudo vi /etc/logrotate.d/flask-openapi-test
```

- 내용

```bash
/home/yelloweb/logs/flask-openapi-test/*.log {
    copytruncate
    daily
    rotate 15
    maxage 7
    missingok
    notifempty
    compress
    dateext
    dateformat -%Y%m%d_%s
    postrotate
        /bin/chown yelloweb:yello /home/yelloweb/logs/flask-openapi-test/*.log*
    endscript
    su root yello
}
```

## 9. Local 개발 테스트용 CentOS 방화벽 설정

```bash
$ sudo firewall-cmd --permanent --add-port=5002/tcp
$ sudo firewall-cmd --reload
$ sudo firewall-cmd --list-all
$ sudo systemctl restart firewalld
```

## 10. Local 개발환경에 OpenAPI Generator 설치
- 참고
  * URL : [OpenAPI Generator Installation](https://github.com/OpenAPITools/openapi-generator#1---installation)
- Download JAR 방식 사용

### 10-1. Download JAR

```bash
$ cd {Project Path}
$ mkdir openapi-generator
$ cd openapi-generator
$ curl -o openapi-generator-cli.jar https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/5.0.0/openapi-generator-cli-5.0.0.jar
```

### 10-2. 실행 스크립트 생성

```bash
$ vi openapi-generator-cli.sh
```

- 내용

```bash
#!/usr/bin/env bash
JAVA_HOME=`/usr/libexec/java_home -v 1.8`
OG_CLI="./openapi-generator-cli.jar"
${JAVA_HOME}/bin/java -jar ${OG_CLI} "$@
```

- 실행권한 설정

```bash
$ chmod +x openapi-generator-cli.sh
```

- 동작확인

```bash
$ ./openapi-generator-cli.sh help
--- 결과 출력
usage: openapi-generator-cli <command> [<args>]

The most commonly used openapi-generator-cli commands are:
    author        Utilities for authoring generators or customizing templates.
    batch         Generate code in batch via external configs.
    config-help   Config help for chosen lang
    generate      Generate code with the specified generator.
    help          Display help information about openapi-generator
    list          Lists the available generators
    meta          MetaGenerator. Generator for creating a new template set and configuration for Codegen.  The output will be based on the language you specify, and includes default templates to include.
    validate      Validate specification
    version       Show version information used in tooling

See 'openapi-generator-cli help <command>' for more information on a specific
command.
---
```

### 10-3. python-flask Template 샘플 파일 확인
- 참고
  * URL : [templating.md](https://github.com/OpenAPITools/openapi-generator/blob/master/docs/templating.md)
  * URL : [sample code](https://trac.engsas.de/gnuboat/browser/src/mapservice?rev=13cbe66f44f250d5e3f76cda11e899f528e510df)
  
- 관련내용

```text
If you've already cloned openapi-generator, find and copy the modules/openapi-generator/src/main/resources/Java directory.
If you have the Refined GitHub Chrome or Firefox Extension, you can navigate to this directory on GitHub and click the "Download" button.
Or, to pull the directory from latest master:
```

```bash
mkdir -p ~/.openapi-generator/templates/ && cd $_
curl -L https://api.github.com/repos/OpenAPITools/openapi-generator/tarball | tar xz
mv `ls`/modules/openapi-generator/src/main/resources/Java ./Java
\rm -rf OpenAPITools-openapi-generator-*
cd Java
```

- 여기서는 “/modules/openapi-generator/src/main/resources/python-flask” 디렉토리의 *.mustache 파일을 templates 디렉토리로 복사한다.

```bash
# Template 파일용 디렉토리 생성
$ mkdir templates

# 파일 다운로드 및 압축해제
$ curl -L https://api.github.com/repos/OpenAPITools/openapi-generator/tarball | tar xz

# 파일복사
$ cp {OpenAPITools Download Dir}/modules/openapi-generator/src/main/resources/python-flask/*.mustache templates/
```

- *.mustache 파일중 필요한 파일을 Custom 해서 사용
- __main__.mustache 파일 수정
  * AS-IS

```text
{{#supportPython2}}
  #!/usr/bin/env python
  {{/supportPython2}}
{{^supportPython2}}
#!/usr/bin/env python3
{{/supportPython2}}

import connexion

from {{packageName}} import encoder


def main():
  app = connexion.App(__name__, specification_dir='./openapi/')
  app.app.json_encoder = encoder.JSONEncoder
  app.add_api('openapi.yaml',
              arguments={'title': '{{appName}}'},
              pythonic_params=True)
  app.run(port={{serverPort}})


if __name__ == '__main__':
  main()
```

  * TO-BE
  
```text
{{#supportPython2}}
#!/usr/bin/env python
{{/supportPython2}}
{{^supportPython2}}
#!/usr/bin/env python3
{{/supportPython2}}

import connexion
import logging
import os
from pathlib import Path

from {{packageName}} import encoder

# logging 설정
logger = logging.getLogger('flask-openapi-test')
home = str(Path(os.path.expanduser('~')))
log_path = home + '/logs/flask-openapi-test'
# Log 디렉토리 생성
if not os.path.exists(log_path):
    os.makedirs(log_path)
# Logger 설정
formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] %(filename)s(%(lineno)d) : %(message)s')
file_handler = logging.FileHandler(log_path + os.sep + 'flask-openapi-test.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

# Flask App 설정
app = connexion.App(__name__, specification_dir='./openapi/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('openapi.yaml',
            arguments={'title': '{{appName}}'},
            pythonic_params=True)
app.app.config.from_object('{{packageName}}.server_impl.Config.DevelopmentConfig')


if __name__ == '__main__':
    app.run(port={{serverPort}})
```

- controller.mustache 파일 수정
  * AS-IS

```text
import connexion
import six

{{#imports}}{{import}}  # noqa: E501
{{/imports}}
from {{packageName}} import util
{{#operations}}
{{#operation}}


def {{operationId}}({{#allParams}}{{paramName}}{{^required}}=None{{/required}}{{^-last}}, {{/-last}}{{/allParams}}):  # noqa: E501
    """{{#summary}}{{.}}{{/summary}}{{^summary}}{{operationId}}{{/summary}}

    {{#notes}}{{.}}{{/notes}} # noqa: E501

    {{#allParams}}
    :param {{paramName}}: {{description}}
        {{^isContainer}}
            {{#isPrimitiveType}}
    :type {{paramName}}: {{>param_type}}
            {{/isPrimitiveType}}
            {{#isUuid}}
    :type {{paramName}}: {{>param_type}}
            {{/isUuid}}
            {{^isPrimitiveType}}
                {{#isFile}}
    :type {{paramName}}: werkzeug.datastructures.FileStorage
                {{/isFile}}
                {{^isFile}}
                    {{^isUuid}}
    :type {{paramName}}: dict | bytes
                    {{/isUuid}}
                {{/isFile}}
            {{/isPrimitiveType}}
        {{/isContainer}}
        {{#isArray}}
            {{#items}}
                {{#isPrimitiveType}}
    :type {{paramName}}: List[{{>param_type}}]
                {{/isPrimitiveType}}
                {{^isPrimitiveType}}
    :type {{paramName}}: list | bytes
                {{/isPrimitiveType}}
            {{/items}}
        {{/isArray}}
        {{#isMap}}
            {{#items}}
                {{#isPrimitiveType}}
    :type {{paramName}}: Dict[str, {{>param_type}}]
                {{/isPrimitiveType}}
                {{^isPrimitiveType}}
    :type {{paramName}}: dict | bytes
                {{/isPrimitiveType}}
            {{/items}}
        {{/isMap}}
    {{/allParams}}

    :rtype: {{#returnType}}{{.}}{{/returnType}}{{^returnType}}None{{/returnType}}
    """
    {{#allParams}}
        {{^isContainer}}
            {{#isDate}}
    {{paramName}} = util.deserialize_date({{paramName}})
            {{/isDate}}
            {{#isDateTime}}
    {{paramName}} = util.deserialize_datetime({{paramName}})
            {{/isDateTime}}
            {{^isPrimitiveType}}
                {{^isFile}}
                    {{^isUuid}}
    if connexion.request.is_json:
        {{paramName}} = {{#baseType}}{{baseType}}{{/baseType}}{{^baseType}}{{#dataType}} {{dataType}}{{/dataType}}{{/baseType}}.from_dict(connexion.request.get_json())  # noqa: E501
                    {{/isUuid}}
                {{/isFile}}
            {{/isPrimitiveType}}
        {{/isContainer}}
        {{#isArray}}
            {{#items}}
                {{#isDate}}
    if connexion.request.is_json:
        {{paramName}} = [util.deserialize_date(s) for s in connexion.request.get_json()]  # noqa: E501
                {{/isDate}}
                {{#isDateTime}}
    if connexion.request.is_json:
        {{paramName}} = [util.deserialize_datetime(s) for s in connexion.request.get_json()]  # noqa: E501
                {{/isDateTime}}
                {{#complexType}}
    if connexion.request.is_json:
        {{paramName}} = [{{complexType}}.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
                {{/complexType}}
            {{/items}}
        {{/isArray}}
        {{#isMap}}
            {{#items}}
                {{#isDate}}
    if connexion.request.is_json:
        {{paramName}} = {k: util.deserialize_date(v) for k, v in six.iteritems(connexion.request.get_json())}  # noqa: E501
                {{/isDate}}
                {{#isDateTime}}
    if connexion.request.is_json:
        {{paramName}} = {k: util.deserialize_datetime(v) for k, v in six.iteritems(connexion.request.get_json())}  # noqa: E501
                {{/isDateTime}}
                {{#complexType}}
    if connexion.request.is_json:
        {{paramName}} = {k: {{baseType}}.from_dict(v) for k, v in six.iteritems(connexion.request.get_json())}  # noqa: E501
                {{/complexType}}
            {{/items}}
        {{/isMap}}
    {{/allParams}}
    return 'do some magic!'
{{/operation}}
{{/operations}}
```

  * TO-BE

```text
import connexion
import six

{{#imports}}{{import}}  # noqa: E501
{{/imports}}
from {{packageName}} import util
{{#operations}}
{{#operation}}

from {{packageName}}.server_impl.controllers import {{classname}}


def {{operationId}}({{#allParams}}{{paramName}}{{^required}}=None{{/required}}{{^-last}}, {{/-last}}{{/allParams}}):  # noqa: E501
    """{{#summary}}{{.}}{{/summary}}{{^summary}}{{operationId}}{{/summary}}

    {{#notes}}{{.}}{{/notes}} # noqa: E501

    {{#allParams}}
    :param {{paramName}}: {{description}}
        {{^isContainer}}
            {{#isPrimitiveType}}
    :type {{paramName}}: {{>param_type}}
            {{/isPrimitiveType}}
            {{#isUuid}}
    :type {{paramName}}: {{>param_type}}
            {{/isUuid}}
            {{^isPrimitiveType}}
                {{#isFile}}
    :type {{paramName}}: werkzeug.datastructures.FileStorage
                {{/isFile}}
                {{^isFile}}
                    {{^isUuid}}
    :type {{paramName}}: dict | bytes
                    {{/isUuid}}
                {{/isFile}}
            {{/isPrimitiveType}}
        {{/isContainer}}
        {{#isArray}}
            {{#items}}
                {{#isPrimitiveType}}
    :type {{paramName}}: List[{{>param_type}}]
                {{/isPrimitiveType}}
                {{^isPrimitiveType}}
    :type {{paramName}}: list | bytes
                {{/isPrimitiveType}}
            {{/items}}
        {{/isArray}}
        {{#isMap}}
            {{#items}}
                {{#isPrimitiveType}}
    :type {{paramName}}: Dict[str, {{>param_type}}]
                {{/isPrimitiveType}}
                {{^isPrimitiveType}}
    :type {{paramName}}: dict | bytes
                {{/isPrimitiveType}}
            {{/items}}
        {{/isMap}}
    {{/allParams}}

    :rtype: {{#returnType}}{{.}}{{/returnType}}{{^returnType}}None{{/returnType}}
    """
    {{#allParams}}
        {{^isContainer}}
            {{#isDate}}
    {{paramName}} = util.deserialize_date({{paramName}})
            {{/isDate}}
            {{#isDateTime}}
    {{paramName}} = util.deserialize_datetime({{paramName}})
            {{/isDateTime}}
            {{^isPrimitiveType}}
                {{^isFile}}
                    {{^isUuid}}
    if connexion.request.is_json:
        {{paramName}} = {{#baseType}}{{baseType}}{{/baseType}}{{^baseType}}{{#dataType}} {{dataType}}{{/dataType}}{{/baseType}}.from_dict(connexion.request.get_json())  # noqa: E501
                    {{/isUuid}}
                {{/isFile}}
            {{/isPrimitiveType}}
        {{/isContainer}}
        {{#isArray}}
            {{#items}}
                {{#isDate}}
    if connexion.request.is_json:
        {{paramName}} = [util.deserialize_date(s) for s in connexion.request.get_json()]  # noqa: E501
                {{/isDate}}
                {{#isDateTime}}
    if connexion.request.is_json:
        {{paramName}} = [util.deserialize_datetime(s) for s in connexion.request.get_json()]  # noqa: E501
                {{/isDateTime}}
                {{#complexType}}
    if connexion.request.is_json:
        {{paramName}} = [{{complexType}}.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
                {{/complexType}}
            {{/items}}
        {{/isArray}}
        {{#isMap}}
            {{#items}}
                {{#isDate}}
    if connexion.request.is_json:
        {{paramName}} = {k: util.deserialize_date(v) for k, v in six.iteritems(connexion.request.get_json())}  # noqa: E501
                {{/isDate}}
                {{#isDateTime}}
    if connexion.request.is_json:
        {{paramName}} = {k: util.deserialize_datetime(v) for k, v in six.iteritems(connexion.request.get_json())}  # noqa: E501
                {{/isDateTime}}
                {{#complexType}}
    if connexion.request.is_json:
        {{paramName}} = {k: {{baseType}}.from_dict(v) for k, v in six.iteritems(connexion.request.get_json())}  # noqa: E501
                {{/complexType}}
            {{/items}}
        {{/isMap}}
    {{/allParams}}
    return {{classname}}.{{operationId}}({{#allParams}}{{paramName}}{{^required}}={{paramName}}{{/required}}{{#hasMore}}, {{/hasMore}}{{/allParams}})
{{/operation}}
{{/operations}}
```

### 10-4. Flask 소스 자동생성 스크립트

```bash
$ vi generate-src.sh
```

- 내용

```bash
#!/usr/bin/env bash
rm -rf ../src-gen

./openapi-generator-cli.sh generate -i ../yaml/sample.yml \
-o ../src-gen \
-g python-flask \
-t templates \
--package-name openapi_test \
-p=serverPort=5002

cp -r ../src/server_impl ../src-gen/openapi_test/
```

- 실행권한 설정

```bash
$ chmod +x generate-src.sh
```

- 동작확인

```bash
$ ./generate-src.sh
```

## 11. 시작/종료 Script
- 서버 접속 후 GUnicorn 시작/종료 Script 작성
- 디렉토리 변경

```bash
$ cd ~
```

- start script

```bash
$ vi start-openapi-test-local.sh
```

- 내용

```bash
#!/bin/bash
cd /home/yelloweb/anaconda3/envs/flask-openapi-test/project/flask-openapi-test/src-gen
/home/yelloweb/anaconda3/envs/flask-openapi-test/bin/python \
/home/yelloweb/anaconda3/envs/flask-openapi-test/bin/gunicorn openapi_test.__main__:app \
--workers 3 -t 0 --daemon -b :5002 \
--error-logfile /home/yelloweb/logs/flask-openapi-test/gunicorn-local-error.log
```

- stop script

```bash
$ vi stop-openapi-test-local.sh
```

- 내용

```bash
#!/bin/bash
kill -9 `ps aux | grep gunicorn | grep openapi_test.__main__:app | awk '{ print $2 }'`
```

- 실행 권한 설정

```bash
$ chmod +x *.sh
```
