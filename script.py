from translate import Translator
translator = Translator(to_lang="en",from_lang="autodetect")
try:
	with open('lyrics3.txt', mode='r') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		print(translation)
except FileNotFoundError as e:
	print("Your file path is incorrect.")

