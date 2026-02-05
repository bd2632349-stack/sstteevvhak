from pyrogram import Client as cl
from pyrogram import filters,idle
from pyrogram.types import Message
from pyrogram.raw.types import InputMediaUploadedPhoto
from pyrogram.types import Photo, Video
from pyrogram.raw.types import MessageMediaPhoto, MessageMediaDocument, DocumentAttributeVideo 
from kvsqlite.sync import Client as scl
from pyrogram.errors import FloodWait
import os
db = scl("data.sqlite")
# import logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger(__name__)
# logger.info('This is an information message.')
# logger.warning('This is a warning message.')
# logger.error('This is an error message.')
app = cl("GewtAn", api_id = 9398500, api_hash = "ad2977d673006bed6e5007d953301e13")
def search_text(text):
     if not db.get(f"f_{text[-19:]}"):
         return False
     else:
        id = db.get(f"f_{text[-19:]}")["id"]
        # #print(id)
        return id


def gettime(time):
    import datetime
    date = datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d")
    return date



def search_data(text):
    if not db.get(f"f_{text[-19:]}"):
         return False
    else:
        data = db.get(f"f_{text[-19:]}")
        # #print(id)
        return data

def url(url):
    if url.startswith("https://t.me/"):
        words = url.split('https://t.me/')[1]
        aa = words.split('/s/')
        if len(aa) !=2:return False
        else:return (aa)

    elif url.startswith("t.me/"):
        words = url.split('t.me/')[1]
        aa = words.split('/s/')
        if len(aa) !=2:return False
        else:return (aa)
    else:return False

def checkurl(urltext):
    if urltext.startswith("https://t.me/") or urltext.startswith("t.me/"):

        if url(str(urltext)) != False:
            
            if len(url(str(urltext))) == 2 :
                return "link"
            else:return False
        else:return False
    elif urltext.startswith("@"):return "username"
    else:return False


def addT(text,id,type,data):
    
    try:    
        if not db.get(f"f_{text[-19:]}"):
            d = {"id": id, "type": type, "spoiler": data.media.spoiler,"panned": data.pinned, "public": data.public, "close_friends": data.close_friends, "edited": data.edited, "caption": data.caption, "date": data.date, "expire_date": data.expire_date}
            db.set(f"f_{text[-19:]}", d)
            print(db.get(f"f_{text[-19:]}"))
            return True
        else:
            print(db.get(f"f_{text[-19:]}"))
            return True
    except: return False

async def post_ch(type,text,path,js):
        app = cl("GetAn", api_id = 9398500, api_hash = "ad2977d673006bed6e5007d953301e13", 
             session_string = 'AgCPaOQAtC6wZ32JLWbozuGt8zsRFfivfWDnOZhDcgksuFOl-xBgioHZZ52mc9WsAel_im4LtVrarf2SWGvofowVAthWNAlGqd2bPItRIKOdExDYM8GAEVLraiGLSkclzoZvuwW_u04eXHLj-0rh-hB3hNTqEsyNwULZ4172pDy8PmZtyll3IJy-QwlHy0XNHuLLmV9OWlWyda2eXN7OY3mNS-xDHeDRlSsER69kbtf4IPoMp0wDVpmNLtGUVAXM5DbQ2HLNIC9gO5XsPRefbTkHAKLsRoKAjDGXXtH5wZGiFLLSR3oyHWzT9nPdA0kzZgZUQrlwRiyPLRxhGvXPjndWu6tEjgAAAAFNhSD4AA'
             )
        await app.start() 
        ch_id=-1001627036490
        parts = path.split("/")
        new_p = "/".join(parts[parts.index("downloads"):])
        print(new_p)
        try:
            #print(type)
            if str(type) == "photo":
                try:
                    aa = await app.send_photo(
                        chat_id=ch_id,
                        photo=new_p
                        )
                    print(addT(text=text, type=type, id=aa.id, data=js))
                    os.remove(new_p)
                    return [True,aa.id]
                except:
                     os.remove(new_p)
                     return [False,0]
            else:
                try:
                    aa = await app.send_video(
                        chat_id=ch_id,
                        video=new_p
                        )
                    print(addT(text=text,type=type,id=aa.id,data=js))
                    os.remove(new_p)
                    return [True,aa.id]
                except:
                    os.remove(new_p)
                    return [False,0]
        except:
             return [False,0]
#print(checkurl("https://t.me/Mostiu/s/1"))
#print((url("https://t.me/Mostiu/s/1")))
##print(search_text("BAACAgIAAxUAAWTxM9WwgJSAW7BTrYlF3mBo0BjbAAIGMwACfLeBS72Q-p7wxjxIHgQ"))
#AgACAgIAAxUAAWT53uyV4E
#text = "AgACAgIAAxUAAWT53uyVdd4EB_u0ZLHwafjfAH2nN2AAIG0zEbj4jRSddd-nbanTcPms_tAAgBAAMCAAN3AAceBA"
#che = search_text(text=text)
##print(che)
#text = "AgACAgIAAxUAAWT521J6DruYJroFd8ZYlthlvEy_AAIG0zEbj4jRS-nbanTPms_tAAgBAAMCAAN3AAceBA"
##print(db.get(f"f_{text[-19:]}"))