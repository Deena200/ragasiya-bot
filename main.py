import random
import os
from datetime import datetime, timedelta
from datetime import time
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    filters,
    ContextTypes,
    ChatMemberHandler
)

# =========================
# CONFIG
# =========================

TOKEN = "8798668728:AAEJj1Pdxw3ZZv78X-mwHDvFTb4Mz3PGO0M"
GROUP_ID = -1003573621688


# =========================
# 1. ADMIN TRIGGER
# =========================
admin_words = ["admin", "admins", "@admin", "@admins"]


admin_replies = [
    "Admin ah? 😏 konjam wait da",
    "Admins busy 😎 later varuvanga",
    "Owner kita pesitu varen 👀",
    "Summon pannita pola 😏",
    "Admin ah koopdura level ku vandhutiya 😎",
    "Admin ippo offline da 😴 wait pannunga",
    "Konjam porumai da… admin varuvaar 😏",
    "Admin ah disturb panra 😏 bold ah iruka",
    "Admin summon successful 😂 wait da",
    "Admin ku ping panni vechuten 👀",
    "Owner busy meeting la 😎 konjam late",
    "Admin ah thedura 😏 enna problem da",
    "Wait da… admin entry mass ah irukum 🔥",
    "Admin kita forward panniten 😎",
    "Admin ippo scene ku varala 😏",
    "Nee koopta admin odane varuva nu nenacha? 😂",
    "Admin ku notification poiduchu 👀",
    "Konjam neram da… admin loading ⏳",
    "Admin ah koopdura tone la iruku 😏",
    "Admin ippo silent mode la 😴",
    "Admin vandha dhaan scene start 🔥",
    "Relax da… admin paathutu reply pannuvaar 😎"
]



async def admin_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        print(update.effective_chat.id)  # ✅ correct place

        text = update.message.text.lower()
        if any(word in text for word in admin_words):
            await update.message.reply_text(random.choice(admin_replies))


# =========================
# 2. SCHEDULED MESSAGES
# =========================
morning_msgs = [
    "🌞 Good morning da makkal",
    "🌞 Good morning! Rise & grind 🔥",
    "🌞 Good morning! Innikum strong ah start pannunga 💪",
    "🌞 Good morning! Pudhu naal, pudhu chance da 😎",
    "🌞 Good morning! Morning vibes ah start pannunga ☀️",
    "🌞 Good morning! Innaiku namma day 🔥",
    "🌞 Good morning da legends 😏",
    "🌞 Good morning! Kalaila energy full ah irukanum 💥",
    "🌞 Good morning team 😎 let's dominate today",
    "🌞 Good morning! Thoongitu irukingala 😏 elundhuru da",
    "🌞 Good morning! Innikum success pakka namadhe 🔥",
    "🌞 Good morning! Start pannunga da... late panna koodathu ⏰",
    "🌞 Good morning! Coffee kudichacha? ☕ illa na ipo po 😏",
    "🌞 Good morning! New day new goals 💪 go smash it",
    "🌞 Good morning! Morning la irundhe focus 🔥",
    "🌞 Good morning! Nethu pochu... innaiku namma chance 😎",
    "🌞 Good morning! Elundhuru da... world wait panla 😏",
    "🌞 Good morning! Give up panna koodathu 💯",
    "🌞 Good morning! Sema naal da innaiku 🔥 feel it",
    "🌞 Good morning! Positive ah start pannunga ✨",
    "🌞 Good morning! Innikum namma level kaatanum 😎",
    "🌞 Good morning! Early start = strong finish 💪",
    "🌞 Good morning! Dream ah reality aakra naal da 🔥",
    "🌞 Good morning! Wake up & prove yourself 😏",
    "🌞 Good morning! Plan pannina naal smooth ah pogum 📈",
    "🌞 Good morning! Energy waste panna koodathu ⚡",
    "🌞 Good morning! Rise up da… success wait pannuthu 🔥"
]


