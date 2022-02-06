import random
import speech_recognition as sr
import os
import sys
import webbrowser
import pyaudio
import pyttsx3
import os
import time
import fuzzywuzzy
import fuzz
import datetime

privet_one = ['Слушаю Вас']
privet_ie=['здрас_твуйте', 'здраствуйте рады вас видеть', 'приветствую отличны покупок']
hello= ['привет', 'превет', 'здраствуй', 'здраствуйте', 'здрасте', 'здравствуй', 'hello', 'hi']
predlojenie = ['Ассортимент товара']
opros = ['что', 'почем', 'почём', 'сколько', 'чё', 'че']
ogurec=['огурчик', 'огурчики', 'огурец', 'огурцы', 'огорцы', 'ogurec']
tomat = ['томат', 'томаты', 'помидор', 'помидоры', 'помидорчик',"тамат"]
kartofel = ['картошка',  'картофель', 'бульба', 'кортошка', 'кортофель']
morcov = ['морковь', 'марковь', 'марковка','марковь']
priceMorcov = ['морковь 21 рубль 99 копеек', "морковь мытая фасованая 46 рубль 99 копеек"]
		#	   "морковь фасованная 52 рубль 50 копеек"]
priceKartofel = ['картофель 50 рублей 50 копеек',] # 'картофель красный 51 рублей 50 копеек',
				# 'картофель экстра 52 рублей 50 копеек']
priceOgurec=['огурецы гладкие 59 рублей 90 копеек', 'огурецы средне плодные пупырчитый 59 рублей 99 копеек']
#'огурец коротко плодный 52 рублей 50 копеек', 'огурец  53 рублей 50 копеек',
			# 'огурец фасованый 600 грамм 54 рублей 50 копеек', 'огурец фасованные 450 грамм 55 рублей 50 копеек']
priceTomat=['томат 65 рублей 99 копеек']#, 'томат сливка 51 рублей 50 копеек',]
		#	'томат фасованный 600 грамм 52 рублей 50 копеек', 'помидоры чеери 53 рублей 50 копеек']
#микрафоню€0

#голос v danom work sluchie print
"""
def golos(price):
	print (price)
	return
"""
d=''

def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()

speak_engine = pyttsx3.init()

def golos(words):
	print(words) # Дополнительно выводим на экран
	os.system("say" + words)
# Проговариваем слова

# Вызов функции и передача строки 
# именно эта строка будет проговорена компьютером
golos("Привет, чем я могу помочь вам?")

# Вызов функции и передача строки 
# именно эта строка будет проговорена компьютером
speak("Привет, чем я могу памочь вам?")
	
#прием речи

'''

def slushaet():
	golos(privet_one)
	return str ( input( '').lower().split())
	print(slushaet)
	
d=slushaet()
print(' то что ввели' ,d)

	Функция command() служит для отслеживания микрофона.
	Вызывая функцию мы будет слуша ть что скажет пользователь,
	при этом для прослушивания будет использован микрофон.
	Получение данные будут сконвертированы в строку и далее
	будет происходить их проверка.
'''

def command():
	# Создаем объект на основе библиотеки
	# speech_recognition и вызываем метод для определения данных
	r = sr.Recognizer()

	# Начинаем прослушивать микрофон и записываем данные в source
	with sr.Microphone() as source:
		# Просто вывод, чтобы мы знали когда говорить
		print("Говорите")
		# Устанавливаем паузу, чтобы прослушивание
		# началось лишь по прошествию 1 секунды
		r.pause_threshold = 1
		# используем adjust_for_ambient_noise для удаления
		# посторонних шумов из аудио дорожки
		r.adjust_for_ambient_noise(source, duration=1)
		# Полученные данные записываем в переменную audio
		# пока мы получили лишь mp3 звук
		audio = r.listen(source)

	try: # Обрабатываем все при помощи исключений
		""" 
		Распознаем данные из mp3 дорожки.
		Указываем что отслеживаемый язык русский.
		Благодаря lower() приводим все в нижний регистр.
		Теперь мы получили данные в формате строки,
		которые спокойно можем проверить в условиях
		"""
		d = r.recognize_google(audio, language="ru-RU").lower()
		# Просто отображаем текст что сказал пользователь
		print("Вы сказали: " + d)
	# Если не смогли распознать текст, то будет вызвана эта ошибка
	except sr.UnknownValueError:
		# Здесь просто проговариваем слова "Я вас не поняла"
	  	# и вызываем снова функцию command() для
		# получения текста от поль
		golos("Я Вас не понял")
		d = command()

	# В конце функции возвращаем текст задания
	# или же повторный вызов функции
	return d


#перебор по слову

def perebor(obekt):
	for i in obekt:
		x=i
		golos(x)

#приветствие
		
def prive():
	for i in hello:
		if i in d: # slushaet:

			#golos(price1)
			golos(random.choice(privet_ie))
		elif i in d:
			print('no')

def fresh (tovar, price):
	for i in   tovar:
		if i in d:
			prive()#golos(price)
			speak(price)
	#	else:

#приветстаие
def prive():
	for i in hello:
		if i in d: # slushaet:
			#golos(price1)
			golos(random.choice(privet_ie))
			speak(random.choice(privet_ie))

if d  in hello:
	print ('hello')
elif d in tomat:
	print ('tomat')	
		
		#golos(priceOgurec)
		
#x = 0
#while  ogurec in d:
		
#проверка текста
# что сказал пользователь (zadanie - текст от пользователя)

'''
def makeSomething(d):
	# Попросту проверяем текст на соответствие
	# Если в тексте что сказал пользователь есть слова
	# "открыть сайт", то выполняем команду
	if 'открыть сайт' in d:
		# Проговариваем текст
		golos("Уже открываю")
		# Указываем сайт для открытия
		url = 'https://itproger.com'
		# Открываем сайт
		webbrowser.open(url)
	# если было сказано "стоп", то останавливаем прогу
	elif 'стоп' in d:
		# Проговариваем текст
		golos("Да, конечно, без проблем")
		speak("Да конечно")
		# Выходим из программы
		sys.exit()
	# Аналогично
	elif 'имя' in d:
		golos("Меня зовут Сири")

# Вызов функции для проверки текста будет 
# осуществляться постоянно, поэтому здесь
# прописан бесконечный цикл while
while True:
	makeSomething(command())	
'''
#def fresh_len():
while True:	
#	if d in hello:
	prive()
	fresh(ogurec, priceOgurec)
	fresh(tomat, priceTomat)
	fresh(kartofel, priceKartofel)
	fresh(morcov, priceMorcov)
	if 'стоп' in d:
		# Проговариваем текст
		golos("Да, конечно, без проблем")
		speak("Да конечно")
		# Выходим из программы
		sys.exit()
	d = command()