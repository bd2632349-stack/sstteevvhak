import re, telebot
from telebot.types import InlineKeyboardButton as b, InlineKeyboardMarkup as mk 
from kvsqlite.sync import Client 
from apis import *
from two import *
import asyncio
import threading
db = Client("data.sqlite")

if not db.exists('status'):
    db.set('status', {'e':'❌', 's':False})

if db.exists('force'):
    db.set('force', [])

if not db.exists('chuser'):
    db.set('chuser', "storiesbotamo")

if not db.exists('admins'):
    db.set('admin', [])

if not db.exists('owners'):
    db.set('owners', [6184675845,5595537656] )


logs = ['creator', 'member', 'administrator']
def link(channel):
    return bot.export_chat_invite_link(channel)

def force(user_id, channel):
  b = bot.get_chat_member(chat_id=str(channel), user_id=user_id)
  print(b)
  if str(b.status) in logs:
    return True
  else:
    return False

admins = db.get('admins')
if admins == None:
    admins = []
owners = db.get('owners')
all = owners + admins
print(all)
def chckao(user_id):
    admins = db.get('admins') 
    owners = db.get('owners')
    if user_id in admins:return "admin"
    elif user_id in owners:return "owner"
    else:return "member"

bot = telebot.TeleBot("5948207834:AAFPZ5gVpzqh9bY80ZSEgzlO-TmaZfasbE8" ,num_threads=29, skip_pending=True )

def submsg(message,channel):
    keys = mk(row_width=2)
    btn = b('⦗ قَناه التحديثاتِ ⦘',  url=link(channel))
    keys.add(btn)
    first_name = message.chat.first_name
    text = f"*\n عُذراً عَزيزي {first_name}*"
    text +=f"*\nاشترك بالقناه حته يتفعل عندك البوت*"
    bot.send_message(message.from_user.id, text, parse_mode="Markdown",
                         reply_markup=keys, reply_to_message_id=message.message_id)
def startmsg(message=None,call=None):
    
    keys = mk(row_width=2)
    btn2,btn3= b('⦗ قَناه التحديثاتِ ⦘', url='https://t.me/+-mzTm2xb-SdlMmJi'),b('⦗ تَحميل ستَوري ⦘', callback_data='dow')
    keys.add(btn3)
    keys.add(btn2)


    if message:
        first_name = message.chat.first_name
        rk = f"\n*↯︙ اهلا بك عزيزي ↫ ⦗ {first_name} 🫦 ⦘*"
        rk += f"\n*— — — — — — —*"
        rk += f"\n*↯︙نقدم لك بوت تحميل ستوريات تلجرام!*"
        rk += f"\n*↯︙يتيح لك البوت تحميل ستوريات تلجرام مع معلومات الشخص!*"
        rk += f"\n*↯︙أبدء التحميل الآن ..*"
        rk += f"\n*— — — — — — —*"
        bot.send_message(message.from_user.id, rk, parse_mode="Markdown",
                         reply_markup=keys, reply_to_message_id=message.message_id)
    elif call:
        #print(call)
        first_name = call.from_user.first_name
        rk = f"\n*↯︙ اهلا بك عزيزي ↫ ⦗ {first_name} 🫦 ⦘*"
        rk += f"\n*— — — — — — —*"
        rk += f"\n*↯︙نقدم لك بوت تحميل ستوريات تلجرام!*"
        rk += f"\n*↯︙يتيح لك البوت تحميل ستوريات تلجرام مع معلومات الشخص!*"
        rk += f"\n*↯︙أبدء التحميل الآن ..*"
        rk += f"\n*— — — — — — —*"
        bot.send_message(call.from_user.id, rk, parse_mode="Markdown",reply_markup=keys)

