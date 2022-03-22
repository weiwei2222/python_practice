class Grade:
    def __init__(self, score):
        self.score = score
    def letter_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        elif self.score >= 60:
            return 'D'
        else:
            return 'F'
    def save_grade(self, io):
        with open(io, 'w') as file:
            file.write(f'{self.score}')
    @classmethod
    def read_grade(cls, io):
        with open(io, 'r') as file:
            while line := file.readline():
                yield Grade(int(line))