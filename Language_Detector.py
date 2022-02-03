import pycld2 as cld2

text_content = "put your text here!"
detected_language = cld2.detect(text_content)
print(detected_language)