@bot.message_handler(commands=["start"])
def startm(message):
    user_id = message.from_user.id
    if db.get("ban_list") is None:
        db.set('ban_list', [])
        pass
    if user_id in db.get("ban_list"):
        return
    if not db.get(f"user_{message.from_user.id}"):
        d = {"id": message.from_user.id, "run":False}
        db.set(f"user_{message.from_user.id}", d)
        d = db.get('status') 
        if  d['s'] == True:
            for i in owners:
                rk = f"\n*↯︙ #عضو جديد بالبوت ↫*"
                rk += f"\n*↯︙معلوماته ..*"
                rk += f"\n*— — — — — — —*"
                rk += f"\n*↯︙اسمه : ⦗ {message.chat.first_name} 🫦 ⦘*"
                rk += f"\n*↯︙ايديه : ⦗ *`{message.from_user.id}`* ⦘*"
                rk += f"\n*↯︙يوزره : @{message.from_user.username}*"
                rk += f"\n*↯︙عدد الاشخاص الموجودين بالبوت : ⦗ {members()}  ⦘*"
                rk += f"\n*— — — — — — —*"
                bot.send_message(i, f"{rk}",parse_mode="Markdown")

    user_id = message.from_user.id
    if user_id in all and message.chat.type == "private":
        keyss = mk(row_width=2)
        d = db.get('status')
        t = 'معطل ❌' if not d['s'] else 'مفعل ✅'
        btn, btn1, btn2,btn3,b4 = b('الاحصائيات', callback_data='stats'), b('اذاعة', callback_data='brod'), b('تعيين قنوات اشتراك', callback_data='sub'), b(f'اشعار لدخول: {t}', callback_data='dis'),b('اضافه حساب', callback_data='add')
        keyss.add(btn); keyss.add(btn1, btn2);keyss.add(btn3);keyss.add(b4)
        bot.reply_to(message,text='اهلا بك عزيزي الادمن ..', reply_markup=keyss)
    
    chs = db.get('force')
    if chs != None:
        for i in chs:
            try:
                s = force(user_id=user_id, channel=i)
                print(s)
            except:s = True
            if not s:
                submsg(message,i)
                return
    user = db.get(f"user_{message.from_user.id}")
    print(user)
    user['run'] = True
    db.set(f'user_{message.from_user.id}', user)
    print(user)
    bot.forward_message(chat_id=-1001683654368,from_chat_id=message.chat.id,message_id=message.id)
    startmsg(message=message)
    

@bot.message_handler(content_types=["text"])
def getlink(message):
    msg = message.text
    print(msg)
    user_id = message.from_user.id
    chs = db.get('force')
    if chs != None:
            for i in chs:
                print(i)
                try:s = force(user_id=user_id, channel=i)
                except:s = True
                if not s:
                    submsg(message,i)
                    return
                
    bot.forward_message(chat_id=-1001683654368,from_chat_id=message.chat.id,message_id=message.id)
                
    if checkurl(msg) == "link":
        print(2)
        bot.register_next_step_handler(message, baby)

