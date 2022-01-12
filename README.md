# elasticsearchproject
This is an elasticsearch project related to web api search. This project is made from the tutorial(https://ke.qq.com/course/3203866)

After clone this project, you can upload the bulk_api.json file into elasticsearch：

curl -u elastic -H"Content-Type: application/json" -XPOST "localhost:9200/web_api_dfr/_bulk" --data-binary @"path\bulk_api.json"

The default password of elasticsearch is elasticadmin

After that you can type: python manage.py runserver

All the js and css are from the tutorial which are in chinese. Would change it in further.
