import unittest


students = []
# Adding the collected data to the students list
def submit_button():
  student_data = {
      "id": 100,
      "name": 'Ken',
      "course": 'IT',
      "fee": 100
  }

  students.append(student_data)


students_output = [{
      "id": 100,
      "name": 'Ken',
      "course": 'IT',
      "fee": 100
  }]

students_output_strings = [{
      "id": '100',
      "name": 'Ken',
      "course": 'IT',
      "fee": '100'
  }]

def outputTotalFee():
  global total_fee
  total_fee = sum(float(student['fee']) for student in students_output)

def outputTotalFeeString():
  global total_fee_string
  total_fee_string = sum(float(student['fee']) for student in students_output_strings)



class Test_Input(unittest.TestCase):
  def test_submit(self):
     submit_button()
     self.assertEqual(students, [{
       "id": 100,
      "name": 'Ken',
      "course": 'IT',
      "fee": 100}]
      )

  def test_output(self):
      outputTotalFee()
      self.assertEqual(total_fee, 100)

  def test_output_string(self):
      outputTotalFeeString()
      self.assertEqual(total_fee_string, 100)


if __name__ == "__main__":
  unittest.main()