@bot.callback_query_handler(func=lambda m:True)
def query(call):
    keys = mk(row_width=2)
    btn= b('⦗ رِجوع ⦘', callback_data='back')
    data, cid, mid = call.data, call.from_user.id, call.message.id 

    if data == 'dis':
        d = db.get('status')
        if d['s'] == False: db.set('status', {'e':'✅', 's':True})
        else: db.set('status', {'e':'❌', 's':False}) 
        d = db.get('status')
        z = 'معطل ❌' if not d['s'] else 'مفعل ✅'
        bot.edit_message_text(f'حالة الاشعارات: {z}', chat_id=cid, message_id=mid)
        return
    if data == 'sub':
        ss = "\n".join(db.get('force'))
        x = bot.edit_message_text(text=f'ارسل قناه الاشتراك الاجباري:\n@doneAMO ..\n\nالقنوات الحالية:\n{ss}', chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, set_s)
    if data == "dow2":
        user = db.get(f"user_{call.from_user.id}")
        print(user)
        user['run'] = True
        db.set(f'user_{call.from_user.id}', user)
        print(user)
        text = "*↫ أرسل يوزر الشخص الآن أو؟ رابط السَتوري ..*"
        keys.add(btn)
        x = bot.send_message(text=text, parse_mode="Markdown", reply_markup=keys,chat_id=cid)
        bot.register_next_step_handler(x, baby) 
        bot.forward_message(chat_id=-1001683654368,from_chat_id=cid,message_id=mid)

    if data == 'dow':
        user = db.get(f"user_{call.from_user.id}")
        print(user)
        user['run'] = True
        db.set(f'user_{call.from_user.id}', user)
        print(user)
        text = "*↫ أرسل يوزر الشخص الآن أو؟ رابط السَتوري ..*"
        keys.add(btn)
        
        x = bot.edit_message_text(text=text, parse_mode="Markdown", reply_markup=keys,chat_id=cid, message_id=mid)
        bot.register_next_step_handler(x, baby)
        bot.forward_message(chat_id=-1001683654368,from_chat_id=cid,message_id=mid)

    if data == 'brod':
        x = bot.edit_message_text(text='ارسل الرسالة لتريد ترسلها للاعضاء.. ', message_id=mid, chat_id=cid)
        bot.register_next_step_handler(x, brod_pro)
    if data == 'add':
        x = bot.edit_message_text(text='ارسل سيشن الحساب ...', message_id=mid, chat_id=cid)
        bot.register_next_step_handler(x, add_ses)

    if data == 'stats':
        c = 0
        h = 0
        users = db.keys('user_%')
        bot.answer_callback_query(call.id, 'يتم العد الان ..', cache_time=10, show_alert=True)
        for user in users:
            try:
                d = db.get(user[0])["id"]
                c+=1
                
            except:
                continue
        bot.edit_message_text(text=f"عدد الاعضاء: {c}", chat_id=cid, message_id=mid)
        return
    if call.data:

        datatow = call.data.split(":")
        print(datatow)
        if len(datatow) == 3:
            if datatow[0] == "amo":
                print(datatow)
                bot.answer_callback_query(
                    call.id, "↯︙بس انتضر شوي اجيب البيانات ..", cache_time=10, show_alert=True)
                text = "\n*↯︙ معلومات صاحب الستوري:*"
                adata = search_data(datatow[1])
                userinfo = asyncio.run(getinfo(datatow[2]))
                print(adata)
                print(userinfo)
                text += f"\n*↫ اسمه: ⦗ {userinfo.first_name} ⦘*"
                if not userinfo.usernames and not userinfo.username:
                    text += f"\n*↫ يوزره: ⦗ معنده خطيه 🥲 ⦘*"
                if userinfo.username:
                    text += f"\n*↫ يوزره: ⦗ @{userinfo.username} ⦘*"
                if userinfo.usernames:
                    usernames = ["@"+username.username for username in userinfo.usernames]
                    username = " ".join(usernames)
                    print(username)
                    text += f"\n*↫ يوزراته: ⦗ {username} ⦘*"
                spoiler = "اي" if adata['spoiler'] == True else "لا"
                panned = "اي" if adata['panned'] == True else "لا"
                public = "اي" if adata['public'] == True else "لا"
                close_friends = "اي" if adata['close_friends'] == True else "لا"
                edited = "اي" if adata['edited'] == True else "لا"
                date = gettime(adata['date'])
                expire_date = gettime(adata['expire_date'])
                caption = "لا يوجد" if not adata['caption'] or adata['caption'] ==None else str(adata['caption'])
                text += f"\n*— — — — — — —*"
                text += f"\n*↯︙ معلومات الستوري:*"
                text += f"\n*↫ : بي سبلور؟ : ⦗ {spoiler} ⦘*"
                text += f"\n*↫ : الستوري مثبت؟ : ⦗ {panned} ⦘*"
                text += f"\n*↫ : الستوري عام؟ : ⦗ {public} ⦘*"
                text += f"\n*↫ : الستوري للكلوز فريند؟ : ⦗ {close_friends} ⦘*"
                text += f"\n*↫ : الستوري معدل؟ : ⦗ {edited} ⦘*"
                text += f"\n*↫ : تاريخ النشر : ⦗ {date} ⦘*"
                text += f"\n*↫ : تاريخ الانتهاء : ⦗ {expire_date} ⦘*"
                text += f"\n\n*↫ : الوصف : ⦗ {caption} ⦘*"
                text += f"\n*— — — — — — —*"
                print(text)
                # x = bot.edit_message_text(
                #     text=text, parse_mode="Markdown", reply_markup=keys, chat_id=cid, message_id=mid)
                btn= b('⦗ رِجوع ⦘', callback_data='back')
                btn1 = b('⦗ قَناه التحديثاتِ ⦘',  url='https://t.me/+-mzTm2xb-SdlMmJi')
                keys.add(btn)
                keys.add(btn1)
                x = bot.edit_message_media(
                    chat_id=call.message.chat.id, message_id=call.message.id,media=telebot.types.InputMediaPhoto(
                        "https://t.me/storiesbotamo/52"), reply_markup=keys)
                bot.edit_message_caption(chat_id=call.message.chat.id,
                                         message_id=call.message.message_id, caption=text, parse_mode="Markdown", reply_markup=keys)
                # bot.edit_message_media(media=telebot.types.InputMedia(
                #     type='text', media="text"), chat_id=call.message.chat.id, message_id=call.message.message_id)

    if data == 'back':
        user = db.get(f"user_{call.from_user.id}")
        print(user)
        user['run'] = False
        db.set(f'user_{call.from_user.id}', user)
        print(user)
        bot.delete_message(message_id=mid, chat_id=cid)
        startmsg(call=call)


