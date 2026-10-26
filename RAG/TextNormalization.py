class TextNormalization:
    def __init__(self,text):
        self.text=text
        
    def lower_case(self,text):
         return text.lower()
    
    def removing_spaces(self,text):
            import re
            removespace= re.sub(r'\s+', ' ', text)
            return removespace.strip()

    def remove_punctuation(self,text):
        import string
        return text.translate(str.maketrans('', '', string.punctuation))
               
    def expand_contractions(self, text):
        import contractions
        return contractions.fix(text)

    def correct_spelling(self, text):
        from textblob import TextBlob
        corrected_words = TextBlob(text).correct()
        return str(corrected_words)

    def call(self):
        self.text=self.lower_case(self.text)
        self.text=self.removing_spaces(self.text)
        self.text=self.remove_punctuation(self.text)
        self.text=self.expand_contractions(self.text)
        self.text=self.correct_spelling(self.text)
        return self.text

cl=TextNormalization("I have core!cte t'he wods for txt normalization")
# print(cl.lower_case(cl.text))
# print(cl.removing_spaces(cl.text))
# print(cl.remove_punctuation(cl.text))
# print(cl.expand_contractions(cl.text))
# print(cl.correct_spelling(cl.text))
print(cl.call())
#----------------------------------------------------------------------------------------


# class TextNormalization:
#     def init__(self, data):
#         self.text = data
        
#     def expand(self):
#         import contractions
#         self.data = contractions.fix(self.data)
        
#     def correcting(self):
#         from textblob import TextBlob
#         obj_textblob = TextBlob(self.data)
#         self.data = str(obj_textblob.correct())

#     def lower(self):
#         self.data = self.data.lower()

#     def removing_punctuation(self):
#         punc=input('Punctuation is need or not yes/no')
#         if punc == 'yes':
#             pass
#         else:
#             import string
#             import re
#             var = string.punctuation
#             self.data = re.sub(f'[{var}]',' ',self.data)
#         self.data = self.data

#     def removing_space(self):
#         import re
#         self.data = re.sub(r'\s+',' ',self.data)

#     def removing_emoji(self):
#         import emoji
#         self.data = emoji.replace_emoji(self.data,'?')
#     def call(self):
#         self.expand=self.expand(self.data)
#         self.correcting=self.correcting(self.data)
#         self.lower()=self.lower(self.data)
#         self.removing_punctuation()=self.removing_punctuation(self.data)
#         self.removing_space()=self.removing_space(self.data)
#         self.removing_emoji()=self.removing_emoji(self.data)
#         return self.data

# cl=TextNormalization("I have core!cte t'he wods for txt normalization")
# cl.call()