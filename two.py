import pyrogram,re,time
from pyrogram import Client as cli
from pyrogram.types import Message
from pyrogram.raw.types import InputMediaUploadedPhoto
from pyrogram.types import Photo, Video
import asyncio
from pyrogram.raw.types import MessageMediaPhoto, MessageMediaDocument, DocumentAttributeVideo 
from apis import *
async def infoS(username=None,idS=None):
            ap = cli("GetAn", api_id=9398500, api_hash="ad2977d673006bed6e5007d953301e13",
             session_string='AgCPaOQAtC6wZ32JLWbozuGt8zsRFfivfWDnOZhDcgksuFOl-xBgioHZZ52mc9WsAel_im4LtVrarf2SWGvofowVAthWNAlGqd2bPItRIKOdExDYM8GAEVLraiGLSkclzoZvuwW_u04eXHLj-0rh-hB3hNTqEsyNwULZ4172pDy8PmZtyll3IJy-QwlHy0XNHuLLmV9OWlWyda2eXN7OY3mNS-xDHeDRlSsER69kbtf4IPoMp0wDVpmNLtGUVAXM5DbQ2HLNIC9gO5XsPRefbTkHAKLsRoKAjDGXXtH5wZGiFLLSR3oyHWzT9nPdA0kzZgZUQrlwRiyPLRxhGvXPjndWu6tEjgAAAAFNhSD4AA'
             )
            await ap.start()
 #       try:
            try:
                users = await ap.get_users(username)
            except (pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied,pyrogram.errors.exceptions.bad_request_400.UsernameInvalid):
                return("UserNotUse")
            except (FloodWait):
                return("Flood")
            peer = await ap.resolve_peer(peer_id=users.id)
            #print('\n')
            res = await ap.invoke(
            pyrogram.raw.functions.stories.GetUserStories(
            user_id=peer,
            )
            )
            le = ((len(res.stories.stories)))
            indexn = None
            if le == 0:
                return("NoStories")
            else:
                if idS != None:
                    for index, i in enumerate(res.stories.stories):
                        #print(i)
                        aa = res.stories.stories[int(index)].id
                        #print(aa)
                        #print(index)
                        if int(aa) == int(idS):
                            indexn = index
                        if index == le and int(aa) != int(idS):
                            indexn = None
                        # #print(aa)
                else:
                    indexn = le - 1

                if idS !=None:i = res.stories.stories[indexn]
                else:i = res.stories.stories[int(indexn)]
                return(i)
#        except:return("error")


async def getinfo(user):
    ap = cli("GetAn", api_id=9398500, api_hash="ad2977d673006bed6e5007d953301e13",
                   session_string='AgCPaOQAtC6wZ32JLWbozuGt8zsRFfivfWDnOZhDcgksuFOl-xBgioHZZ52mc9WsAel_im4LtVrarf2SWGvofowVAthWNAlGqd2bPItRIKOdExDYM8GAEVLraiGLSkclzoZvuwW_u04eXHLj-0rh-hB3hNTqEsyNwULZ4172pDy8PmZtyll3IJy-QwlHy0XNHuLLmV9OWlWyda2eXN7OY3mNS-xDHeDRlSsER69kbtf4IPoMp0wDVpmNLtGUVAXM5DbQ2HLNIC9gO5XsPRefbTkHAKLsRoKAjDGXXtH5wZGiFLLSR3oyHWzT9nPdA0kzZgZUQrlwRiyPLRxhGvXPjndWu6tEjgAAAAFNhSD4AA')
    await ap.start()
    try:
        users = await ap.get_users(user)
        return users
    except (pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied, pyrogram.errors.exceptions.bad_request_400.UsernameInvalid):
        return ("UserNotUse")
    except (FloodWait):
        return ("Flood")

