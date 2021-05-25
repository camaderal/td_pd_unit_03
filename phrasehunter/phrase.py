class Phrase():
    
    def __init__(self, phrase):
        self.phrase = phrase
        self.revealed_chars = [False if char.isalpha() else True for char in phrase]

    def __str__(self):
        return self.phrase

    def display(self):
        show_str = []
        for idx, char in enumerate(self.phrase):
            if not self.revealed_chars[idx]:
                show_str.append("_")
            else:
                show_str.append(char)

        print(" ".join(show_str))

    def check_letter(self, letter):
        num_correct = 0
        
        for idx, char in enumerate(self.phrase):
            if char.lower() == letter:
                self.revealed_chars[idx] = True
                num_correct += 1
        
        return num_correct

    def check_complete(self):
        return False not in self.revealed_chars
