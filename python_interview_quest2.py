class Employee:

    employee_id = 0

    def __init__(self,name,mobile_number):
        self.name =name
        self.mobile_number = mobile_number
        self.id = self.employee_id_p()


    @classmethod
    def employee_id_p(cls):
       cls.employee_id +=1
       return  cls.employee_id

    def get_details(self):
        return  f"The employee name:{self.name}, ID:{self.id}, number:{self.mobile_number}"


obj = Employee("Sarath","8092891748",)
obj_1 = Employee("ravi","8092891548",)
obj_2 = Employee("ram","80928917908")

print(obj.get_details())
print(obj_1.get_details())
print(obj_2.get_details())






# Write a function that parses the input string and returns the output string,
# Input: “3*qwer, 2*abc”
# Output:
#  “qwerqwerqwerabcabc”


# 9910057763


def process_string(input_str):
    parts = input_str.split(",")
    result = ""

    for part in parts:
        count, substr = part.split("*")
        count =     int(count.strip())
        substr = substr.strip()
        result += substr * count

    return result


# Example usage
input_str = "3*qwer, 2*abc"
output = process_string(input_str)
print(output)  # Output: "qwerqwerqwerabcabc"


def string_process_data(input_str):
    parts = input_str.split(",")
    result =''

    for part in  parts:
        count,substr = part.split('*')
        count = int(count.strip())
        substr = substr.strip()
        print(count)
        result += substr * count
    return result

input_str = "3*qwer, 2*abc"
output_string = string_process_data(input_str)
print(output_string)


class Employee:

    def __init__(self, name: str, salary: str):
        self.name = name
        self.salary = salary


class Tester(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def test(self):
        print("{} is testing".format(self.name))


class Developer(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def develop(self):
        print("{} is developing".format(self.name))


class Company:

    def __init__(self, name: str):
        self.name = name

    def work(self, employee):
        if isinstance(employee, Developer):
            employee.develop()
        elif isinstance(employee, Tester):
            employee.test()
        else:
            raise Exception("Unknown employee")




from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name: str, salary: str):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class Tester(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def test(self):
        print("{} is testing".format(self.name))

    def work(self):
        self.test()

class Developer(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def develop(self):
        print("{} is developing".format(self.name))

    def work(self):
        self.develop()

class Company:

    def __init__(self, name: str):
        self.name = name

    def work(self, employee: Employee):
        employee.work()



carbon = Company("Carbon")
developer = Developer("Nusret", "1000000")
tester = Tester("Someone", "1000000")
carbon.work(developer) # Will print Nusret is developing
carbon.work(tester) # Will print Someone is testing




# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")

# def welcome_decorator(func):
#     def wrapper(*args):
#         result = func(*args)
#         print("The welcome decorator",result)
#         return result
#     return wrapper

# @welcome_decorator
# def welcome(s):
#     return s

# op = welcome("Python")


v = {"g":"Google","a":"Amazon","m":"meta"}
print(v)

go = v.get('g')
print(go)
am = v.get('a')
print(am)
me = v.get('m')
print(me)


first = [1,2,3]
second = [4,5,6]
data = list(map(lambda x,y:x**y,first,second))
print(data)



# select max(salary) as second_hieghest_salary from employees
# where  salary< (select max(salary) from employees)
#
#
#
# select p.product_name,p.sku,order_name,order_sku,line_number,order_line_number from product as p
#  inner join order
#  on
#  p.id = order_product_id
#  and
#  left join order_line
#  on
#  order_line.id = order.id
#  order by p.product_name,p.sku