#!/usr/local/bin/python
# -*- coding: utf-8 -*-




'''##########################################################################################################################################
Developed By HamidSJ From Iran,Ahvaz
For MTN-Irancell ceontent campaign of Content Providers
##########################################################################################################################################'''





import telebot
import sqlite3 as sql
from telebot import types as tp

#bot = telebot.TeleBot("416140031:AAHObPMLhyAJsFAblRwz_jcyoItGU6boiPI") # characterTestbot
bot = telebot.TeleBot("416416566:AAHE-0gZZlYV4q-00m-ZKvgsypum-cO7AHw")  # YourTypeBot
con = sql.connect('charBot.db')
startMessage = "تبریک ! شما عضو ربات خودشناسی شدید. با این ربات میتونید از خودتون تست بگیرید و بیشتر باهاش (خودتون) آشنا بشید 😃\nحالا برای ادامه لازمه که روی ثبت نام کلیک کنی".decode("utf-8")
startAgainMessage = "تبریک ! شما عضو ربات خودشناسی شدید. با این ربات میتونید از خودتون تست بگیرید و بیشتر باهاش (خودتون) آشنا بشید 😃".decode("utf-8")
signUpMessage = "خب همه چی تقریبا حله ! 😁\n برو تست رو شروع کن. منتظر چی هستی؟".decode("utf-8")
testsList = ["📌✅ تست MBTI ✏️".decode("utf-8"),"✅ تست هوش تصویری 🎆️".decode("utf-8"),"✅ تست شخصیت پنهان ✏️".decode("utf-8"),"✅ تست شخصیت رفتاری ✏️".decode("utf-8"),"✅ چقدر سالمین ؟ ✏️".decode("utf-8"),"✅ غمگین یا افسرده ؟ ✏️".decode("utf-8"),"✅ تست رضایت شغلی ✏️".decode("utf-8"),"✅ تست ازدواج ✏️".decode("utf-8"),"✅ تست زیبایی ✏️".decode("utf-8")]
testButton1 = tp.KeyboardButton(text=testsList[0])
testButton2 = tp.KeyboardButton(text=testsList[1])
testButton3 = tp.KeyboardButton(text=testsList[2])
testButton4 = tp.KeyboardButton(text=testsList[3])
testButton5 = tp.KeyboardButton(text=testsList[4])
testButton6 = tp.KeyboardButton(text=testsList[5])
testButton7 = tp.KeyboardButton(text=testsList[6])
testButton8 = tp.KeyboardButton(text=testsList[7])
testButton9 = tp.KeyboardButton(text=testsList[8])
MainMenuButtun = "❌ بازگشت به منوی اصلی".decode("utf-8")
##############################################################################################################################
def soalNumber(number):
    listemun = ["0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣"]
    if number>=0 and number<10:
        return listemun[number].decode("utf-8")+"  "
    elif number>=10 and number<100 :
        return listemun[(number%10)].decode("utf-8")+listemun[(number/10)].decode("utf-8")+"  "
    elif number>=100 and number<1000:
        return  listemun[((number%100)%10)].decode("utf-8") + listemun[((number/10)%10)].decode("utf-8") +listemun[(number / 100)].decode("utf-8") + "  "
    else:
        return ""
##############################################################################################################################
@bot.message_handler(commands=["start"])
def startCommandFunction(message):
    if str(message.chat.type)=="private":
        con = sql.connect('charBot.db')
        kb = tp.ReplyKeyboardMarkup(row_width=1)
        kba = tp.ReplyKeyboardMarkup()
        checkSignSql = "SELECT * FROM Users WHERE user_id=%s" % message.chat.id
        cu = con.execute(checkSignSql)
        res = cu.fetchall()
        #print res
        if res.__len__()==0:
            kb_b = tp.KeyboardButton(text="ثبت نام".decode("utf-8"),request_contact=True)
            kb.add(kb_b)
            bot.send_message(chat_id=message.chat.id,text=startMessage,reply_markup=kb)
        else:
            kba.row(testButton1)
            kba.row(testButton2)
            kba.row(testButton3)
            kba.row(testButton4)
            kba.row(testButton5)
            kba.row(testButton6)
            kba.row(testButton7)
            kba.row(testButton8)
            kba.row(testButton9)
            bot.send_message(chat_id=message.chat.id,text=startAgainMessage,reply_markup=kba)
##############################################################################################################################
@bot.message_handler(content_types=['contact'])
def signUp(message):
    if str(message.chat.type) == "private":
        con = sql.connect('charBot.db')
        KBtests = tp.ReplyKeyboardMarkup()
        KBtests.row(testButton1)
        KBtests.row(testButton2)
        KBtests.row(testButton3)
        KBtests.row(testButton4)
        KBtests.row(testButton5)
        KBtests.row(testButton6)
        KBtests.row(testButton7)
        KBtests.row(testButton8)
        KBtests.row(testButton9)
        phoneNumber = message.contact.phone_number
        insertNumberSql = "INSERT INTO Users(user_id,number,activeTest,activeQuestion,pointActiveTest) VALUES ('%s','%s','0','0','12345')" % (str(message.chat.id), str(phoneNumber))
        checkSignNumberSql = "SELECT * FROM Users WHERE number=%s" % str(phoneNumber)
        cuCheck = con.execute(checkSignNumberSql)
        if cuCheck.fetchall().__len__()==0:
            con.execute(insertNumberSql)
            con.commit()
        bot.send_message(chat_id=message.chat.id,text=signUpMessage,
                         reply_to_message_id=message.message_id,reply_markup=KBtests)
