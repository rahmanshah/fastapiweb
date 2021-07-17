import fastapi
import uvicorn

# step 1- creating an app

app = fastapi.FastAPI()

#step 2 - creating a function which will be called when page is requested

@app.get('/')
def index():
    content = """
    <h1>Hello FastAPI Web App</h1>
    <div>Here will our code will live</div>
    """
    resp = fastapi.responses.HTMLResponse(content)
    return resp

#step 3 - to run our API when we want to run locally

if __name__ == '__main__' :
    uvicorn.run(app)

#step 4 - to run app in prod, use command uviorn maodule:variable which is in our case uvicorn main:app