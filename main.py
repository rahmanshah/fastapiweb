import fastapi
import uvicorn

# step 1- creating an app

app = fastapi.FastAPI()

#step 2 - creating a function which will be called when page is requested
@app.get('/')
def index():
    return "Hello World!"

#step 3 - to run our API
uvicorn.run(app)