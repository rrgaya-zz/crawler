from datasources import scale_serp
import json

result = scale_serp.get_news(query='coronavirus rodoviária bahia')
print(json.dumps(result))
print("Hello World")
