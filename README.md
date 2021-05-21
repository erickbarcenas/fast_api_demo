##Official documentation

[fastapi](https://fastapi.tiangolo.com/tutorial/first-steps/)
##Command to run the program
uvicorn app:app --reload
* Custom option:
uvicorn app:app --host 0.0.0.0 --port 8000
uvicorn app:app --host 0.0.0.0 --host IP


## Command to obtain the list of dependencies
pip freeze > requirements.txt

## Uri to open the documentation
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc