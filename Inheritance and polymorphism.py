class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'你好！我是{self.name},今年{self.age}岁。')

class Teacher(Person):

    def __init__(self, name, age, department,employee_id):
        super().__init__(name, age)#调用父类（Person）构造函数
        self.department = department
        self. employee_id = employee_id
        self.coures_thought = []

    def assign_course(self, course_name):
        self.coures_thought.append(course_name)
        print(f'{self.name}将教授《{course_name}》')
        
    def introduce(self):
        print(f'我是{self.department}的{self.name}')
        print(f'工号是{self.employee_id}')
        if self.coures_thought:
            print(f'教授课程{self.coures_thought}')

def introduce_person(person):
    print('*******人员介绍*******')
    person.introduce()

person1 = Person('王', 21)
teacher1 = Teacher('张教授', 45, '计算机',11451)

introduce_person(person1)
introduce_person(teacher1)



    