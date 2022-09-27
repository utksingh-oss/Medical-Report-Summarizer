import mysql.connector as connector
from datetime import date


class PatientDiagHelper:
	def __init__(self):
		self.con = connector.connect(host = 'localhost', port = '3306', user='root', password = '858684Arsh123!',database = 'final_year_project')
		query = 'create table if not exists patients_diagnosis(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,patient_id INT NOT NULL , FOREIGN KEY(patient_id) References patients(patientId),report_date DATE, details MEDIUMTEXT, remarks TEXT)'
		cur = self.con.cursor()
		cur.execute(query)
		print("Created")

	def insert_patients_diag(self , patient_id, diag , remark):
		query = "insert into patients_diagnosis(patient_id ,report_date, details , remarks) values({},'{}','{}','{}')".format(patient_id,date.today(), diag ,remark)
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()
		print("Inserted Successfully")

	def get_patients_diag(self , patient_id):
		query = "select * from patients_diagnosis"
		cur = self.con.cursor(buffered = True)
		cur.execute(query)
		res = []
		for row in cur:
			res.append(row)
		return res

