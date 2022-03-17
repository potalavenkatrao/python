{
  "directions": "post the uuid as a JSON object {\"uuid\": \"[uuid]\", \"email\": \"[your_email]\"} to http://[URL]/[path]", 
  "path": "rQu3SiUCmtfn", 
  "uuid": "d7fa1722-88f8-11ec-b461-b263bbd31520"
}


# -*- coding: utf-8 -*-
import requests
url="https://devops-quiz.eks.ethos-tools.com/"
response = requests.get(url)
data=response.json()

#print(data["uuid"])
path=data["path"]

data_res={"email":"something@ethos.com","uuid":data["uuid"]}
#print(data_res)
url1="https://devops-quiz.eks.ethos-tools.com/"+path
e=requests.post(url1,json=data_res)
print(e.json)