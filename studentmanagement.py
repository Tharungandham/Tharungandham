#this file is for git practice purpose 
import pickle
class Student:
  def __init__(self):
    for i in range(1):
      self.id=int(input("enter the student id : "))
      self.name=input("enter the student name : ")
      self.age=int(input("enter the student age : "))
      self.marks=float(input("enter the student marks : "))
class StudentManager:
  def add_student(self):
    s1=Student()
    self.stu_lst=[]
    self.stu_lst.append(s1)
  def save_to_file(self,filename):
    with open(filename,'wb') as wf:
      pickle.dump(self.stu_lst,wf)
  def load_file(self,filename):
    with open(filename,"rb") as fr:
      self.fileread=pickle.load(fr)
      print(self.fileread)
  def search_student(self):
    student_id=int(input("enter the student id to search :"))
    student_delete=int(input("enter the student id to delete :"))
    for stu in self.fileread:
      if stu.id==student_id:
        print(f"student id {stu.id},student name {stu.name},age {stu.age}, marks {stu.marks}")
      if stu.id==student_delete:
        self.fileread.remove(stu)
    print(self.fileread)


if __name__=="__main__":
  m=StudentManager()
  m.add_student()
  m.save_to_file("student")
  m.load_file("student")
  m.search_student()