##############################################################################################################################
@bot.message_handler(func= lambda mes:str(mes.text.encode("utf-8")).decode("utf-8")==testsList[2])
def startTest1(message):
    con = sql.connect('charBot.db')
    checkTestActivationSql = "SELECT * FROM Users WHERE user_id=%s AND NOT activeTest=0" % str(message.chat.id)
    setActiveTestSql = "UPDATE Users SET activeTest='%s' WHERE user_id='%s'" % ("STest1", str(message.chat.id))
    setActiveQuestionSql = "UPDATE Users SET activeQuestion='%s' WHERE user_id='%s'" % ("1", str(message.chat.id))
    selectFirstQuestionSql = "SELECT * FROM STest1 WHERE ID=1"
    res = con.execute(checkTestActivationSql).fetchall()
    if res.__len__() != 0:
        bot.send_message(chat_id=message.chat.id,
                         text="اول این آزمون رو تموم کن بعد برو سراغ یکی دیگ داداچ D:".decode("utf-8"),
                         reply_to_message_id=message.message_id)
    else:
        kb = tp.ReplyKeyboardMarkup(row_width=1)
        con.execute(setActiveTestSql)
        con.execute(setActiveQuestionSql)
        con.commit()
        res = con.execute(selectFirstQuestionSql).fetchone()
        kb_b = tp.KeyboardButton(text=MainMenuButtun)
        kb.row(kb_b)
        for i in range(2, 9):
            if str(res[i].encode("utf-8")).decode("utf-8") != "0":
                kb_b = tp.KeyboardButton(text=str(res[i].encode("utf-8")).decode("utf-8"))
                kb.row(kb_b)
        bot.send_message(chat_id=message.chat.id, text=soalNumber(1)+str(res[1].encode("utf-8")).decode("utf-8"), reply_markup=kb)
##############################################################################################################################
@bot.message_handler(func= lambda mes:str(mes.text.encode("utf-8")).decode("utf-8")==testsList[3])
def startTest2(message):
    if str(message.chat.type) == "private":
        con = sql.connect('charBot.db')
        checkTestActivationSql = "SELECT * FROM Users WHERE user_id=%s AND NOT activeTest=0" % str(message.chat.id)
        setActiveTestSql = "UPDATE Users SET activeTest='%s' WHERE user_id='%s'" % ("STest2", str(message.chat.id))
        setActiveQuestionSql = "UPDATE Users SET activeQuestion='%s' WHERE user_id='%s'" % ("1", str(message.chat.id))
        selectFirstQuestionSql = "SELECT * FROM STest2 WHERE ID=1"
        res = con.execute(checkTestActivationSql).fetchall()
        #print res
        if res.__len__() != 0:
            bot.send_message(chat_id=message.chat.id,
                             text="اول این آزمون رو تموم کن بعد برو سراغ یکی دیگ داداچ D:".decode("utf-8"),
                             reply_to_message_id=message.message_id)
        else:
            kb = tp.ReplyKeyboardMarkup(row_width=1)
            con.execute(setActiveTestSql)
            con.execute(setActiveQuestionSql)
            con.commit()
            res = con.execute(selectFirstQuestionSql).fetchone()
            kb_b = tp.KeyboardButton(text=MainMenuButtun)
            kb.row(kb_b)
            for i in range(2, 9):
                if str(res[i].encode("utf-8")).decode("utf-8") != "0":
                    kb_b = tp.KeyboardButton(text=str(res[i].encode("utf-8")).decode("utf-8"))
                    kb.row(kb_b)
            bot.send_message(chat_id=message.chat.id, text=str(res[1].encode("utf-8")).decode("utf-8"), reply_markup=kb)
##############################################################################################################################
@bot.message_handler(func= lambda mes:str(mes.text.encode("utf-8")).decode("utf-8")==testsList[4])
def startTest3(message):
    if str(message.chat.type) == "private":
        con = sql.connect('charBot.db')
        checkTestActivationSql = "SELECT * FROM Users WHERE user_id=%s AND NOT activeTest=0" % str(message.chat.id)
        setActiveTestSql = "UPDATE Users SET activeTest='%s' WHERE user_id='%s'" % ("STest3", str(message.chat.id))
        setActiveQuestionSql = "UPDATE Users SET activeQuestion='%s' WHERE user_id='%s'" % ("1", str(message.chat.id))
        selectFirstQuestionSql = "SELECT * FROM STest3 WHERE ID=1"
        res = con.execute(checkTestActivationSql).fetchall()
        if res.__len__() != 0:
            bot.send_message(chat_id=message.chat.id,
                             text="اول این آزمون رو تموم کن بعد برو سراغ یکی دیگ داداچ D:".decode("utf-8"),
                             reply_to_message_id=message.message_id)
        else:
            kb = tp.ReplyKeyboardMarkup(row_width=1)
            con.execute(setActiveTestSql)
            con.execute(setActiveQuestionSql)
            con.commit()
            res = con.execute(selectFirstQuestionSql).fetchone()
            kb_b = tp.KeyboardButton(text=MainMenuButtun)
            kb.row(kb_b)
            for i in range(2, 9):
                if str(res[i].encode("utf-8")).decode("utf-8") != "0":
                    kb_b = tp.KeyboardButton(text=str(res[i].encode("utf-8")).decode("utf-8"))
                    kb.row(kb_b)
            bot.send_message(chat_id=message.chat.id, text=soalNumber(1)+str(res[1].encode("utf-8")).decode("utf-8"), reply_markup=kb)
##############################################################################################################################
@bot.message_handler(func= lambda mes:str(mes.text.encode("utf-8")).decode("utf-8")==testsList[5])
def startTest4(message):
    if str(message.chat.type) == "private":
        con = sql.connect('charBot.db')
        checkTestActivationSql = "SELECT * FROM Users WHERE user_id=%s AND NOT activeTest=0" % str(message.chat.id)
        setActiveTestSql = "UPDATE Users SET activeTest='%s' WHERE user_id='%s'" % ("STest4", str(message.chat.id))
        setActiveQuestionSql = "UPDATE Users SET activeQuestion='%s' WHERE user_id='%s'" % ("1", str(message.chat.id))
        selectFirstQuestionSql = "SELECT * FROM STest4 WHERE ID=1"
        res = con.execute(checkTestActivationSql).fetchall()
        if res.__len__() != 0:
            bot.send_message(chat_id=message.chat.id,
                             text="اول این آزمون رو تموم کن بعد برو سراغ یکی دیگ داداچ D:".decode("utf-8"),
                             reply_to_message_id=message.message_id)
        else:
            kb = tp.ReplyKeyboardMarkup(row_width=1)
            con.execute(setActiveTestSql)
            con.execute(setActiveQuestionSql)
            con.commit()
            res = con.execute(selectFirstQuestionSql).fetchone()
            kb_b = tp.KeyboardButton(text=MainMenuButtun)
            kb.row(kb_b)
            for i in range(2, 9):
                if str(res[i].encode("utf-8")).decode("utf-8") != "0":
                    kb_b = tp.KeyboardButton(text=str(res[i].encode("utf-8")).decode("utf-8"))
                    kb.row(kb_b)
            bot.send_message(chat_id=message.chat.id, text=soalNumber(1)+str(res[1].encode("utf-8")).decode("utf-8"), reply_markup=kb)