async def S(username=None, idS=None):
            ap = cli("GetAn", api_id = 9398500, api_hash = "ad2977d673006bed6e5007d953301e13", 
             session_string = 'AgCPaOQAtC6wZ32JLWbozuGt8zsRFfivfWDnOZhDcgksuFOl-xBgioHZZ52mc9WsAel_im4LtVrarf2SWGvofowVAthWNAlGqd2bPItRIKOdExDYM8GAEVLraiGLSkclzoZvuwW_u04eXHLj-0rh-hB3hNTqEsyNwULZ4172pDy8PmZtyll3IJy-QwlHy0XNHuLLmV9OWlWyda2eXN7OY3mNS-xDHeDRlSsER69kbtf4IPoMp0wDVpmNLtGUVAXM5DbQ2HLNIC9gO5XsPRefbTkHAKLsRoKAjDGXXtH5wZGiFLLSR3oyHWzT9nPdA0kzZgZUQrlwRiyPLRxhGvXPjndWu6tEjgAAAAFNhSD4AA'
             )
            await ap.start()
    # ap = cli("leolhl", api_id=20615411, api_hash="58ddcd6aa11aca86f0054da0b5deb370", session_string="AgCPaOQAtC6wZ32JLWbozuGt8zsRFfivfWDnOZhDcgksuFOl-xBgioHZZ52mc9WsAel_im4LtVrarf2SWGvofowVAthWNAlGqd2bPItRIKOdExDYM8GAEVLraiGLSkclzoZvuwW_u04eXHLj-0rh-hB3hNTqEsyNwULZ4172pDy8PmZtyll3IJy-QwlHy0XNHuLLmV9OWlWyda2eXN7OY3mNS-xDHeDRlSsER69kbtf4IPoMp0wDVpmNLtGUVAXM5DbQ2HLNIC9gO5XsPRefbTkHAKLsRoKAjDGXXtH5wZGiFLLSR3oyHWzT9nPdA0kzZgZUQrlwRiyPLRxhGvXPjndWu6tEjgAAAAFNhSD4AA")
    # try:
            #print(username)
            #print(idS)
            try:
                users = await ap.get_users(username)
            except (pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied, pyrogram.errors.exceptions.bad_request_400.UsernameInvalid):
                return ("UserNotUse")
            except(IndexError):return("userCH")
            except (FloodWait):
                return ("Flood")

            # #print(users)
            # #print(users)
            #print(users)

            peer = await ap.resolve_peer(peer_id=users.id)
            # #print(peer)
            res = await ap.invoke(
                pyrogram.raw.functions.stories.GetUserStories(
                    user_id=peer,
                )
            )
            # #print(res)
            le = ((len(res.stories.stories)))
            #print(le)
            indexn = None
            # #print(indexn)
            if le == 0:
                return ("NoStories")
            else:
                if idS != None:
                    for index, i in enumerate(res.stories.stories):
                        #print(i)
                        aa =  res.stories.stories[int(index)].id
                        #print(aa)
                        #print(index)
                        if int(aa) == int(idS):
                            indexn = index
                        if index == le and int(aa) != int(idS):
                            indexn = None
                        # #print(aa)
                else:
                    indexn = le - 1
                    # #print(indexn)
                    # #print(le)
                    # #print(res.stories.stories[int(indexn)])
                #print(indexn)
                if idS != None:
                    #print(idS)
                    try:
                        i =  res.stories.stories[indexn]
                    except:return("astory")
                else:
                    try:
                        i = res.stories.stories[int(indexn)]
                    except:
                        return ("astory")
                ch_id = -1001627036490
                if isinstance(i.media, MessageMediaPhoto):
                    file =  Photo._parse(None, i.media.photo)
                    # #print(file)
                    file_id = file.file_id
                    # #print(file_id)
                    che = search_text(file_id)
                    # #print(file.file_id[-19:])
                    # #print(che)
                    # #print(file.file_id)
                    if che == False:
                        lista = await ap.download_media(file_id)
                        post = await post_ch(
                            type="photo",
                            text=file_id,
                            path=lista,
                            js=i
                        )
                        #print(post)
                        if post[0] == True:
                            return ["photo", f"https://t.me/storiesbotamo/{post[1]}", file_id]
                    else:
                        return (["photo", f"t.me/storiesbotamo/{search_text(file.file_id)}", file_id])

                if isinstance(i.media, MessageMediaDocument):
                    file = Video._parse(
                        None, i.media.document, DocumentAttributeVideo, None)
                    file_id = file.file_id
                    # #print(file_id)
                    che = search_text(file_id)
                    # #print(file.file_id[-19:])
                    # #print(che)
                    # #print(file.file_id)
                    if che == False:
                        lista = await ap.download_media(file_id)
                        post = await post_ch(
                            type="video",
                            text=file_id,
                            path=lista,
                            js=i
                        )
                        #print(post)
                        if post[0] == True:
                            return ["video", f"https://t.me/storiesbotamo/{post[1]}", file_id]

                    else:
                        return (["video", f"t.me/storiesbotamo/{search_text(file.file_id)}", file_id])
    # except:
    #         return ("error")
#       https://t.me/raitp/s/16
# link = asyncio.run(S("raitp", 16))
# #print(link)


# userinfo = asyncio.run(getinfo("@aaaba"))

# usernames = ["@"+username.username for username in userinfo.usernames]
# print(usernames)
# print(userinfo)