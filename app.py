from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
import pywhatkit

app = FastAPI()

# Serve the HTML form
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r") as file:
        html = file.read()
    return html

# Handle form submission
@app.post("/send-message/")
async def send_message(request: Request, mobile_number: str = Form(...), message: str = Form(...), hours: int = Form(...), minutes: int = Form(...)):
    # Call Pywhatkit function to send WhatsApp message
    pywhatkit.sendwhatmsg(f"+{mobile_number}", message, hours, minutes)
    return {"message": "Message sent successfully!"}