##############################################################################################################################
@bot.message_handler(func= lambda mes:str(mes.text.encode("utf-8")).decode("utf-8")==testsList[6])
def startTest5(message):
    if str(message.chat.type) == "private":
        con = sql.connect('charBot.db')
        checkTestActivationSql = "SELECT * FROM Users WHERE user_id=%s AND NOT activeTest=0" % str(message.chat.id)
        setActiveTestSql = "UPDATE Users SET activeTest='%s' WHERE user_id='%s'" % ("STest5", str(message.chat.id))
        setActiveQuestionSql = "UPDATE Users SET activeQuestion='%s' WHERE user_id='%s'" % ("1", str(message.chat.id))
        selectFirstQuestionSql = "SELECT * FROM STest5 WHERE ID=1"
        res = con.execute(checkTestActivationSql).fetchall()
        if res.__len__() != 0:
            bot.send_message(chat_id=message.chat.id,
                             text="اول این آزمون رو تموم کن بعد برو سراغ یکی دیگ داداچ D:".decode("utf-8"),
                             reply_to_message_id=message.message_id)
        else:
            kb = tp.ReplyKeyboardMarkup(row_width=1)
            con.execute(setActiveTestSql)
            con.execute(setActiveQuestionSql)
            con.commit()
            res = con.execute(selectFirstQuestionSql).fetchone()
            kb_b = tp.KeyboardButton(text=MainMenuButtun)
            kb.row(kb_b)
            for i in range(2, 9):
                if str(res[i].encode("utf-8")).decode("utf-8") != "0":
                    kb_b = tp.KeyboardButton(text=str(res[i].encode("utf-8")).decode("utf-8"))
                    kb.row(kb_b)
            bot.send_message(chat_id=message.chat.id, text=soalNumber(1)+str(res[1].encode("utf-8")).decode("utf-8"), reply_markup=kb)
##############################################################################################################################
@bot.message_handler(func= lambda mes:str(mes.text.encode("utf-8")).decode("utf-8")==testsList[7])
def startTest6(message):
    if str(message.chat.type) == "private":
        con = sql.connect('charBot.db')
        checkTestActivationSql = "SELECT * FROM Users WHERE user_id=%s AND NOT activeTest=0" % str(message.chat.id)
        setActiveTestSql = "UPDATE Users SET activeTest='%s' WHERE user_id='%s'" % ("STest6", str(message.chat.id))
        setActiveQuestionSql = "UPDATE Users SET activeQuestion='%s' WHERE user_id='%s'" % ("1", str(message.chat.id))
        selectFirstQuestionSql = "SELECT * FROM STest6 WHERE ID=1"
        res = con.execute(checkTestActivationSql).fetchall()
        if res.__len__() != 0:
            bot.send_message(chat_id=message.chat.id,
                             text="اول این آزمون رو تموم کن بعد برو سراغ یکی دیگ داداچ D:".decode("utf-8"),
                             reply_to_message_id=message.message_id)
        else:
            kb = tp.ReplyKeyboardMarkup(row_width=1)
            con.execute(setActiveTestSql)
            con.execute(setActiveQuestionSql)
            con.commit()
            res = con.execute(selectFirstQuestionSql).fetchone()
            kb_b = tp.KeyboardButton(text=MainMenuButtun)
            kb.row(kb_b)
            for i in range(2, 9):
                #print str(res[i].encode("utf-8")).decode("utf-8")
                if str(res[i].encode("utf-8")).decode("utf-8") != "0":
                    kb_b = tp.KeyboardButton(text=str(res[i].encode("utf-8")).decode("utf-8"))
                    kb.row(kb_b)
            bot.send_message(chat_id=message.chat.id, text=soalNumber(1)+str(res[1].encode("utf-8")).decode("utf-8"), reply_markup=kb)
##############################################################################################################################
@bot.message_handler(func= lambda mes:str(mes.text.encode("utf-8")).decode("utf-8")==testsList[8])
def startTest7(message):
    if str(message.chat.type) == "private":
        con = sql.connect('charBot.db')
        checkTestActivationSql = "SELECT * FROM Users WHERE user_id=%s AND NOT activeTest=0" % str(message.chat.id)
        setActiveTestSql = "UPDATE Users SET activeTest='%s' WHERE user_id='%s'" % ("STest7", str(message.chat.id))
        setActiveQuestionSql = "UPDATE Users SET activeQuestion='%s' WHERE user_id='%s'" % ("1", str(message.chat.id))
        selectFirstQuestionSql = "SELECT * FROM STest7 WHERE ID=1"
        res = con.execute(checkTestActivationSql).fetchall()
        if res.__len__() != 0:
            bot.send_message(chat_id=message.chat.id,
                             text="اول این آزمون رو تموم کن بعد برو سراغ یکی دیگ داداچ D:".decode("utf-8"),
                             reply_to_message_id=message.message_id)
        else:
            kb = tp.ReplyKeyboardMarkup(row_width=1)
            con.execute(setActiveTestSql)
            con.execute(setActiveQuestionSql)
            con.commit()
            res = con.execute(selectFirstQuestionSql).fetchone()
            kb_b = tp.KeyboardButton(text=MainMenuButtun)
            kb.row(kb_b)
            for i in range(2, 9):
                #print str(res[i].encode("utf-8")).decode("utf-8")
                if str(res[i].encode("utf-8")).decode("utf-8") != "0":
                    kb_b = tp.KeyboardButton(text=str(res[i].encode("utf-8")).decode("utf-8"))
                    kb.row(kb_b)
            bot.send_message(chat_id=message.chat.id, text=soalNumber(1)+str(res[1].encode("utf-8")).decode("utf-8"), reply_markup=kb)
