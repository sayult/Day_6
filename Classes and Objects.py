class Student:

    school_name = '安东军事学院'

    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.courses = []

    def enroll_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
        else:
            print('已成功选修此课程。')

    def display_info(self):
        print(f'学生:{self.name}({self.student_id})')
        print(f'专业：{self.major}')
        print(f'已选课程：{', '.join(self.courses) if self.courses else '无'}')


student1 = Student('BVVD', '114514', '银狮吞噬学')
student2 = Student('李田所', '1919810', '目力训练')

student1.display_info()