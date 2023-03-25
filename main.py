from flask import Flask
from flask_postmark import Postmark
import os


# init flask app
app = Flask(__name__)

# set config vars
app.config["POSTMARK_SERVER_TOKEN"] = os.environ.get("email_server_token")
postmark = Postmark(app)

@app.route("/send", methods=["GET"])
def send_email():
    postmark.send(
        From=os.environ.get("sender_email"),
        To=os.environ.get("receiver_email"),
        Subject="Postmark Test",
        HtmlBody="<html><body>This is a test email</body></html>"
    )

    return "OK"
