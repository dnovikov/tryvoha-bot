import asyncio
import argparse
from playsound import playsound
from telethon import TelegramClient, events

async def main():

    parser = argparse.ArgumentParser(description='Play a warning signal when a specified word appears in a Telegram channel.')
    parser.add_argument('-i', '--api_id', metavar='api_id', type=int, required=True,
                        help='Telegram API ID')
    parser.add_argument('-s', '--api_hash', metavar='api_hash', type=ascii, required=True,
                        help='Telegram API hash')
    parser.add_argument('-c', '--channel_id', metavar='channel_id', type=int, required=True,
                        help='Telegram entity (typically channel or user) ID')
    parser.add_argument('-p', '--phrase', nargs='?', default='тривога',
                        help='phrase or word to look for')

    args = parser.parse_args()
    print(args)

    client = TelegramClient('anon', args.api_id, args.api_hash)

    @client.on(events.NewMessage(chats=[args.channel_id]))
    async def alarm_handler(event):
        if args.phrase in event.raw_text:
            print(event.raw_text)
            playsound('air-warning.mp3')

    async with client:
        # This is required to update the telethon's cache.
        await client.get_dialogs()

        await client.run_until_disconnected()

asyncio.run(main())
