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
        app = cl("GetAn", api_id = 22988799, api_hash = "9988946e0e68db0ba35bdb0ab3453d29", 
             session_string = '1ApWapzMBu2rHZ_NaXQ6TfKsaiiYQoM_SeKI6xk49iXCbp473hxkraQDHgjRWV96JDqQPneFyVjyWnJo9Yosi16g1bdntrxsIgH31Fq9oVVW2_RdgZ92n9RWYn6gq9d8ZaC6kJCf9qaxcsufuTDdaEN3m9a2NckMmwPbB2FAUSwxNPAfhf8epmsuvxsmZsL449BRTxFNQiaW8kjaLvZI8M2yqpklxicnuvfKjSTqWr43W6xnfEaLQ1oLaKXSI_zyL4PH-Y3bczGl9CJggYSOQxP5kIQlzMgYp0MsFdsL403Oj86gMPVLZnb0ZtSxvJxRz_jsGi96v2rwP31ooDsrhdT00j3OwbxQ='
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
