class salary():
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_Salary(self):
        return self.pay*12+self.bonus

class employee():
    def __init__(self,firstname,lastname,age,pay,bonus):
        self.first=firstname
        self.lastname=lastname
        self.age=age
        self.obj_salary=salary(pay,bonus)

    def totalsalary(self):
        return self.obj_salary.annual_Salary()


emp=employee('Mohan','hazaru',23,1000,200)
print emp.totalsalary()



