import requests
import json
from ProjectDB import ProjectDB
Project = ProjectDB()

# project_url = "http://localhost:5000/projects"
# project_data = {'data':{"project_id":"45","project_name":"ABCD","location":"New York",
#                  "bid_end_time":"2017-11-19","seller_id":"foo","buyer_id":None,
#                  "description":"ABC","creation_time":""}}
#
# api_headers = {'Content-Type': 'application/json'}
#
# project_put = requests.put(project_url, headers=api_headers, data=json.dumps(project_data))
#


seller_url = "http://localhost:5000/sellers"
seller_data = {'data':{"project_id":"45","project_name":"ABCD","location":"New York",
                 "bid_end_time":"2017-11-19","seller_id":"foo","buyer_id":None,
                 "description":"ABC","creation_time":""}}

api_headers = {'Content-Type': 'application/json'}

seller_put = requests.put(seller_url, headers=api_headers, data=json.dumps(seller_data))
print seller_put.status_code
print seller_put.text