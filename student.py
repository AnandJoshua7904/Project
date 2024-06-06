class student:
  def __init__ (self,name,age,marks):
          self.name=name
          self.age=age
          self.marks=marks

  def get_marks(self):
        return self.__marks
  
  def set_marks(self, marks):
        self.__marks = marks 

  def __str__(self):
        return f'(name:{self.name},age:{self.age},marks:{self.marks})'     

  
student1=student("Joshua",22,500)
print(student1)
