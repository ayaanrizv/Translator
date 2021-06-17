from translate import Translator
translator = Translator(to_lang="en",from_lang="autodetect")
try:
	with open('lyrics.txt', mode='r') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
	with open('translated-lyrics.txt', mode='w') as my_file2:
		my_file2.write(translation)
except FileNotFoundError as e:
	print("Your file path is incorrect.")

