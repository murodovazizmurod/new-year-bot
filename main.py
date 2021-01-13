from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from PIL import Image, ImageDraw, ImageFont
import time
from datetime import datetime

client = TelegramClient('name', "", "")
client.start()

time1 = ''

def get_left_units():
    """Returns left days/hours/minutes until new year"""
    now = datetime.now()
    days = 31 - now.day
    hours = 23 - now.hour
    minutes = 59 - now.minute
    return (days, hours, minutes)



def tick():
       global time1
       # get the current local time from the PC
       time2 = time.strftime('%H:%M')
       time.sleep(2)
       # if time string has changed, update it
       if time2 != time1:
            time1 = time2
            # img = Image.new('RGB', (640, 640), color = (40, 40, 40))
            img = Image.open("profile.jpg")
            font = ImageFont.truetype('Kingthings Bloone!.TTF', 60)
            font2 = ImageFont.truetype('MerryChristmasStar.ttf', 70)
            d = ImageDraw.Draw(img)
            data = get_left_units()
            d.text((180,70), str(data[0])+" days", font = font, fill = (255,255,255))
            d.text((150,180), str(data[1])+" hours", font = font, fill = (255,255,255))
            d.text((100,310), str(data[2])+" minutes", font = font, fill = (255,255,255))
            d.text((200,500), "to New Year", font = font2, fill = (255,255,255))
            img.save('profile1.jpg')
            upload()


def upload():
    client(DeletePhotosRequest(client.get_profile_photos('me')))
    result = client(UploadProfilePhotoRequest(
        file=client.upload_file('profile1.jpg')
    ))
    tick()

while True:
    tick()

client.run_until_disconnected()
