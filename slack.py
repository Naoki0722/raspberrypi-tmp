import requests

def send():
  headers = {
      'Authorization': 'Bearer TOKEN', # ダミートークン
  }

  message = {
      'message': 'test',
  }

  requests.post('https://notify-api.line.me/api/notify', headers=headers, data=message)


if __name__ == "__main__":
    send()
