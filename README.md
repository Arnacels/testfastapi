####FastAPI TEST

git clone https://github.com/Arnacels/testfastapi.git .

docker-compose up --build


- POST 

/task/add/

    {
      "task_id": "string", 
      "title": "string", 
      "params": {} #Opional
    }