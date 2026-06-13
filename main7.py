from fastapi import FastAPI
app = FastAPI()

@app.post("/create_user")
def create_user(name:str, age: int, clg:str, sem=int):
    return{
        "message": "User Created",
        "data": {
            "name": name,
            "age": age,
            "clg":clg,
            "sem":sem
        }
    
    }
    
    
    
    
    
    
#-=-=-=-=-=-=http://127.0.0.1:8000/docs-===-=-=-=-=--=--=-=-=-=-=-=