class User:
    def solve(self, n):
        pass


class Student(User):
    pass


class Teacher(User):
    def check_solution(self, user, n):
        pass


class Admin(User):
    def edit(self, n):
        pass


class SuperAdmin(Admin):
    def grant(self, user):
        pass

    
# Ваш код

print(issubclass(Student, User), issubclass(Teacher, User),
      issubclass(Admin, User), issubclass(SuperAdmin, Admin))
print(hasattr(Student, 'solve'), hasattr(Student, 'check_solution'), hasattr(Student, 'edit'))
print(hasattr(Teacher, 'check_solution'), hasattr(Teacher, 'edit'))
print(hasattr(Admin, 'edit'), hasattr(Admin, 'grant'))
print(hasattr(SuperAdmin, 'solve'), hasattr(SuperAdmin, 'edit'), hasattr(SuperAdmin, 'grant'))