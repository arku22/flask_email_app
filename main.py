from postmarker.core import PostmarkClient
from dotenv import load_dotenv
import os


# load env variables
load_dotenv()

postmark = PostmarkClient(server_token=os.environ.get('email_server_token'))
postmark.emails.send(
    From=os.environ.get('sender_email'),
    To=os.environ.get('receiver_email'),
    Subject='Hello from Postmark',
    HtmlBody='<strong>Hello</strong> dear postmark user.'
)
