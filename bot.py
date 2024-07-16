import telebot
import config
import time

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
# launched = False


def review(message):
	try:
		message_to_save = int(message.text)
		# markup = types.InlineKeyboardMarkup()
		# item1 = types.InlineKeyboardButton("Stop the timer")
		# markup.add(item1)

		bot.send_message(message.chat.id, f"Seconds left: {message_to_save}")
		for seconds_left in range(message_to_save - 1, -1, -1):
			time.sleep(1)
			bot.send_message(message.chat.id, f"Seconds left: {seconds_left}")
			# launched = True
			# if message.text == "Stop the timer":
			# 	message_to_save = 0

	except ValueError:
		bot.send_message(message.chat.id, "Try again! Its not a number!?")
		review(message)


@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
	item1 = types.KeyboardButton("🤾‍♂️ Sport")
	item2 = types.KeyboardButton("🍉 Muscle building diet")
	item3 = types.KeyboardButton("😴 Sleep")
	item4 = types.KeyboardButton("⌚ Timer")
	item5 = types.KeyboardButton("💪 Motivation to train")
	markup.add(item1, item2, item3, item4, item5)

	bot.send_message(message.chat.id, "Welcome {0.first_name}, AllAboutSport is the bot that will assist you in your way of following Healthy LifeStyle. I have over twenty videos about training muscles of each of your body part. And for equipment all you need is just HORIZONTAL BAR, bars located in almost every park. Just choose what you need and enjoy your training! 🏅".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text(message):
	if message.chat.type == 'private':
		if message.text == '🤾‍♂️ Sport': 
			markup = types.InlineKeyboardMarkup(row_width=3)
			shoulders = types.InlineKeyboardButton(text='Shoulder', url='https://youtu.be/qoZSsuKvGs4?si=8853epTTPSxRHi8K')
			chest = types.InlineKeyboardButton(text='Chest', url='https://youtu.be/BkS1-El_WlE?si=HrtFkMGVuYdH5F8V')
			biceps = types.InlineKeyboardButton(text='Biceps', url='https://youtu.be/Ukc6DzX17Sc?si=wKGsDDiEMCtYifgG')
			forearms = types.InlineKeyboardButton(text='Forearms', url='https://youtu.be/32Sh5yvm4pg?si=PuiPKNv0G1QTp-TX')
			abss = types.InlineKeyboardButton(text='Abs', url='https://youtu.be/Bg-vBfORcgo?si=f4gqkuqYQ0EZYRyG')
			Quads = types.InlineKeyboardButton(text='Quads', url='https://youtu.be/_wARCz4ckBI?si=O-6VZgFSLQ41jysy')
			traps = types.InlineKeyboardButton(text='Trapezius', url='https://youtu.be/MBzJWoKPJcY?si=3Lgh45yRj9iKXwAF')
			rhomb = types.InlineKeyboardButton(text='Rhomboids', url='https://youtu.be/KiJgMIPNYB4?si=T9-FOHq6JbssYlmT')
			tricp = types.InlineKeyboardButton(text='Triceps', url='https://youtu.be/gre8lBLSH7w?si=ksJAJV7t5EAKCeTO')
			Lats = types.InlineKeyboardButton(text='Lats', url='https://youtu.be/mjnseqLiVXM?si=1Al6cJkywgQbRXtk')
			lowerback = types.InlineKeyboardButton(text='Lower Back', url='https://youtu.be/cVnIAfmEox0?si=sbHJThw1mnsu2WTy')
			glutes = types.InlineKeyboardButton(text='Glutes', url='https://youtu.be/rsxKcJVTtUw?si=9iD9DK2Krxw-y9aC')
			hams = types.InlineKeyboardButton(text='Hamstrings', url='https://youtu.be/9N3kVU_tj7s?si=1ntruNw3e9TH-a4P')
			calves = types.InlineKeyboardButton(text='Calves', url='https://youtu.be/-OYGKgwOcJ8?si=P5g_qKG3Og-tj7uk')
			comp = types.InlineKeyboardButton(text='Overall(recommended)', url='https://youtu.be/-MRNjTr6xrE?si=OMTf4GNAELc1D_kR')
			calis = types.InlineKeyboardButton(text='C A L I S T H E N I C S 🤫', url='https://youtu.be/vczr0WuYK9g?si=gU6-Nxto6Qt04qc3')
			calis2 = types.InlineKeyboardButton(text='C A L I S T H E N I C S (2) ✊', url='https://youtu.be/qdR0lwDx9hY?si=2OGrai2rGRa0Vc7N')

			markup.add(shoulders, chest, biceps, forearms, abss, Quads, traps, rhomb, tricp, Lats, lowerback, glutes, hams, calves, comp, calis, calis2)


			file = open('Sportsec.jpg', 'rb')
			bot.send_photo(message.chat.id, file, "Please, choose which part of your body you want to train. 😌", reply_markup=markup)

		elif message.text == '🍉 Muscle building diet':
			markup = types.InlineKeyboardMarkup(row_width=1)
			item1 = types.InlineKeyboardButton(text='I N F O R M A T I O N', url='https://youtu.be/osqvOUJjaCo?si=UnHjlcny4CI6IKlR')
			item2 = types.InlineKeyboardButton(text='M O R E  I N F O R M A T I O N', url='https://youtu.be/dinpkrcpKAk?si=s-0lIrzpAsTsWAHC')
			markup.add(item1, item2)

			bot.send_message(message.chat.id, "Here, you have all needed information! 🍇", reply_markup=markup)

		elif message.text == '😴 Sleep':
			markup = types.InlineKeyboardMarkup(row_width=1)
			item1 = types.InlineKeyboardButton(text='I N F O R M A T I O N', url='https://youtu.be/pz6TbZ3lNV8?si=NYwhsPLlBFGC7W2J')
			item2 = types.InlineKeyboardButton(text='M O R E  I N F O R M A T I O N', url='https://youtu.be/26DrJmGWsVk?si=TAwU0TdrCqpVA-zS')
			markup.add(item1, item2)

			bot.send_message(message.chat.id, "Here, you have all needed information about sleep 🛌", reply_markup=markup)

		elif message.text == '⌚ Timer':
			sent = bot.send_message(message.chat.id, "Please enter the amount of time in seconds) 🔢")
			bot.register_next_step_handler(sent, review)
			

		
		elif message.text == '💪 Motivation to train':
			markup = types.InlineKeyboardMarkup(row_width=1)
			item1 = types.InlineKeyboardButton(text='Anime training clips', url='https://www.youtube.com/playlist?list=PLIo46dKcAFlcbgN-5l-yxC-O0GQx8v4lg')
			item2 = types.InlineKeyboardButton(text='Quotes', callback_data='Quotes')
			markup.add(item1, item2)

			bot.send_message(message.chat.id, "Here, you can find some motivation!?", reply_markup=markup)
		else:
			bot.send_message(message.chat.id, "Sorry, but I dont understand this) 🙃")

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
	if callback.data == 'Quotes':
		bot.send_message(callback.message.chat.id, "“I hated every minute of training, but I said, ‘Don’t quit. Suffer now and live the rest of your life as a champion.” \n – Muhammad Ali")
		bot.send_message(callback.message.chat.id, "“If you don’t find the time, if you don’t do the work, you don’t get the results.” \n – Arnold Schwarzenegger")
	
		

if __name__ == "__main__":
    bot.polling(none_stop=True)