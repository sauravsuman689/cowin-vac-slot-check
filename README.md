# cowin-vac-slot-check

##Let's fight with covid19 and get vaccinated..!!

This project is based on India cowin public API to check the available slots for covid19 vaccine and send the alert if any slot is available in any district to telegram bot channel.
This program is written for 18 years of people. Program can be updated for 45 years of people also.

cowin public api url - https://apisetu.gov.in/public/marketplace/api/cowin

***To Create the Telegram Bot***

Firstly, create a bot using Telegram BotFather. To create a BotFather follow the below steps –

    1. Open the telegram app and search for @BotFather.
    2. Click on the start button or send “/start”.
    3. Then send “/newbot” message to set up a name and a username(Note - username should be unique else it will throw the error messsage).
    4. After setting name and username BotFather will give you an API token which is your bot token.
    5. Now, search your username with @username in the telegram app and click start. Send a message in the chat.
    6. Run the below url in the browser by adding you bot API token in the url.

        https://api.telegram.org/bot{API-token}/getUpdates

        You will see similar output in browser :

        {"ok":true,"result":[{"update_id":525205765,
        "message":{"message_id":2,"from":{"id":$$$$,"is_bot":false,"first_name":"$$$$","last_name":"$$$$","language_code":"en"},"chat":{"id":$$$$,"first_name":"$$$$","last_name":"$$$$","type":"private"},"date":1621163598,"text":"Hello"}}]}

        Here, in the above output you will get the chatID i.e. the value of "id".

***Instruction to run the program***

    * Update the bot API token and chatID in the telegramalert.py file.
    * Update your district codes in the check-slots-main.py file.

Run the check-slots-main.py scipt to get the alert notification.
    
NOTE - Here the condition in the code is if the age limit if equal to 18 and slot available is 
       great than or equal to 1 then it will send the alert to telegram.










