class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', '-']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for p in punctuation:
                    text = text.replace(p, '')

                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                position = words.index(word) + 1
                results[file_name] = position
        return results

    def count(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                results[file_name] = count
        return results

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))





