class Profile:
    def __init__(self, profession):
        self.profession = profession

    def info(self):
        return ""

    def describe(self):
        print(self.profession)
        extra_info = self.info()
        if extra_info:
            print(extra_info)


class Vacancy(Profile):
    def __init__(self, profession, salary):
        super().__init__(profession)
        self.salary = salary

    def info(self):
        return f"Предлагаемая зарплата: {self.salary}"


class Resume(Profile):
    def __init__(self, profession, experience):
        super().__init__(profession)
        self.experience = experience

    def info(self):
        return f"Стаж работы: {self.experience}"
    


# Ваш код

profile = Profile('Дворник')
vacancy = Vacancy('Программист', 100000)
resume = Resume('Программист', 5)
profile.describe()
vacancy.describe()
resume.describe()
print(isinstance(vacancy, Profile), isinstance(resume, Profile))