afternoon_msgs = [
    "🌤️ Good afternoon da makkal",
    "🌤️ Good afternoon! Saptingala da? 🍛",
    "🌤️ Good afternoon! Lunch time 😋",
    "🌤️ Good afternoon! Energy refill pannunga 🔋",
    "🌤️ Good afternoon! Sapadu miss panna koodathu 😏",
    "🌤️ Good afternoon! Full ah sapdu da strength venum 💪",
    "🌤️ Good afternoon! Lunch mudichacha illa busy ah? 😎",
    "🌤️ Good afternoon! Sapadu + rest = power combo 🔥",
    "🌤️ Good afternoon! Over work pannadhe da, sapdu 😏",
    "🌤️ Good afternoon! Break eduthu refresh aagunga ☕",
    "🌤️ Good afternoon! Food sapta dhaan energy varum ⚡",
    "🌤️ Good afternoon! Half day mudinchu... innum balance 🔥",
    "🌤️ Good afternoon! Relax pannitu continue pannunga 😌",
    "🌤️ Good afternoon! Lunch apram sleep varutha 😴",
    "🌤️ Good afternoon! Sapadu strong ah irukanum da 😎",
    "🌤️ Good afternoon! Energy boost pannitu comeback 🔥",
    "🌤️ Good afternoon! Innikum productive ah irukanum 💯",
    "🌤️ Good afternoon! Saptingala illa fasting ah? 😏",
    "🌤️ Good afternoon! Recharge pannunga da 🔋",
    "🌤️ Good afternoon! Chill pannitu next half start pannunga 😎"
]


evening_msgs = [
    "🌆 Good evening da makkal",
    "🌆 Good evening! ☕ Tea time da",
    "🌆 Good evening! Evening chill vibes 😌",
    "🌆 Good evening! Work mudichacha? 😏",
    "🌆 Good evening! Konjam relax pannunga 😌",
    "🌆 Good evening! Tea kudichacha illa innum wait ah ☕",
    "🌆 Good evening! Day epdi pochu da 😎",
    "🌆 Good evening! Stress ellam release pannunga 💆",
    "🌆 Good evening! Chill mode on 😏",
    "🌆 Good evening! Work ah mudichitu relax pannunga 🔥",
    "🌆 Good evening! Coffee/Tea break time ☕",
    "🌆 Good evening! Innikum sema work pannirukeenga 😎",
    "🌆 Good evening! Little break eduthu refresh aagunga ⚡",
    "🌆 Good evening! Evening vibes enjoy pannunga 🌇",
    "🌆 Good evening! Half tired ah irukingala 😏",
    "🌆 Good evening! Relax pannitu night ku ready aagunga 🔥",
    "🌆 Good evening! Mind ah calm pannunga 😌",
    "🌆 Good evening! Innikum nalla perform pannirukeenga 💯",
    "🌆 Good evening! Tea + snacks ready ah? 😋",
    "🌆 Good evening! Konjam slow down pannunga da 😎"
]


night_msgs = [
    "🌙 Good night da makka",
    "🌙 Good night! Rest well 😴",
    "🌙 Good night! Tomorrow fresh start 🔥",
    "🌙 Good night! Innikum nalla pannirukeenga 💯",
    "🌙 Good night! Relax pannitu nalla thoongunga 😌",
    "🌙 Good night! Day full ah work pannitinga 😎",
    "🌙 Good night! Mind ah calm pannitu sleep pannunga 🧘",
    "🌙 Good night! Tomorrow stronger comeback 🔥",
    "🌙 Good night! Stress ellam vidunga 😴",
    "🌙 Good night! Nalla rest eduthu recharge aagunga 🔋",
    "🌙 Good night! Innaiku mudinchu... next level naal varuthu 😏",
    "🌙 Good night! Sweet dreams da 😴",
    "🌙 Good night! Late ah thoongadhe 😏",
    "🌙 Good night! Body ku rest romba mukkiyam 💪",
    "🌙 Good night! Tomorrow goals ready ah vechukonga 🔥",
    "🌙 Good night! Peaceful ah thoongunga 🌌",
    "🌙 Good night! Day complete... proud ah iru 😎",
    "🌙 Good night! Konjam relax pannitu sleep pannunga 😌",
    "🌙 Good night! Dream big da 🔥",
    "🌙 Good night! Alarm set pannitingala? ⏰"
]


