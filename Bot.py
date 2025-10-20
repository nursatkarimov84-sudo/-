import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = "8380445579:AAHMsiZ1bdmli0Zt8sm3FOngjOGnZYozywM"

EMOJIS = ["😊", "😘", "😍", "🥰", "😏", "❤️", "🔥", "💋", "💕", "🎀", "🌟", "⚡", "🌈", "🌸", "💫", "✨", "🎉", "🫂", "🤗", "👄"]

class RomanticBot:
    def __init__(self, token):
        self.application = Application.builder().token(token).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        # Основные команды
        commands = [
            ('start', self.start),
            ('help', self.help),
            ('obnyt', self.obnyt),
            ('pocelovat', self.pocelovat),
            ('gladit', self.gladit),
            ('prilitat', self.prilitat),
            ('laskat', self.laskat),
            ('shepotat', self.shepotat),
            ('strast', self.strast),
            ('jelat', self.jelat),
            ('soblaznyat', self.soblaznyat),
            ('igrat', self.igrat),
            ('fantazirovat', self.fantazirovat),
            ('flirt', self.flirt),
            ('romantika', self.romantika),
            ('blijost', self.blijost),
            ('privlekat', self.privlekat),
            ('iskushat', self.iskushat),
            ('machta', self.machta),
            ('uvlechenie', self.uvlechenie),
            ('lapki', self.lapki),
            ('smeatsa', self.smeatsa),
            ('tancovat', self.tancovat),
            ('podarok', self.podarok),
            ('kompliment', self.kompliment)
        ]
        
        for command, handler in commands:
            self.application.add_handler(CommandHandler(command, handler))
        
        # Обработка всех сообщений для реакции на русские слова
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        welcome_text = """💖 Привет! Я романтичный бот! 💖

🤖 *Как использовать:*
• Просто напиши команду
• Или напиши в чате слова: *обнять, поцеловать, погладить, прижаться, ласкать, шептать, флиртовать* и я отреагирую!

❤️ *Нежные команды:*
/obnyt - обнять
/pocelovat - поцеловать  
/gladit - погладить
/prilitat - прижаться
/laskat - ласкать
/shepotat - шептать
/romantika - романтика
/flirt - флиртовать
/lapki - лапки

🔥 *Страстные команды:*
/strast - страсть
/jelat - желать
/soblaznyat - соблазнить
/privlekat - привлекать
/iskushat - искушать
/blijost - близость

💫 *Игривые команды:*
/igrat - играть
/fantazirovat - фантазировать
/machta - мечтать
/uvlechenie - увлечение
/smeatsa - смеяться
/tancovat - танцевать
/podarok - подарок
/kompliment - комплимент

*Просто напиши команду или одно из волшебных слов!* 💕"""
        await update.message.reply_text(welcome_text, parse_mode='Markdown')

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await self.start(update, context)

    # Нежные команды
    async def obnyt(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        hugs = [
            f"💕 {update.effective_user.first_name} нежно обнимает тебя и прижимает к груди {random.choice(EMOJIS)}",
            f"🤗 Теплые объятия от {update.effective_user.first_name}! Чувствуешь как бьется мое сердце? 💓",
            f"🫂 {update.effective_user.first_name} крепко-крепко обнимает тебя, не желая отпускать!",
            f"💝 Обнимашки с {update.effective_user.first_name}! Так тепло и уютно... 🌸",
            f"🌟 {update.effective_user.first_name} обнимает тебя так нежно, что на глазах выступают слезы счастья 🥲"
        ]
        await update.message.reply_text(random.choice(hugs))

    async def pocelovat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        kisses = [
            f"💋 {update.effective_user.first_name} нежно целует тебя в губы {random.choice(EMOJIS)}",
            f"😘 Теплый поцелуй от {update.effective_user.first_name}! Чувствуешь страсть? 🔥",
            f"👄 {update.effective_user.first_name} страстно целует тебя, запуская пальцы в твои волосы 💕",
            f"💋 Нежные поцелуи по всему телу от {update.effective_user.first_name}... 💫",
            f"🥰 {update.effective_user.first_name} покрывает твое лицо нежными поцелуями, как весенний дождь 🌸"
        ]
        await update.message.reply_text(random.choice(kisses))

    async def gladit(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"✨ {update.effective_user.first_name} нежно гладит тебя по волосам {random.choice(EMOJIS)}",
            f"🖐️ Легкие прикосновения пальцев {update.effective_user.first_name} скользят по твоей коже... 🔥",
            f"💫 {update.effective_user.first_name} ласково поглаживает твою спину, вызывая мурашки 🌟",
            f"🌸 Нежные поглаживания от {update.effective_user.first_name} заставляют тебя расслабиться... 💕",
            f"🦋 Пальцы {update.effective_user.first_name} нежно скользят по твоей коже, как бабочки 🦋"
        ]
        await update.message.reply_text(random.choice(responses))

    async def prilitat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"🌟 {update.effective_user.first_name} нежно прижимается к тебе {random.choice(EMOJIS)}",
            f"💞 Так уютно рядом с {update.effective_user.first_name}! Никуда не отпущу... 🌙",
            f"🫂 {update.effective_user.first_name} прижимается к тебе, чувствуя твое тепло...",
            f"🌙 {update.effective_user.first_name} нежно прильнул к тебе под одеялом... 💫"
        ]
        await update.message.reply_text(random.choice(responses))

    async def laskat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"💖 {update.effective_user.first_name} нежно ласкает тебя {random.choice(EMOJIS)}",
            f"🌸 Ласковые прикосновения {update.effective_user.first_name} заставляют тебя таять...",
            f"🌟 {update.effective_user.first_name} окружает тебя заботой и лаской",
            f"💫 Каждое прикосновение {update.effective_user.first_name} наполнено нежностью..."
        ]
        await update.message.reply_text(random.choice(responses))

    async def shepotat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"👂 {update.effective_user.first_name} шепчет тебе на ушко ласковые слова... {random.choice(EMOJIS)}",
            f"💬 Тихый шепот {update.effective_user.first_name}: 'Ты так прекрасен...' 🔥",
            f"🫦 {update.effective_user.first_name} шепчет горячие слова, от которых ты краснеешь... 🙈",
            f"🌙 {update.effective_user.first_name} шепчет тебе сладкие обещания на ночь... 💫"
        ]
        await update.message.reply_text(random.choice(responses))

    # Страстные команды
    async def strast(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"🔥 Страсть {update.effective_user.first_name} к тебе разгорается все сильнее! {random.choice(EMOJIS)}",
            f"💥 {update.effective_user.first_name} чувствует такую сильную страсть, что не может думать ни о чем другом! ❤️‍🔥",
            f"⚡ Искры страсти летят между вами! {update.effective_user.first_name} не может устоять! 💫",
            f"🌹 Страсть {update.effective_user.first_name} к тебе подобна огню, который невозможно потушить! 🔥"
        ]
        await update.message.reply_text(random.choice(responses))

    async def jelat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"💗 {update.effective_user.first_name} желает тебя всем своим существом... {random.choice(EMOJIS)}",
            f"🫦 Жгучее желание в глазах {update.effective_user.first_name} говорит само за себя... 🔥",
            f"🌟 {update.effective_user.first_name} хочет тебя так сильно, что дрожит от нетерпения... 💕",
            f"🌙 Желание {update.effective_user.first_name} растет с каждой минутой, проведенной рядом с тобой... ✨"
        ]
        await update.message.reply_text(random.choice(responses))

    async def soblaznyat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"💃 {update.effective_user.first_name} соблазнительно смотрит на тебя... {random.choice(EMOJIS)}",
            f"🎭 {update.effective_user.first_name} играет с тобой в опасную игру соблазна... Готов рискнуть? ⚡",
            f"😏 {update.effective_user.first_name} знает как тебя соблазнить... И у него это отлично получается! 🔥",
            f"💋 Искусство соблазна от {update.effective_user.first_name} заставляет твое сердце биться чаще... 💓"
        ]
        await update.message.reply_text(random.choice(responses))

    # Игривые команды
    async def igrat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"😈 {update.effective_user.first_name} начинает игривые шалости... {random.choice(EMOJIS)}",
            f"🎮 {update.effective_user.first_name} играет с тобой в опасную игру! Готов проиграть? 😏",
            f"👻 Игривое настроение {update.effective_user.first_name} заразительно! Давай повеселимся! 🎉",
            f"🦊 {update.effective_user.first_name} хитро улыбается, придумывая новую игру... 💫"
        ]
        await update.message.reply_text(random.choice(responses))

    async def fantazirovat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"🌌 {update.effective_user.first_name} делится своей самой смелой фантазией с тобой... {random.choice(EMOJIS)}",
            f"💭 А что если... {update.effective_user.first_name} предлагает воплотить наши мечты? 🌟",
            f"🌈 {update.effective_user.first_name} представляет нас вместе в романтичном месте... 🏝️",
            f"🎠 Фантазии {update.effective_user.first_name} уносят вас в мир грез и наслаждений... 💖"
        ]
        await update.message.reply_text(random.choice(responses))

    async def flirt(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"😏 {update.effective_user.first_name} игриво флиртует с тобой! {random.choice(EMOJIS)}",
            f"💋 Флирт от {update.effective_user.first_name} заставляет сердце биться чаще! 💓",
            f"🎭 {update.effective_user.first_name} заигрывает с тобой, бросая многозначительные взгляды... 👀",
            f"🌹 Искусство флирта от {update.effective_user.first_name} сводит тебя с ума... 🔥"
        ]
        await update.message.reply_text(random.choice(responses))

    async def romantika(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"💖 {update.effective_user.first_name} создает романтическую атмосферу! {random.choice(EMOJIS)}",
            f"🌹 Романтика с {update.effective_user.first_name}... Свечи, музыка и только мы двое... 🕯️",
            f"✨ {update.effective_user.first_name} настроен на романтический лад! Приготовься к волшебству! 🌟",
            f"🎶 Романтический вечер с {update.effective_user.first_name} обещает быть незабываемым... 💫"
        ]
        await update.message.reply_text(random.choice(responses))

    async def blijost(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"🫂 {update.effective_user.first_name} хочет быть с тобой максимально близко... {random.choice(EMOJIS)}",
            f"💘 Этот момент слишком интимен для слов... {update.effective_user.first_name} просто смотрит в твои глаза... 👁️",
            f"🌹 {update.effective_user.first_name} создает атмосферу полной близости и доверия... ✨",
            f"🌟 Близость с {update.effective_user.first_name} заставляет мир вокруг исчезать... 💖"
        ]
        await update.message.reply_text(random.choice(responses))

    async def privlekat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"💫 {update.effective_user.first_name} неотразимо привлекателен! {random.choice(EMOJIS)}",
            f"🎯 {update.effective_user.first_name} привлекает твое внимание магнетическим взглядом!",
            f"✨ Ты не можешь устоять перед {update.effective_user.first_name}! Это просто невозможно! 🔥",
            f"🌹 Притяжение между вами становится все сильнее с каждой минутой... 💕"
        ]
        await update.message.reply_text(random.choice(responses))

    async def iskushat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"😈 {update.effective_user.first_name} искушает тебя... {random.choice(EMOJIS)}",
            f"🍎 {update.effective_user.first_name} предлагает запретный плод! Устоишь? 😏",
            f"💋 Искушение от {update.effective_user.first_name} слишком сильно! Ты уже проиграл... 🔥",
            f"🎭 Игра в искушение с {update.effective_user.first_name} становится все опаснее... ⚡"
        ]
        await update.message.reply_text(random.choice(responses))

    async def machta(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"🌠 {update.effective_user.first_name} мечтает о тебе! {random.choice(EMOJIS)}",
            f"💭 Мечты {update.effective_user.first_name} сбываются с тобой! Это судьба! ✨",
            f"🌈 {update.effective_user.first_name} представляет вас вместе в самых смелых мечтах!",
            f"🌟 Мечты о {update.effective_user.first_name} становятся самой прекрасной реальностью... 💖"
        ]
        await update.message.reply_text(random.choice(responses))

    async def uvlechenie(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"🎯 {update.effective_user.first_name} увлечен тобой! {random.choice(EMOJIS)}",
            f"💫 Увлечение {update.effective_user.first_name} растет с каждой минутой! Остановиться невозможно! 🔥",
            f"✨ {update.effective_user.first_name} не может оторвать от тебя глаз! Ты завораживаешь!",
            f"🌹 Увлечение перерастает в нечто большее... {update.effective_user.first_name} тонет в твоих глазах... 💕"
        ]
        await update.message.reply_text(random.choice(responses))

    async def lapki(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"🐾 {update.effective_user.first_name} нежно трогает тебя лапками! {random.choice(EMOJIS)}",
            f"🖐️ Мягкие лапки {update.effective_user.first_name} ласкают твое лицо...",
            f"💕 {update.effective_user.first_name} протягивает к тебе лапки для обнимашек!",
            f"🌸 Лапки {update.effective_user.first_name} такие нежные и мягкие... 💫"
        ]
        await update.message.reply_text(random.choice(responses))

    async def smeatsa(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"😂 {update.effective_user.first_name} заразительно смеется вместе с тобой! {random.choice(EMOJIS)}",
            f"🎉 Смех {update.effective_user.first_name} такой искренний и красивый!",
            f"🤣 {update.effective_user.first_name} смеется до слез! Как же хорошо вместе!",
            f"💫 Ваш смех сливается воедино, создавая музыку счастья... 🎶"
        ]
        await update.message.reply_text(random.choice(responses))

    async def tancovat(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"💃 {update.effective_user.first_name} приглашает тебя на танец! {random.choice(EMOJIS)}",
            f"🎶 Танцы с {update.effective_user.first_name} - это pure magic!",
            f"✨ {update.effective_user.first_name} танцует только для тебя... Завораживающе!",
            f"🌟 Ваши тела движутся в унисон под романтичную музыку... 💕"
        ]
        await update.message.reply_text(random.choice(responses))

    async def podarok(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"🎁 {update.effective_user.first_name} дарит тебе подарок от всего сердца! {random.choice(EMOJIS)}",
            f"💝 Сюрприз от {update.effective_user.first_name}! Ты этого точно заслуживаешь!",
            f"🎀 {update.effective_user.first_name} приготовил для тебя нечто особенное...",
            f"✨ Этот подарок от {update.effective_user.first_name} со смыслом... Ты самый лучший! 🌟"
        ]
        await update.message.reply_text(random.choice(responses))

    async def kompliment(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        responses = [
            f"💖 {update.effective_user.first_name} говорит тебе комплимент: Ты невероятно прекрасен! {random.choice(EMOJIS)}",
            f"🌟 Твои глаза сияют ярче звезд! - шепчет {update.effective_user.first_name}",
            f"🌹 Ты делаешь этот мир лучше просто своим присутствием! - признается {update.effective_user.first_name}",
            f"✨ {update.effective_user.first_name} замирает, глядя на тебя: Ты самое красивое существо во вселенной! 💫"
        ]
        await update.message.reply_text(random.choice(responses))

    # Обработка сообщений с русскими словами
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        text = update.message.text.lower()
        
        # Словарь реакций на русские слова
        word_responses = {
            'обнять': self.obnyt,
            'поцеловать': self.pocelovat,
            'погладить': self.gladit,
            'прижаться': self.prilitat,
            'ласкать': self.laskat,
            'шептать': self.shepotat,
            'флиртовать': self.flirt,
            'страсть': self.strast,
            'желать': self.jelat,
            'соблазнить': self.soblaznyat,
            'играть': self.igrat,
            'фантазировать': self.fantazirovat,
            'романтика': self.romantika,
            'близость': self.blijost,
            'привлекать': self.privlekat,
            'искушать': self.iskushat,
            'мечтать': self.machta,
            'увлечение': self.uvlechenie,
            'лапки': self.lapki,
            'смеяться': self.smeatsa,
            'танцевать': self.tancovat,
            'подарок': self.podarok,
            'комплимент': self.kompliment
        }
        
        # Проверяем каждое слово в сообщении
        for word, handler in word_responses.items():
            if word in text:
                await handler(update, context)
                return
        
        # Если не нашли ключевых слов, отправляем случайный ответ
        random_responses = [
            f"Как мило! {random.choice(EMOJIS)}",
            f"Ты заставляешь мое сердце биться чаще! 💓",
            f"Продолжай, мне нравится! {random.choice(EMOJIS)}",
            f"Ты такой прекрасный! 🌟",
            f"От твоих слов становится так тепло... 🌸",
            f"Шепчи мне это на ушко... 👂 {random.choice(EMOJIS)}",
            f"Твои слова как музыка для моей души... 🎶"
        ]
        await update.message.reply_text(random.choice(random_responses))

    def run(self):
        """Запуск бота"""
        self.application.run_polling()

if __name__ == '__main__':
    bot = RomanticBot(BOT_TOKEN)
    print("Бот запущен! 🚀")
    bot.run()