##############################################################################################################################
@bot.message_handler(func=lambda msg:str(msg.text.encode("utf-8")).decode("utf-8")==testsList[0])
def strtMBTI(message):
    if str(message.chat.type) == "private":
        con = sql.connect('charBot.db')
        checkTestActivationSql = "SELECT * FROM Users WHERE user_id=%s AND NOT activeTest=0" % str(message.chat.id)
        setActiveTestSql = "UPDATE Users SET activeTest='%s' WHERE user_id='%s'" % ("SMBTI", str(message.chat.id))
        setActiveQuestionSql = "UPDATE Users SET activeQuestion='%s' WHERE user_id='%s'" % ("1", str(message.chat.id))
        selectFirstQuestionSql = "SELECT * FROM SMBTI WHERE ID=1"
        res = con.execute(checkTestActivationSql).fetchall()
        if res.__len__() != 0:
            bot.send_message(chat_id=message.chat.id,
                             text="اول این آزمون رو تموم کن بعد برو سراغ یکی دیگ داداچ D:".decode("utf-8"),
                             reply_to_message_id=message.message_id)
        else:
            kb = tp.ReplyKeyboardMarkup(row_width=1)
            con.execute(setActiveTestSql)
            con.execute(setActiveQuestionSql)
            con.commit()
            res = con.execute(selectFirstQuestionSql).fetchone()
            #print res
            kb_b = tp.KeyboardButton(text=MainMenuButtun)
            kb.row(kb_b)
            for i in range(2,4):
                kb_b = tp.KeyboardButton(text=str(res[i].encode("utf-8")).decode("utf-8"))
                kb.row(kb_b)
            bot.send_message(chat_id=message.chat.id, text=soalNumber(1)+str(res[1].encode("utf-8")).decode("utf-8"),reply_markup=kb)
##############################################################################################################################
@bot.message_handler(func=lambda msg:str(msg.text.encode("utf-8")).decode("utf-8")==testsList[1])
def strtStasvir(message):
    kbsign = tp.ReplyKeyboardMarkup(row_width=1)
    if str(message.chat.type) == "private":
        con = sql.connect('charBot.db')
        setActiveTestSql = "UPDATE Users SET activeTest='%s' WHERE user_id='%s'" % ("SAX", str(message.chat.id))
        setActiveQuestionSql = "UPDATE Users SET activeQuestion='%s' WHERE user_id='%s'" % ("0", str(message.chat.id))
        checkUserSignSql = "SELECT * FROM Users WHERE user_id='%s'" % str(message.chat.id)
        con.execute(setActiveTestSql)
        con.execute(setActiveQuestionSql)
        con.commit()
        if con.execute(checkUserSignSql).fetchall().__len__() != 0:
            kbLevels = tp.ReplyKeyboardMarkup(row_width=1)
            selectAllOfLevelsSql = "SELECT * FROM SAX"
            AllOfLevels = con.execute(selectAllOfLevelsSql).fetchall()
            kbLevels_b = tp.KeyboardButton(text="➡️ بازگشت".decode("utf-8"))
            kbLevels.row(kbLevels_b)
            for row in AllOfLevels:
                level = str(row[0]).decode("utf-8")
                txt = "مرحله ".decode("utf-8")
                buttunText = txt+" "+level
                kbLevels_b = tp.KeyboardButton(text=buttunText)
                kbLevels.row(kbLevels_b)
            ##print int(str(kbLevels_b.text.encode("utf-8")).decode("utf-8").split("مرحله ".decode("utf-8"))[1])
            bot.send_message(chat_id=message.chat.id,text="مرحله ی مورد نظر را انتخاب کنید :".decode("utf-8"), reply_markup=kbLevels)
        else:
            kb_bsign = tp.KeyboardButton(text="ثبت نام".decode("utf-8"), request_contact=True)
            kbsign.add(kb_bsign)
            bot.send_message(chat_id=message.chat.id, text="لطفا ابتدا ثبت نام کنید سپس تست را شروع کنید 😊".decode("utf-8"), reply_markup=kbsign)
