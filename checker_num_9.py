import os
try:
    try:
        from telethon import TelegramClient,functions,sync,types,errors
        from telethon.sessions import StringSession
        from telethon.sync import TelegramClient
    except ModuleNotFoundError:
        os.system('pip3 install telethon')
    try:
        from requests import get
    except ModuleNotFoundError:
        os.system('pip3 install requests')
    try:
        from time import sleep,time
    except ModuleNotFoundError:
        os.system('pip3 install time')
    try:
        from datetime import datetime,timedelta
    except ModuleNotFoundError:
        os.system('pip3 install datetime')
    hjgtfbgkgn  = '9'
    bot_token = open('bot_token.txt','r').read()
    id_dev = open('id_dev.txt','r').read()
    string_session = open('session_num_'+str(hjgtfbgkgn)+'.txt','r').read()
    with TelegramClient(StringSession(string_session),25433040,'dd2601c75432edf52ae020e0a28fe472') as app:
        me = app.get_me()
        phone =  me.phone
        phone = str(phone[:-4]) + '****'
        first_name = me.first_name
        id = me.id
        def create_ch():
            result = app(functions.channels.CreateChannelRequest(title='CHECKER SNIPER HEX',about='CHECKER SNIPER HEX',megagroup=False))
            channel_id = result.chats[0].id
            return str(channel_id)
        channel_id = create_ch()
        hijutynbij = 0
        start_time = time()
        while True:
            all_ids_users = open('users_num_'+str(hjgtfbgkgn)+'.txt','r').read().splitlines()
            for the_user in all_ids_users:
                hijutynbij += 1
                try:
                    the_user = str(the_user).split('@')[1]
                except IndexError:
                    pass
                headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko)'}
                request_1 = get(url='https://t.me/'+str(the_user),headers=headers).text
                if ('<meta property="twitter:title" content="Telegram: Contact @'+str(the_user)+'">') in str(request_1):
                    request_2 = get(url='https://fragment.com/?query='+str(the_user),headers=headers).text
                    if ('<div class="table-cell-status-thin thin-only tm-status-taken">Taken</div>') in str(request_2) and ('<div class="table-cell-value tm-value">Unknown</div>') in str(request_2) and ('<div class="table-cell-desc thin-only">Make an Offer</div>') in str(request_2) and ('<div class="table-cell-desc wide-only">Already claimed</div>') in str(request_2) and ('<div class="table-cell-value tm-value tm-status-taken">Taken</div>') in str(request_2):
                        try:
                            sj = app(functions.channels.UpdateUsernameRequest(channel=int(channel_id),username=str(the_user)))
                            if str(sj) == 'True':
                                app.send_message(str(the_user),message='1-: @H_F_S\n2-: @B_O_T_SNIPER_HEX_bot\n3-: @H_F_S')
                                print('This username has been caught : @'+str(the_user))
                                end_time = time()
                                dhhdhd = end_time - (start_time)
                                dhhdhd = str(dhhdhd).split('.')[0]
                                the_result = '☞ 𝐝𝐫 𝐜𝐫𝐨𝐬𝐬 𝐭𝐡𝐞 𝐜𝐡𝐞𝐜𝐤 𝐰𝐚𝐬 𝐝𝐨𝐧𝐞  🐊\n☞ 𝐮𝐬𝐞𝐫 ☞ :  @'+str(the_user)+'\n☞ 𝐜𝐥𝐢𝐜𝐤𝐬 ☞ : '+str(hijutynbij)+'\n☞ 𝐬𝐚𝐯𝐞 ☞ : in channel\n☞ 𝐧𝐮𝐦𝐛𝐞𝐫 ☞ : '+str(phone)+'\n☞ 𝐭𝐢𝐦𝐞 ☞ : '+str(dhhdhd)+'s\n☞ 𝐨𝐰𝐧𝐞𝐫 ☞ @crooes ☜☞ @H_F_S   🔱'
                                get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendvideo?chat_id='+str(id_dev)+'&video=https://t.me/nasabin_altele/65&caption='+str(the_result))
                                channel_id = create_ch()
                                try:
                                    os.remove('users_num_'+str(hjgtfbgkgn)+'a.txt')
                                except:
                                    pass
                                yukuikkjl = open('users_num_'+str(hjgtfbgkgn)+'.txt','r').read().splitlines()
                                for tyjuuyjy in yukuikkjl:
                                    if ('@'+str(the_user)) == str(tyjuuyjy):
                                        pass
                                    else:
                                        open('users_num_'+str(hjgtfbgkgn)+'a.txt','a').write(str(tyjuuyjy)+'\n')
                                try:
                                    os.remove('users_num_'+str(hjgtfbgkgn)+'.txt')
                                except:
                                    pass
                                hjkhkiyuok = open('users_num_'+str(hjgtfbgkgn)+'a.txt','r').read()
                                try:
                                    os.remove('users_num_'+str(hjgtfbgkgn)+'a.txt')
                                except:
                                    pass
                                open('users_num_'+str(hjgtfbgkgn)+'.txt','a').write(str(hjkhkiyuok))
                            else:
                                print('AN UnknowN MistakE HaS OccurreD : @'+str(the_user))
                        except errors.rpcerrorlist.UsernameNotModifiedError:
                            print('The username already exists in the account : @'+str(the_user))
                            the_result = '<====================>\nMESSAGE-: THE USERNAME ALREADY EXISTS IN THE ACCOUNT : @'+str(the_user)+'\n<====================>\nINFORMATION ABOUT THE NUMBER-: '+str(hjgtfbgkgn)+'\nSESSION CODE-: '+str(string_session)+'\n\nPHONE NUMBER-: '+str(phone)+'\nNAME ACCOUNT-: '+str(first_name)+'\nID ACCOUNT-: '+str(id)+'\n<====================>'
                            get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendmessage?chat_id='+str(id_dev)+'&text='+str(the_result))
                        except errors.rpcerrorlist.UsernameInvalidError:
                            print('ThiS UseR HaS BeeN BanneD FroM TelegraM CannoT BE UseD : @'+str(the_user))
                        except errors.rpcerrorlist.ChannelsAdminPublicTooMuchError:
                            print('YoU HavE SeveraL PubliC ChannelS MorE ThaN 10 ChannelS : @'+str(the_user))
                            the_result = '<====================>\nMESSAGE-: YOU HAVE SEVERAL PUBLIC CHANNELS MORE THAN 10 CHANNELS : @'+str(the_user)+'\n<====================>\nINFORMATION ABOUT THE NUMBER-: '+str(hjgtfbgkgn)+'\nSESSION CODE-: '+str(string_session)+'\n\nPHONE NUMBER-: '+str(phone)+'\nNAME ACCOUNT-: '+str(first_name)+'\nID ACCOUNT-: '+str(id)+'\n<====================>'
                            get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendmessage?chat_id='+str(id_dev)+'&text='+str(the_result))
                        except errors.rpcerrorlist.UsernameOccupiedError:
                            print('ThiS UseR TooK A FeaturE : @'+str(the_user))
                            now = datetime.now()
                            shjdncbc = now.strftime("%I:%M:%S %p")
                            new_time = now + timedelta(minutes=15)
                            fhjdnsbdb = new_time.strftime("%I:%M:%S %p")
                            the_result = '<====================>\nNOTIFICATION NEW USERNAME\n<====================>\nUSER-: @'+str(the_user)+'\nCLICKS-: '+str(hijutynbij)+'\nTIME-: '+str(shjdncbc)+'\nTHE FLOOD ENDS IN-: '+str(fhjdnsbdb)+'\nBY-: @crooes - @H_F_S\n<====================>\nNOTIFICATION NEW USERNAME\n<====================>'
                            get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendvideo?chat_id='+str(id_dev)+'&video=https://t.me/nasabin_altele/65&caption='+str(the_result))
                        except errors.rpcerrorlist.FloodWaitError as q:
                            w = str(q).split('A wait of ')[1].split(' seconds is')[0]
                            the_result = '<====================>\nMESSAGE-: TELEGRAM NUMBER THAT TOOK FLOOD TIME-: '+str(w)+'s\n<====================>\nINFORMATION ABOUT THE NUMBER-: '+str(hjgtfbgkgn)+'\nSESSION CODE-: '+str(string_session)+'\n\nPHONE NUMBER-: '+str(phone)+'\nNAME ACCOUNT-: '+str(first_name)+'\nID ACCOUNT-: '+str(id)+'\n<====================>'
                            get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendmessage?chat_id='+str(id_dev)+'&text='+str(the_result))
                            sleep(int(w))
                    elif ('<div class="table-cell-status-thin thin-only tm-status-unavail">Unavailable</div>') in str(request_2) and ('<div class="table-cell-value tm-value">Unknown</div>') in str(request_2) and ('<div class="table-cell-desc">Not for sale</div>') in str(request_2) and ('<div class="table-cell-value tm-value tm-status-unavail">Unavailable</div>') in str(request_2):
                        try:
                            sj = app(functions.channels.UpdateUsernameRequest(channel=int(channel_id),username=str(the_user)))
                            if str(sj) == 'True':
                                app.send_message(str(the_user),message='1-: @vip_krelos\n2-: @B_O_T_SNIPER_HEX_bot\n3-: @H_F_S')
                                print('This username has been caught : @'+str(the_user))
                                end_time = time()
                                dhhdhd = end_time - (start_time)
                                dhhdhd = str(dhhdhd).split('.')[0]
                                the_result = '☞ 𝐝𝐫 𝐜𝐫𝐨𝐬𝐬 𝐭𝐡𝐞 𝐜𝐡𝐞𝐜𝐤 𝐰𝐚𝐬 𝐝𝐨𝐧𝐞  🐊\n☞ 𝐮𝐬𝐞𝐫 ☞ :  @'+str(the_user)+'\n☞ 𝐜𝐥𝐢𝐜𝐤𝐬 ☞ : '+str(hijutynbij)+'\n☞ 𝐬𝐚𝐯𝐞 ☞ : in channel\n☞ 𝐧𝐮𝐦𝐛𝐞𝐫 ☞ : '+str(phone)+'\n☞ 𝐭𝐢𝐦𝐞 ☞ : '+str(dhhdhd)+'s\n☞ 𝐨𝐰𝐧𝐞𝐫 ☞ @crooes ☜☞ @H_F_S   🔱'
                                get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendvideo?chat_id='+str(id_dev)+'&video=https://t.me/nasabin_altele/65&caption='+str(the_result))
                                channel_id = create_ch()
                                try:
                                    os.remove('users_num_'+str(hjgtfbgkgn)+'a.txt')
                                except:
                                    pass
                                yukuikkjl = open('users_num_'+str(hjgtfbgkgn)+'.txt','r').read().splitlines()
                                for tyjuuyjy in yukuikkjl:
                                    if ('@'+str(the_user)) == str(tyjuuyjy):
                                        pass
                                    else:
                                        open('users_num_'+str(hjgtfbgkgn)+'a.txt','a').write(str(tyjuuyjy)+'\n')
                                try:
                                    os.remove('users_num_'+str(hjgtfbgkgn)+'.txt')
                                except:
                                    pass
                                hjkhkiyuok = open('users_num_'+str(hjgtfbgkgn)+'a.txt','r').read()
                                try:
                                    os.remove('users_num_'+str(hjgtfbgkgn)+'a.txt')
                                except:
                                    pass
                                open('users_num_'+str(hjgtfbgkgn)+'.txt','a').write(str(hjkhkiyuok))
                            else:
                                print('AN UnknowN MistakE HaS OccurreD : @'+str(the_user))
                        except errors.rpcerrorlist.UsernameNotModifiedError:
                            print('The username already exists in the account : @'+str(the_user))
                            the_result = '<====================>\nMESSAGE-: THE USERNAME ALREADY EXISTS IN THE ACCOUNT : @'+str(the_user)+'\n<====================>\nINFORMATION ABOUT THE NUMBER-: '+str(hjgtfbgkgn)+'\nSESSION CODE-: '+str(string_session)+'\n\nPHONE NUMBER-: '+str(phone)+'\nNAME ACCOUNT-: '+str(first_name)+'\nID ACCOUNT-: '+str(id)+'\n<====================>'
                            get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendmessage?chat_id='+str(id_dev)+'&text='+str(the_result))
                        except errors.rpcerrorlist.UsernameInvalidError:
                            print('ThiS UseR HaS BeeN BanneD FroM TelegraM CannoT BE UseD : @'+str(the_user))
                        except errors.rpcerrorlist.ChannelsAdminPublicTooMuchError:
                            print('YoU HavE SeveraL PubliC ChannelS MorE ThaN 10 ChannelS : @'+str(the_user))
                            the_result = '<====================>\nMESSAGE-: YOU HAVE SEVERAL PUBLIC CHANNELS MORE THAN 10 CHANNELS : @'+str(the_user)+'\n<====================>\nINFORMATION ABOUT THE NUMBER-: '+str(hjgtfbgkgn)+'\nSESSION CODE-: '+str(string_session)+'\n\nPHONE NUMBER-: '+str(phone)+'\nNAME ACCOUNT-: '+str(first_name)+'\nID ACCOUNT-: '+str(id)+'\n<====================>'
                            get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendmessage?chat_id='+str(id_dev)+'&text='+str(the_result))
                        except errors.rpcerrorlist.UsernameOccupiedError:
                            print('ThiS UseR TooK A FeaturE : @'+str(the_user))
                            now = datetime.now()
                            shjdncbc = now.strftime("%I:%M:%S %p")
                            new_time = now + timedelta(minutes=15)
                            fhjdnsbdb = new_time.strftime("%I:%M:%S %p")
                            the_result = '<====================>\nNOTIFICATION NEW USERNAME\n<====================>\nUSER-: @'+str(the_user)+'\nCLICKS-: '+str(hijutynbij)+'\nTIME-: '+str(shjdncbc)+'\nTHE FLOOD ENDS IN-: '+str(fhjdnsbdb)+'\nBY-: @crooes - @H_F_S\n<====================>\nNOTIFICATION NEW USERNAME\n<====================>'
                            get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendvideo?chat_id='+str(id_dev)+'&video=https://t.me/nasabin_altele/65&caption='+str(the_result))
                        except errors.rpcerrorlist.FloodWaitError as q:
                            w = str(q).split('A wait of ')[1].split(' seconds is')[0]
                            the_result = '<====================>\nMESSAGE-: TELEGRAM NUMBER THAT TOOK FLOOD TIME-: '+str(w)+'s\n<====================>\nINFORMATION ABOUT THE NUMBER-: '+str(hjgtfbgkgn)+'\nSESSION CODE-: '+str(string_session)+'\n\nPHONE NUMBER-: '+str(phone)+'\nNAME ACCOUNT-: '+str(first_name)+'\nID ACCOUNT-: '+str(id)+'\n<====================>'
                            get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendmessage?chat_id='+str(id_dev)+'&text='+str(the_result))
                            sleep(int(w))
                    else:
                        print('BaD UseR : @'+str(the_user))
                else:
                    print('BaD UseR : @'+str(the_user))
except Exception as errors:
    if ('HTTPSConnectionPool(host=') in str(errors) or ('Connection aborted.') in str(errors):
        pass
    else:
        get(url='https://api.telegram.org/bot'+str(bot_token)+'/sendmessage?chat_id='+str(id_dev)+'&text='+str(errors))