midnight_msgs = [
    "🌌 Good night da makkaa (Midnight special 😏)",
    "🌌 Good night! Innum thoongala? 😏",
    "🌌 Good night! Midnight vibes on 🌙",
    "🌌 Good night! Late ah wake ah irukingala 😏",
    "🌌 Good night! Time 12 da… sleep panna poriya illa scroll ah? 📱",
    "🌌 Good night! Midnight thoughts start aagiducha 👀",
    "🌌 Good night! Thoonga da 😴 health mukkiyam",
    "🌌 Good night! Silent night… calm mind 😌",
    "🌌 Good night! Late night la overthinking ah? 😏",
    "🌌 Good night! Phone va vachitu thoongu da 😴",
    "🌌 Good night! Night owl ah maaritingala 😎",
    "🌌 Good night! Dreams ku time da 🌙",
    "🌌 Good night! Midnight la motivation varudha illa sleep ah? 😏",
    "🌌 Good night! Tomorrow ku energy save pannunga 🔋",
    "🌌 Good night! Dark la irundhaalum mind bright ah irukanum ✨",
    "🌌 Good night! Idhu rest time da… work illa 😌",
    "🌌 Good night! Late ah thoonga koodathu 😏",
    "🌌 Good night! Innikum close… tomorrow new start 🔥",
    "🌌 Good night! Eyes close pannunga da 😴",
    "🌌 Good night! Midnight la peace feel pannunga 🌌"
]



async def send_morning(context):
    await context.bot.send_message(chat_id=GROUP_ID, text=random.choice(morning_msgs))

async def send_afternoon(context):
    await context.bot.send_message(chat_id=GROUP_ID, text=random.choice(afternoon_msgs))

async def send_evening(context):
    await context.bot.send_message(chat_id=GROUP_ID, text=random.choice(evening_msgs))

async def send_night(context):
    await context.bot.send_message(chat_id=GROUP_ID, text=random.choice(night_msgs))

async def send_midnight(context):
    await context.bot.send_message(chat_id=GROUP_ID, text=random.choice(midnight_msgs))
# =========================
# 3. LEAVE MESSAGE
# =========================
async def member_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member

    if result.old_chat_member.status != "left" and result.new_chat_member.status == "left":
        user = result.new_chat_member.user
        name = f"<a href='tg://user?id={user.id}'>{user.first_name}</a>"

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"👋 {name} left the group",
            parse_mode="HTML"
        )


# =========================
# MAIN
# =========================
app = ApplicationBuilder().token(TOKEN).build()

# Admin trigger
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, admin_reply))

# Leave detection
app.add_handler(ChatMemberHandler(member_update, ChatMemberHandler.CHAT_MEMBER))

# Scheduler
from datetime import time
import pytz

IST = pytz.timezone("Asia/Kolkata")

job_queue = app.job_queue

job_queue.run_daily(send_morning, time=time(7, 0, tzinfo=IST))
job_queue.run_daily(send_afternoon, time=time(13, 0, tzinfo=IST))
job_queue.run_daily(send_evening, time=time(16, 0, tzinfo=IST))
job_queue.run_daily(send_night, time=time(21, 0, tzinfo=IST))
job_queue.run_daily(send_midnight, time=time(0, 0, tzinfo=IST))



# 👇 scheduler here

print("🔥 hy deena Bot is running...")
app.run_polling()