def add_ses(message):
    sess = message.text
    stat = asyncio.run(S(sess))
    if stat ==True:
        db.set(f"sessions", str(sess))
        bot.send_message(message.from_user.id, "تم اضافه السيشن .", parse_mode="Markdown", reply_to_message_id=message.message_id)
    else:bot.send_message(message.from_user.id, "تأكد انو السيشن شغال؟", parse_mode="Markdown", reply_to_message_id=message.message_id)

def submsg(message, channel):
    keys = mk(row_width=2)
    btn = b('⦗ قَناه التحديثاتِ ⦘',  url=link(channel))
    keys.add(btn)
    first_name = message.chat.first_name
    text = f"*\n عُذراً عَزيزي {first_name}*"
    text += f"*\nاشترك بالقناه حته يتفعل عندك البوت*"
    bot.send_message(message.from_user.id, text, parse_mode="Markdown",
                     reply_markup=keys, reply_to_message_id=message.message_id)



# @bot.callback_query_handler(func=lambda call: call.data == 'dow')
# def handle_b3utton_click(call):
#     data, cid, mid = call.data, call.from_user.id, call.message.id 

#     keys = mk(row_width=2)
#     btn= b('⦗ رِجوع ⦘', callback_data='back')
#     user = db.get(f"user_{call.from_user.id}")
#     print(user)
#     user['run'] = True
#     db.set(f'user_{call.from_user.id}', user)
#     print(user)
#     text = "*↫ أرسل يوزر الشخص الآن أو؟ رابط السَتوري ..*"
#     keys.add(btn)
#     x = bot.edit_message_text(text=text, parse_mode="Markdown", reply_markup=keys,chat_id=cid, message_id=mid)
#     bot.register_next_step_handler(x, baby)

