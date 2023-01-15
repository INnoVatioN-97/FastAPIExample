from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/")
async def root():
    return {"status": 200, "message": "헬로!"}


@app.post("/image/")
async def uploadImage(image= Form()):
    print('uploadImage >>> image has been arrived! ',image)
    return {"status": 200, "message": "이미지전송됨!","data": image}
  