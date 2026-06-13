#----------------https method---------------------

#put= changing the entire data
#patch = partial data change
#delete=delete the data
#get = we recive the data from database
#post = sending the data to the databases



from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def home():
    return{"message":"Welcome Fastapi"}



@app.get("/about")
def home():
    return{"message":"this website is about play"}


@app.get("/contact")
def home():
    return{"message":"this website is about contact"}


@app.get("/policy")
def home():
    return{"message":"this website is about policy"}