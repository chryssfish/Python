######################################################################################################################################################################
import codecs

text=input("Give your text to encode it with ROT13\n")
encoded_text = codecs.encode(text,'rot_13')
print("The encoded text is : " , encoded_text)