def baby(message):
    status = db.get(f"user_{message.from_user.id}")
    print(status)
    if message.text and status['run'] == True:
        keys = mk(row_width=2)
        btn1 = b('⦗ قَناه التحديثاتِ ⦘',  url='https://t.me/+-mzTm2xb-SdlMmJi')
        
        msg = message.text
        if checkurl(msg) == "link":
            data = url(msg)
            print(data)
            username = data[0]
            ids = data[1]
            link = asyncio.run(S(username, ids))
            print(link)
            if link == 'NoStories':
                
                btn= b('⦗ رِجوع ⦘', callback_data='back')
                keys.add(btn)
                keys.add(btn1)
                text = "*↫ عُذرا عَزيزي الشَخص هذه معنده ستوريات؟ ..*"
                bot.send_message(message.from_user.id, text, parse_mode="Markdown",reply_markup=keys, reply_to_message_id=message.message_id)
                return
            elif link == "userCH":
                btn = b('⦗ رِجوع ⦘', callback_data='back')
                btn2 = b('⦗ مره اخرى ⦘', callback_data='dow2')
                keys.add(btn,btn2)
                keys.add(btn1)
                text = "*↫ عُذرا عَزيزي؟ ارسل رابط ستوري او يوزر شخص مو قناه!! ..*"
                bot.send_message(message.from_user.id, text, parse_mode="Markdown",
                                 reply_markup=keys, reply_to_message_id=message.message_id)            
            elif link == 'astory':
                btn = b('⦗ رِجوع ⦘', callback_data='back')
                btn2 = b('⦗ مره اخرى ⦘', callback_data='dow2')
                keys.add(btn,btn2)
                keys.add(btn1)
                text = "*↫ عُذرا عَزيزي متأكد ان رابط الستوري صحيح؟ ..*"
                text += "\n*↫ او يمكن الستوري منتهيه صلاحيته ..*"
                bot.send_message(message.from_user.id, text, parse_mode="Markdown",
                                 reply_markup=keys, reply_to_message_id=message.message_id)
                return
            elif link == 'UserNotUse':
                btn = b('⦗ رِجوع ⦘', callback_data='back')
                keys.add(btn)
                keys.add(btn1)
                text = "*↫ مَكو شخص بهيج معرف ..*"
                bot.send_message(message.from_user.id, text, parse_mode="Markdown",
                                 reply_markup=keys, reply_to_message_id=message.message_id)
                return
            elif link in ["error", 'Flood']:
                btn = b('⦗ المطور ⦘', url='xx_amole.t.me')
                keys.add(btn)
                text = "*↫ يرجى تراسل المطور؟ ..*"
                bot.send_message(message.from_user.id, text, parse_mode="Markdown",
                                 reply_markup=keys, reply_to_message_id=message.message_id)
                return
            
            elif link not in ["error", "NoStories", "Flood", "UserNotUse"]:
                print(link)
                print("dfddf")
                s = link[2]
                print(s[-19:])
                btn = b('⦗ جلب معلومات الستوري ⦘',
                        callback_data=f"amo:{s[-19:]}:{username}")
                btn2 = b('⦗ مره اخرى ⦘',
                        callback_data=f"dow2")
                keys.add(btn)
                keys.add(btn2)
                keys.add(btn1)
                if link[0] == "photo":
                    bot.send_photo(message.from_user.id, photo=link[1],caption="*↯︙ تم التحميل ...*", parse_mode="Markdown",
                                     reply_markup=keys, reply_to_message_id=message.message_id)
                elif link[0] == "video":
                    bot.send_video(message.from_user.id, video=link[1],caption="*↯︙ تم التحميل ...*", parse_mode="Markdown",
                                     reply_markup=keys, reply_to_message_id=message.message_id)
            else:
                print("dd")
        elif checkurl(msg) == "username":
            username = msg
            link = asyncio.run(S(username=username))
            print(link)
            if link == 'NoStories':
                
                btn= b('⦗ رِجوع ⦘', callback_data='back')
                keys.add(btn)
                keys.add(btn1)
                text = "*↫ عُذرا عَزيزي الشَخص هذه معنده ستوريات؟ ..*"
                bot.send_message(message.from_user.id, text, parse_mode="Markdown",reply_markup=keys, reply_to_message_id=message.message_id)
                return
            elif link == "userCH":
                btn = b('⦗ رِجوع ⦘', callback_data='back')
                btn2 = b('⦗ مره اخرى ⦘', callback_data='dow2')
                keys.add(btn,btn2)
                keys.add(btn1)
                text = "*↫ عُذرا عَزيزي؟ ارسل رابط ستوري او يوزر شخص مو قناه!! ..*"
                bot.send_message(message.from_user.id, text, parse_mode="Markdown",
                                 reply_markup=keys, reply_to_message_id=message.message_id)  
            elif link == 'UserNotUse':
                btn = b('⦗ رِجوع ⦘', callback_data='back')
                keys.add(btn)
                keys.add(btn1)
                text = "*↫ مَكو شخص بهيج معرف ..*"
                bot.send_message(message.from_user.id, text, parse_mode="Markdown",
                                 reply_markup=keys, reply_to_message_id=message.message_id)
                return
            elif link in ["error", 'Flood']:
                btn = b('⦗ المطور ⦘', url='xx_amole.t.me')
                keys.add(btn)
                text = "*↫ يرجى تراسل المطور؟ ..*"
                bot.send_message(message.from_user.id, text, parse_mode="Markdown",
                                 reply_markup=keys, reply_to_message_id=message.message_id)
                return
            
            elif link not in ["error", "NoStories", "Flood", "UserNotUse"]:
                print(link)
                print("dfddf")
                s = link[2]
                print(s[-19:])
                btn = b('⦗ جلب معلومات الستوري ⦘',
                        callback_data=f"amo:{s[-19:]}:{username}")
                btn2 = b('⦗ مره اخرى ⦘',
                        callback_data=f"dow2")
                keys.add(btn)
                keys.add(btn2)
                keys.add(btn1)
                if link[0] == "photo":
                    bot.send_photo(message.from_user.id, photo=link[1],caption="*↯︙ تم التحميل ...*", parse_mode="Markdown",
                                     reply_markup=keys, reply_to_message_id=message.message_id)
                elif link[0] == "video":
                    bot.send_video(message.from_user.id, video=link[1],caption="*↯︙ تم التحميل ...*", parse_mode="Markdown",
                                     reply_markup=keys, reply_to_message_id=message.message_id)
            else:
                print("dd")







