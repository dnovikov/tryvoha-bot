# Tryvoha Bot
Disclaimer: this is more a convenient naming, rather than a real bot.
It is designed to play air warning sound when detects a certain phrase or a word in a specified Telegram chat.
## Why I created it
Despite we all can see air warning announcements in various Telegram bots, we may not hear physical alarm sound in certain location. I'd put my hands on code when I missed a couple of air warning this way.
This "bot" is designed to solve the issue. Launch it and turn your speakers loud!
## Prerequisites
1. Python 3
1. pip
## Usage
1. Create a Telegram application and obtain it's API ID and hash, as described [here](https://docs.telethon.dev/en/stable/basic/signing-in.html).
1. Find user or channel ID. The simplest way is to use `@getidsbot`. Add it to your contact list and forward a message from a user or a channel you want to listen for.
1. Run `pip install -r requirements.txt`
1. Run the script from command line: `python3 run.py -i <api_id> -s <api_hash> -c <channel_id> -w '<your word>'`. E.g. `python3 run.py -i 12345678 -s xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -c -100000000000000`. The default word to listen for is 'тривога'.
1. Turn your speakers louder!
