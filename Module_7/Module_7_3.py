test_file = 'test_file.txt'

file = open(test_file, 'w')
file.write("It's a text for task Найти везде, \
Используйте его для самопроверки. Успехов в решении задачи! \
text text text")
file.close()

class  WordsFinder:
    file_names = []
   
    def __init__(self, *names):
        self.names = names
        self.file_names.append(*self.names)
        #print(self.file_names)
       
    def get_all_words(self):
        all_words = {}
       
        for f_name in self.file_names:
           
            with open(f_name) as file:
               
                for line in file:
                   
                    line = line.lower()
                   
                    symbol_to_remove = [',', '.', '=', '!', '?', ';', ':', ' - ']
                   
                    for symbol in symbol_to_remove:
                        line = line.replace(symbol, '')
                       
                    line = line.split()
                   
                    all_words.update({f'{f_name}' : list(line)})
                   
            return all_words  
       
    def find(self, word):
        for name, words in self.get_all_words().items():
            index = words.index(word.lower())
            return {name : index +1}
           
   
    def count(self, word):
        for name, words in self.get_all_words().items():
            return {name : words.count(word.lower())}
           
           
       
   
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего