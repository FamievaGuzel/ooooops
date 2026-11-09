class BaseParagraph:
    def __init__(self, width):
        self.width = width
        self.words = []
        self.current_line = []

    def add_word(self, word):
        current_length = sum(len(w) for w in self.current_line) + len(self.current_line)
        if current_length + len(word) <= self.width:
            self.current_line.append(word)
        else:
            self._print_line(self.current_line)
            self.current_line = [word]

    def _print_line(self, line):
        pass
    def end(self):
        if self.current_line:
            self._print_line(self.current_line)
            self.current_line = []


class LeftParagraph(BaseParagraph):
    def _print_line(self, line):
        text = ' '.join(line)
        print(text.ljust(self.width))


class RightParagraph(BaseParagraph):
    def _print_line(self, line):
        text = ' '.join(line)
        print(text.rjust(self.width))

# Ваш код

lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
        