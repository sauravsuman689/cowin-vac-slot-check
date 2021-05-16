import requests

def telegram_bot_sendtext(bot_message):
    
    ## Add your bot token and bot chatID below
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

#telegram_bot_sendtext("hello saurav")