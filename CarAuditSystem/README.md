How to start 

Commands
```shell
export FLASK_ENV=<current_environmnet>

python manage.py runserver 
```
acess host/api/1/ to get swagger 

Note:uwsgi can be used later for production running , this above command is non prod or mvp projects


Important Files/Directory Appendix

```yaml
Directories:
  api_intiator: location for views and routes and request schema
  apps : location for all different api services , directory is grouped by table they are accessing
  config : confiugrations for diffrent environment , name of config file is env name,default env base
Files:
  api_intiator/views.py : all views of the api are stored here
  api_intiator/routes.py : all routes of the api are stored here , views mapped to url path 
  api_intiator/request_schema: argument parsers are designed here for get request ,can be used for payload in future
  manage.py : entrypoint of flask app
  database.py : db intializer of flask app
```