##############################################################################################################################
@bot.message_handler(func=lambda msg:True)
def Answers(message):
    #print str(message.text.encode("utf-8")).decode("utf-8")
    if str(message.chat.type) == "private":
        kbsign = tp.ReplyKeyboardMarkup(row_width=1)
        kb = tp.ReplyKeyboardMarkup(row_width=1)
        con = sql.connect('charBot.db')
        checkAnswer = False
        checkUserSignSql = "SELECT * FROM Users WHERE user_id='%s'"% str(message.chat.id)
        if con.execute(checkUserSignSql).fetchall().__len__() !=0:
            getActiveTestNameSql = "SELECT activeTest FROM Users WHERE user_id='%s'" % str(message.chat.id)
            activeTest = con.execute(getActiveTestNameSql).fetchone()[0]
            getActiveQuestionNumberSql = "SELECT activeQuestion FROM Users WHERE user_id='%s'" % str(message.chat.id)
            activeQuestion = con.execute(getActiveQuestionNumberSql).fetchone()[0]
            #print str(activeQuestion)
            if str(message.text.encode("utf-8")).decode("utf-8") != MainMenuButtun:
                if str(activeTest) == "STest1" or str(activeTest) == "STest2" or str(activeTest) == "STest3" or str(activeTest) == "STest4" or str(activeTest) == "STest5" or str(activeTest) == "STest6" or str(activeTest) == "STest7" :
                    getNowPointActiveTestSql = "SELECT pointActiveTest FROM Users WHERE user_id='%s'"% str(message.chat.id)
                    NowPointActiveTest = con.execute(getNowPointActiveTestSql).fetchone()[0]

                    if str(message.text.encode("utf-8")).decode("utf-8")!="➡️ برگشت به سوال قبل".decode("utf-8"):
                        checkAnswerSql = "SELECT * FROM %s WHERE ID=%d"% (str(activeTest),int(activeQuestion))
                        setActiveQuestionAgainSql = "UPDATE Users SET activeQuestion='%d' WHERE user_id='%s'" % (int(activeQuestion)+1,str(message.chat.id))
                        #print checkAnswerSql
                        Answers = con.execute(checkAnswerSql).fetchone()
                        now = 0
                        for i in range(2,9):
                            #print str(Answers[i].encode("utf-8")).decode("utf-8")
                            if str(Answers[i].encode("utf-8")).decode("utf-8")==str(message.text.encode("utf-8")).decode("utf-8"):
                                checkAnswer = True
                                now = i-1
                                break
                        if activeTest=="STest1":
                            getThisQuestionPointSql = "SELECT * FROM ETest1 WHERE ID='%d'"% int(activeQuestion)
                        elif activeTest=="STest2":
                            getThisQuestionPointSql = "SELECT * FROM ETest2 WHERE ID='%d'" % int(activeQuestion)
                        elif activeTest == "STest3":
                            getThisQuestionPointSql = "SELECT * FROM ETest3 WHERE ID='%d'" % int(activeQuestion)
                        elif activeTest == "STest4":
                            getThisQuestionPointSql = "SELECT * FROM ETest4 WHERE ID='%d'" % int(activeQuestion)
                        elif activeTest == "STest5":
                            getThisQuestionPointSql = "SELECT * FROM ETest5 WHERE ID='%d'" % int(activeQuestion)
                        elif activeTest == "STest6":
                            getThisQuestionPointSql = "SELECT * FROM ETest6 WHERE ID='%d'" % int(activeQuestion)
                        else:  # activeTest == "STest7":
                            getThisQuestionPointSql = "SELECT * FROM ETest7 WHERE ID='%d'" % int(activeQuestion)
                        thisQuestionPointSql = con.execute(getThisQuestionPointSql).fetchone()[now]
                        if checkAnswer:
                            if str(NowPointActiveTest) != "12345":
                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (str(str(NowPointActiveTest)+","+str(thisQuestionPointSql)),str(message.chat.id))
                                #print setNowPointActiveTestSql
                            else:
                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (str(thisQuestionPointSql),str(message.chat.id))
                            #print setNowPointActiveTestSql
                            con.execute(setNowPointActiveTestSql)
                            con.commit()
                            checkNextQuestionExistSql = "SELECT * FROM %s WHERE ID=%s" % (str(activeTest),str(int(str(activeQuestion))+1))
                            NextQuestionExist = con.execute(checkNextQuestionExistSql).fetchone()
                            if NextQuestionExist !=None:
                                kb_b = tp.KeyboardButton(text=MainMenuButtun)
                                kb.row(kb_b)
                                for i in range(2, 9):
                                    if str(NextQuestionExist[i].encode("utf-8")).decode("utf-8") != "0":
                                        kb_b = tp.KeyboardButton(text=str(NextQuestionExist[i].encode("utf-8")).decode("utf-8"))
                                        kb.row(kb_b)
                                kb_b = tp.KeyboardButton(text="➡️ برگشت به سوال قبل".decode("utf-8"))
                                kb.row(kb_b)
                                con.execute(setActiveQuestionAgainSql)
                                con.commit()
                                bot.send_message(chat_id=message.chat.id, text=soalNumber(int(str(activeQuestion))+1)+str(NextQuestionExist[1].encode("utf-8")).decode("utf-8"), reply_markup=kb)
                            else:
                                getPointsSql = "SELECT pointActiveTest FROM Users WHERE user_id='%s'" % str(message.chat.id)
                                points = str(con.execute(getPointsSql).fetchone()[0])
                                arrayPoints = points.split(",")
                                sum=0
                                for point in arrayPoints:
                                    sum+=int(point)
                                KBtests = tp.ReplyKeyboardMarkup()
                                KBtests.row(testButton1)
                                KBtests.row(testButton2)
                                KBtests.row(testButton3)
                                KBtests.row(testButton4)
                                KBtests.row(testButton5)
                                KBtests.row(testButton6)
                                KBtests.row(testButton7)
                                KBtests.row(testButton8)
                                KBtests.row(testButton9)
                                if str(activeTest)=="STest1":
                                    natayej = con.execute("SELECT * FROM NTest1").fetchall()
                                elif str(activeTest)=="STest2":
                                    natayej = con.execute("SELECT * FROM NTest2").fetchall()
                                elif str(activeTest)=="STest3":
                                    natayej = con.execute("SELECT * FROM NTest3").fetchall()
                                elif str(activeTest)=="STest4":
                                    natayej = con.execute("SELECT * FROM NTest4").fetchall()
                                elif str(activeTest)=="STest5":
                                    natayej = con.execute("SELECT * FROM NTest5").fetchall()
                                elif str(activeTest)=="STest6":
                                    natayej = con.execute("SELECT * FROM NTest6").fetchall()
                                else:  # str(activeTest)=="STest7":
                                    natayej = con.execute("SELECT * FROM NTest7").fetchall()
                                natijeh = ""
                                for row in natayej:
                                    if sum >= int(str(row[1])) and sum <=int(str(row[2])):
                                        natijeh = str(row[3].encode("utf-8")).decode("utf-8")
                                bot.send_message(chat_id=message.chat.id,text="نتیجه آزمون شما 😉👇🏻👇🏻👇🏻👇🏻👇🏻".decode("utf-8"))
                                bot.send_message(chat_id=message.chat.id,text= natijeh)
                                bot.send_message(chat_id=message.chat.id, text=str("اگه دلتون خواست میتونید یه آزمون دیگه رو شروع کنید 😉").decode("utf-8"),reply_markup=KBtests)
                                con.execute("UPDATE Users SET activeTest='0' WHERE user_id='%s'" % str(message.chat.id))
                                con.execute("UPDATE Users SET activeQuestion='0' WHERE user_id='%s'" % str(message.chat.id))
                                con.execute("UPDATE Users SET pointActiveTest='12345' WHERE user_id='%s'" % str(message.chat.id))
                                con.commit()
                    else:
                        if int(activeQuestion) != 1:
                            setActiveQuestionAgainSql = "UPDATE Users SET activeQuestion='%d' WHERE user_id='%s'" % (int(activeQuestion) - 1, str(message.chat.id))
                            con.execute(setActiveQuestionAgainSql)
                            con.commit()
                            goToNextQuestionSql = "SELECT * FROM %s WHERE ID=%d" % (str(activeTest),int(int(activeQuestion) - 1))
                            res = con.execute(goToNextQuestionSql).fetchone()
                            kb_b = tp.KeyboardButton(text=MainMenuButtun)
                            kb.row(kb_b)
                            for n in range(2, 9):
                                if str(res[n].encode("utf-8")).decode("utf-8") != "0":
                                    kb_b = tp.KeyboardButton(text=str(res[n].encode("utf-8")).decode("utf-8"))
                                    kb.row(kb_b)
                            if int(activeQuestion) - 1 != 1:
                                kb_b = tp.KeyboardButton(text="➡️ برگشت به سوال قبل".decode("utf-8"))
                                kb.row(kb_b)
                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (str(NowPointActiveTest)[:str(NowPointActiveTest).__len__() - 2], str(message.chat.id))
                            else:
                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % ("12345", str(message.chat.id))
                            bot.send_message(chat_id=message.chat.id, text=soalNumber(int(str(activeQuestion))-1)+str(res[1].encode("utf-8")).decode("utf-8"),
                                             reply_markup=kb)
                            con.execute(setActiveQuestionAgainSql)
                            con.execute(setNowPointActiveTestSql)
                            #print setNowPointActiveTestSql
                            con.commit()
                elif str(activeTest) == "SMBTI":
                    getActiveQuestionNumberSql = "SELECT activeQuestion FROM Users WHERE user_id='%s'" % str(message.chat.id)
                    activeQuestion = con.execute(getActiveQuestionNumberSql).fetchone()[0]
                    getNowPointActiveTestSql = "SELECT pointActiveTest FROM Users WHERE user_id='%s'" % str(message.chat.id)
                    NowPointActiveTest = con.execute(getNowPointActiveTestSql).fetchone()[0]
                    if str(message.text.encode("utf-8")).decode("utf-8")!="➡️ برگشت به سوال قبل".decode("utf-8"):
                        checkAnswerSql = "SELECT * FROM %s WHERE ID=%d" % (str(activeTest), int(activeQuestion))
                        setActiveQuestionAgainSql = "UPDATE Users SET activeQuestion='%d' WHERE user_id='%s'" % (int(activeQuestion) + 1, str(message.chat.id))
                        #print checkAnswerSql
                        Answers = con.execute(checkAnswerSql).fetchone()
                        now = 0
                        if str(Answers[2].encode("utf-8")).decode("utf-8") == str(message.text.encode("utf-8")).decode("utf-8"):
                            checkAnswer = True
                            now = 1
                        elif str(Answers[3].encode("utf-8")).decode("utf-8") == str(message.text.encode("utf-8")).decode(
                                "utf-8"):
                            checkAnswer = True
                            now = 2
                        if checkAnswer:
                            if int(activeQuestion) != 87:
                                getScoreSql = "SELECT * FROM EMBTI WHERE soal=%d" % int(activeQuestion)
                                Scores = con.execute(getScoreSql).fetchall()
                                if now == 1:
                                    for row in Scores:
                                        if row[3] > 0:
                                            tipCode = str(row[2])[0]
                                            if NowPointActiveTest != "12345":
                                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (
                                                str(str(NowPointActiveTest) + "," + tipCode + str(row[3])),
                                                str(message.chat.id))
                                                con.execute(setNowPointActiveTestSql)
                                                con.commit()
                                                break
                                            else:
                                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (
                                                str(tipCode + str(row[3])), str(message.chat.id))
                                                con.execute(setNowPointActiveTestSql)
                                                con.commit()
                                                break
                                elif now == 2:
                                    for row in Scores:
                                        if row[4] > 0:
                                            tipCode = str(row[2])[0]
                                            if NowPointActiveTest != "12345":
                                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (
                                                    str(str(NowPointActiveTest) + "," + tipCode + str(row[3])),
                                                    str(message.chat.id))
                                                con.execute(setNowPointActiveTestSql)
                                                con.commit()
                                                break
                                            else:
                                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (
                                                str(tipCode + str(row[3])), str(message.chat.id))
                                                con.execute(setNowPointActiveTestSql)
                                                con.commit()
                                                break
                                goToNextQuestionSql = "SELECT * FROM SMBTI WHERE ID=%d" % int(int(activeQuestion) + 1)
                                #print goToNextQuestionSql
                                res = con.execute(goToNextQuestionSql).fetchone()
                                kb_b = tp.KeyboardButton(text=MainMenuButtun)
                                kb.row(kb_b)
                                for n in range(2, 4):
                                    kb_b = tp.KeyboardButton(text=str(res[n].encode("utf-8")).decode("utf-8"))
                                    kb.row(kb_b)
                                kb_b = tp.KeyboardButton(text="➡️ برگشت به سوال قبل".decode("utf-8"))
                                kb.row(kb_b)
                                bot.send_message(chat_id=message.chat.id, text=soalNumber(int(str(activeQuestion))+1)+str(res[1].encode("utf-8")).decode("utf-8"),
                                                 reply_markup=kb)
                                con.execute(setActiveQuestionAgainSql)
                                con.commit()
                            elif int(activeQuestion) == 87:
                                getScoreSql = "SELECT * FROM EMBTI WHERE soal=%d" % int(activeQuestion)
                                Scores = con.execute(getScoreSql).fetchall()
                                if now == 1:
                                    for row in Scores:
                                        if row[3] > 0:
                                            tipCode = str(row[2])[0]
                                            if NowPointActiveTest != "12345":
                                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (str(str(NowPointActiveTest) + "," + tipCode + str(row[3])),str(message.chat.id))
                                                con.execute(setNowPointActiveTestSql)
                                                con.commit()
                                                break
                                            else:
                                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (
                                                    str(tipCode + str(row[3])), str(message.chat.id))
                                                con.execute(setNowPointActiveTestSql)
                                                con.commit()
                                                break
                                elif now == 2:
                                    for row in Scores:
                                        if row[4] > 0:
                                            tipCode = str(row[2])[0]
                                            if NowPointActiveTest != "12345":
                                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (
                                                    str(str(NowPointActiveTest) + "," + tipCode + str(row[3])),
                                                    str(message.chat.id))
                                                con.execute(setNowPointActiveTestSql)
                                                con.commit()
                                                break
                                            else:
                                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (
                                                    str(tipCode + str(row[3])), str(message.chat.id))
                                                con.execute(setNowPointActiveTestSql)
                                                con.commit()
                                                break
                                points = str(con.execute(
                                    "SELECT pointActiveTest FROM Users WHERE user_id='%s'" % str(message.chat.id)).fetchone()[
                                                 0])
                                arrayPoints = points.split(",")
                                sumE = 0
                                sumI = 0
                                sumS = 0
                                sumN = 0
                                sumT = 0
                                sumF = 0
                                sumJ = 0
                                sumP = 0
                                for point in arrayPoints:
                                    if point[0] == 'E':
                                        sumE += int(point[1])
                                    elif point[0] == 'I':
                                        sumI += int(point[1])
                                    elif point[0] == 'S':
                                        sumS += int(point[1])
                                    elif point[0] == 'N':
                                        sumN += int(point[1])
                                    elif point[0] == 'T':
                                        sumT += int(point[1])
                                    elif point[0] == 'F':
                                        sumF += int(point[1])
                                    elif point[0] == 'J':
                                        sumJ += int(point[1])
                                    elif point[0] == 'P':
                                        sumP += int(point[1])
                                tag = ""
                                if sumE > sumI:
                                    tag = tag + "E"
                                else:
                                    tag = tag + "I"
                                if sumS > sumN:
                                    tag = tag + "S"
                                else:
                                    tag = tag + "N"
                                if sumT > sumF:
                                    tag = tag + "T"
                                else:
                                    tag = tag + "F"
                                if sumJ > sumP:
                                    tag = tag + "J"
                                else:
                                    tag = tag + "P"
                                if tag=="ISTJ":
                                    idOfTipCode =1
                                elif tag=="ISFJ":
                                    idOfTipCode =2
                                elif tag == "ESTP":
                                    idOfTipCode = 3
                                elif tag == "ESFP":
                                    idOfTipCode = 4
                                elif tag == "INTJ":
                                    idOfTipCode = 5
                                elif tag == "INFJ":
                                    idOfTipCode = 6
                                elif tag == "ENTP":
                                    idOfTipCode = 7
                                elif tag == "ENFP":
                                    idOfTipCode = 8
                                elif tag == "ISTP":
                                    idOfTipCode = 9
                                elif tag == "INTP":
                                    idOfTipCode = 10
                                elif tag == "ESTJ":
                                    idOfTipCode = 11
                                elif tag == "ENTJ":
                                    idOfTipCode = 12
                                elif tag == "ISFP":
                                    idOfTipCode = 13
                                elif tag == "INFP":
                                    idOfTipCode = 14
                                elif tag == "ESFJ":
                                    idOfTipCode = 15
                                elif tag == "ENFJ":
                                    idOfTipCode = 16
                                natijehSql = "SELECT natijeh FROM NMBTI WHERE ID=%d" % int(idOfTipCode)
                                #print natijehSql
                                Natijeh = str(con.execute(natijehSql).fetchone()[0].encode("utf-8")).decode("utf-8")
                                bot.send_message(chat_id=message.chat.id,
                                                 text="نتیجه آزمون شما 😉👇🏻👇🏻👇🏻👇🏻👇🏻".decode("utf-8"))
                                bot.send_message(chat_id=message.chat.id, text=Natijeh)
                                Kbtests = tp.ReplyKeyboardMarkup(row_width=1)
                                Kbtests.row(testButton1)
                                Kbtests.row(testButton2)
                                Kbtests.row(testButton3)
                                Kbtests.row(testButton4)
                                Kbtests.row(testButton5)
                                Kbtests.row(testButton6)
                                Kbtests.row(testButton7)
                                Kbtests.row(testButton8)
                                Kbtests.row(testButton9)
                                bot.send_message(chat_id=message.chat.id,
                                                 text=str("اگه دلتون خواست میتونید یه آزمون دیگه رو شروع کنید 😉").decode(
                                                     "utf-8"), reply_markup=Kbtests)
                                con.execute("UPDATE Users SET activeTest='0' WHERE user_id='%s'" % str(message.chat.id))
                                con.execute("UPDATE Users SET activeQuestion='0' WHERE user_id='%s'" % str(message.chat.id))
                                con.execute(
                                    "UPDATE Users SET pointActiveTest='12345' WHERE user_id='%s'" % str(message.chat.id))
                                con.commit()
                            else:
                                pass
                    else:
                        if int(activeQuestion) != 1:
                            setActiveQuestionAgainSql = "UPDATE Users SET activeQuestion='%d' WHERE user_id='%s'" % (int(activeQuestion) - 1, str(message.chat.id))
                            con.execute(setActiveQuestionAgainSql)
                            con.commit()
                            goToNextQuestionSql = "SELECT * FROM SMBTI WHERE ID=%d" % int(int(activeQuestion) - 1)
                            res = con.execute(goToNextQuestionSql).fetchone()
                            kb_b = tp.KeyboardButton(text=MainMenuButtun)
                            kb.row(kb_b)
                            for n in range(2, 4):
                                kb_b = tp.KeyboardButton(text=str(res[n].encode("utf-8")).decode("utf-8"))
                                kb.row(kb_b)
                            if int(activeQuestion) - 1 != 1:
                                kb_b = tp.KeyboardButton(text="➡️ برگشت به سوال قبل".decode("utf-8"))
                                kb.row(kb_b)
                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (str(NowPointActiveTest)[:str(NowPointActiveTest).__len__() - 3], str(message.chat.id))
                            else:
                                setNowPointActiveTestSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % (
                                    "12345", str(message.chat.id))
                            bot.send_message(chat_id=message.chat.id, text=soalNumber(int(str(activeQuestion))-1)+str(res[1].encode("utf-8")).decode("utf-8"),
                                             reply_markup=kb)
                            con.execute(setActiveQuestionAgainSql)
                            con.execute(setNowPointActiveTestSql)
                            #print setNowPointActiveTestSql
                            con.commit()
                elif str(activeTest) == "SAX" and str(activeQuestion) == "0":
                    if str(message.text.encode("utf-8")).decode("utf-8")!="➡️ بازگشت".decode("utf-8"):
                        soal = int(str(message.text.encode("utf-8")).decode("utf-8").split("مرحله ".decode("utf-8"))[1])
                        selectRowOfLevelSql = "SELECT * FROM SAX WHERE ID=%d"% int(soal)
                        res = con.execute(selectRowOfLevelSql).fetchone()
                        path = str(res[1])
                        photoSoal = open(path,"rb")
                        kb_b = tp.KeyboardButton(text="➡️ بازگشت".decode("utf-8"))
                        kb.row(kb_b)
                        for n in range(2,5):
                            lent = str(res[n].encode("utf-8")).decode("utf-8").__len__()
                            kb_b = tp.KeyboardButton(text=str(res[n].encode("utf-8")).decode("utf-8")[:lent-1])
                            kb.row(kb_b)
                        bot.send_photo(chat_id=message.chat.id, photo=photoSoal,
                                       caption="پاسخ تصویر را از بین گزینه ها انتخاب کنید : ".decode("utf-8"),
                                       reply_to_message_id=message.message_id,
                                       reply_markup=kb)
                        setActiveTestAgainSql = "UPDATE Users SET activeQuestion='%s' WHERE user_id='%s'" % (str(soal), str(message.chat.id))
                        con.execute(setActiveTestAgainSql)
                        con.commit()
                    else:
                        setActiveTestAgainSql = "UPDATE Users SET activeTest='%s' WHERE user_id='%s'" % ("0", str(message.chat.id))
                        con.execute(setActiveTestAgainSql)
                        con.commit()
                        Kbtests = tp.ReplyKeyboardMarkup(row_width=1)
                        Kbtests.row(testButton1)
                        Kbtests.row(testButton2)
                        Kbtests.row(testButton3)
                        Kbtests.row(testButton4)
                        Kbtests.row(testButton5)
                        Kbtests.row(testButton6)
                        Kbtests.row(testButton7)
                        Kbtests.row(testButton8)
                        Kbtests.row(testButton9)
                        bot.send_message(chat_id=message.chat.id,text=str("اگه دلتون خواست میتونید یه آزمون دیگه رو شروع کنید 😉").decode("utf-8"), reply_markup=Kbtests)
                elif str(activeTest) == "SAX" and str(activeQuestion) != "0":
                    if str(message.text.encode("utf-8")).decode("utf-8") != "➡️ بازگشت".decode("utf-8"):
                        selectRowOfLevelSql = "SELECT * FROM SAX WHERE ID=%d" % int(activeQuestion)
                        res = con.execute(selectRowOfLevelSql).fetchone()
                        sahih = False
                        for n in range(2,5):
                            lent = str(res[n].encode("utf-8")).decode("utf-8").__len__()
                            if str(res[n].encode("utf-8")).decode("utf-8")[:lent-1] == str(message.text.encode("utf-8")).decode("utf-8"):
                                if str(res[n].encode("utf-8")).decode("utf-8")[lent-1:] == "T".decode("utf-8"):
                                    bot.send_message(chat_id=message.chat.id,text="تبریک میگم پاسخ شما درست بود 😃".decode("utf-8"),reply_to_message_id=message.message_id)
                                    sahih = True
                                    break
                        if not sahih:
                            bot.send_message(chat_id=message.chat.id,
                                             text="تبریک نمیگم پاسخ شما غلط بود 😂".decode("utf-8"),
                                             reply_to_message_id=message.message_id)
                    else:
                        setActiveTestAgainSql = "UPDATE Users SET activeQuestion='%s' WHERE user_id='%s'" % ("0", str(message.chat.id))
                        con.execute(setActiveTestAgainSql)
                        con.commit()
                        kbLevels = tp.ReplyKeyboardMarkup(row_width=1)
                        selectAllOfLevelsSql = "SELECT * FROM SAX"
                        AllOfLevels = con.execute(selectAllOfLevelsSql).fetchall()
                        kbLevels_b = tp.KeyboardButton(text="➡️ بازگشت".decode("utf-8"))
                        kbLevels.row(kbLevels_b)
                        for row in AllOfLevels:
                            level = str(row[0]).decode("utf-8")
                            txt = "مرحله ".decode("utf-8")
                            buttunText = txt + " " +level
                            kbLevels_b = tp.KeyboardButton(text=buttunText)
                            kbLevels.row(kbLevels_b)
                        bot.send_message(chat_id=message.chat.id, text="مرحله ی مورد نظر را انتخاب کنید :".decode("utf-8"),reply_markup=kbLevels)
            else:
                setActiveQuestionAgainSql = "UPDATE Users SET activeQuestion='%s' WHERE user_id='%s'" % ("0", str(message.chat.id))
                setActiveTestAgainSql = "UPDATE Users SET activeTest='%s' WHERE user_id='%s'" % ("0", str(message.chat.id))
                setPointActiveTestAgainSql = "UPDATE Users SET pointActiveTest='%s' WHERE user_id='%s'" % ("12345", str(message.chat.id))
                con.execute(setActiveTestAgainSql)
                con.execute(setActiveQuestionAgainSql)
                con.execute(setPointActiveTestAgainSql)
                con.commit()
                Kbtests = tp.ReplyKeyboardMarkup(row_width=1)
                Kbtests.row(testButton1)
                Kbtests.row(testButton2)
                Kbtests.row(testButton3)
                Kbtests.row(testButton4)
                Kbtests.row(testButton5)
                Kbtests.row(testButton6)
                Kbtests.row(testButton7)
                Kbtests.row(testButton8)
                Kbtests.row(testButton9)
                bot.send_message(chat_id=message.chat.id,
                                 text=str("اگه دلتون خواست میتونید یه آزمون دیگه رو شروع کنید 😉").decode("utf-8"),
                                 reply_markup=Kbtests)
        else:
            kb_bsign = tp.KeyboardButton(text="ثبت نام".decode("utf-8"), request_contact=True)
            kbsign.add(kb_bsign)
            bot.send_message(chat_id=message.chat.id, text="لطفا ابتدا ثبت نام کنید سپس تست را شروع کنید 😊".decode("utf-8"), reply_markup=kbsign)

##############################################################################################################################

bot.polling(none_stop=True)
