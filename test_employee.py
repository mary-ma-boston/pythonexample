import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Corey', 'Schafer',50000)
        emp_2 = Employee('Sue','Smith', 60000)

        self.assertEqual(emp_1.email(),'Corey.Schafer@gmail.com')
        self.assertEqual(emp_2.email(),'Sue.Smith@gmail.com')


    def test_fullname(self):
        emp_1 = Employee('Corey','Schafer',50000)
        emp_2 = Employee('Sue','Smith', 60000)

        self.assertEqual(emp_1.fullname(),'Corey Schafer')
        self.assertEqual(emp_2.fullname(),'Sue Smith')


    def test_apply_raise(self):
        emp_1 = Employee('Corey','Schafer',50000)
        emp_2 = Employee('Sue','Smith', 60000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay,52500)
        self.assertEqual(emp_2.pay,63000)


if __name__=='__main__':
   unittest.main()


    


    