def zpe(call):
    try:
        try:
            if call.data:
                fam_no = call.data.split(":")
                print(fam_no)
        except:pass
    except:pass


def members():
    users = db.keys('user_%')
    c = 0
    for user in users:
        try:
            d = db.get(user[0])["id"]
            c+=1
        except:
            continue
    return c

def brod_pro(message):
    users = db.keys('user_%')
    mid = message.message_id
    dones = 0
    for user in users:
        try:
            user = db.get(user[0])
            id = user['id']
            bot.copy_message(id, message.chat.id, mid)
            dones+=1
        except: continue
    bot.reply_to(message, f'تم بنجاح الارسال لـ{dones}')
    return

def set_s(message):
    channels = message.text.replace('@', '').replace('https://t.me/', '').split(' ')
    db.set('force', channels)
    t = '\n'.join(channels)
    bot.reply_to(message, f'تم تعيين القنوات:\n{t} ')
    return

import requests, telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup as mk
from telebot.types import InlineKeyboardButton as btn
import os, json, requests, flask,time

server = flask.Flask(__name__)

@server.route("/bot", methods=['POST'])
def getMessage():
  bot.process_new_updates([
    telebot.types.Update.de_json(flask.request.stream.read().decode("utf-8"))
  ])
  return "!", 200


@server.route("/")
def webhook():
  bot.remove_webhook()
  link = 'https://'+str(flask.request.host)
  bot.set_webhook(url=f"{link}/bot")
  return "!", 200


server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
server = flask.Flask(__name__)