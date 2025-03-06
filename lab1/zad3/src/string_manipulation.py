class StringManipulation():
    def reverse_string(self, str):
        return str[::-1]
    
    def count_words(self, str):
        return len(str.split()) if str.strip() else 0
    
    def capitalized_words(self, str):
        return ' '.join(str.capitalize() if str else str for str in str.split())
    