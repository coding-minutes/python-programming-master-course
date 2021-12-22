<center><h2>Exercise - 22</h2> </center>

### Problem Statement :-

1. create a class **SchoolMember** , it should have following instance attributes :

- name

- age

SchoolMember should have a **introduce()** function, that should return "My name is xyz. I am abc years old."



2. create a subclass of SchoolMember called **Student**, there should be following instance attributes :

- name

- age

- my_class

- roll_no

**Note** : (Make sure you reuse the parent class attributes)

Student class should override **introduce()** function from SchoolMember class, and Student introduce() should return "I am in xyz class. My roll number is pqr."



3. create another subclass of SchoolMember with name of **Teacher**, there should be following instance attributes :

- name

- age

- subject

- salary

**Note** : (Make sure you reuse the parent class attributes)

**`Teacher class should override introduce() function from SchoolMember class, and Teacher introduce() should return "I Teach xyz subject. My salary is pqr."
`**

### Solution :-
```python
# Write only the classes and their member functions.
# No need to initialize and call functions.


class SchoolMember:
    ### Write Code for SchoolMember class ###
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    ### Code ends here ###
    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old."
    
    
class Student(SchoolMember):
     ### Write Code for Student class ###
    def __init__(self,name,age,my_class,roll_no):
        # initializing base class constructor
        super().__init__(name,age)
        self.my_class=my_class
        self.roll_no=roll_no
        
    ### Code ends here ###
    def introduce(self):
        return f"I am in {self.my_class} class. My roll number is {self.roll_no}."
    
    
class Teacher(SchoolMember):
     ### Write Code for Teacher class ###
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject=subject
        self.salary=salary
    
    ### Code ends here ###
    def introduce(self):
        return f"I Teach {self.subject} subject. My salary is {self.salary}."
    
    
```

