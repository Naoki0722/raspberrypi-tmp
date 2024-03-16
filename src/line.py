import os

import requests
from dotenv import load_dotenv


class Line:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv("LINE_TOKEN")
        self.url = "https://notify-api.line.me/api/notify"

    def send(self, message):
        try:
            requests.post(
                self.url,
                headers={"Authorization": f"Bearer {self.token}"},
                data={"message": message},
            )
        except Exception as e:
            print(e)
            return
