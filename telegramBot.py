import requests

def send_to_telegram(message):

    apiToken = '6543953745:AAFwdlmTlHy3nJxThbjanGCQTJgN8KhhFpU'
    chatID = '5340070089'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram("Naber")
