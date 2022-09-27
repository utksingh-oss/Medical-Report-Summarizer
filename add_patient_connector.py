import mysql.connector as connector

class PatientHelper:
	def __init__(self):
		self.con = connector.connect(host = 'localhost',port = '3306', user='root',password = '858684Arsh123!',database = 'final_year_project')
		query = 'create table if not exists patients(patientId   INT NOT NULL AUTO_INCREMENT PRIMARY KEY, first_name varchar(20) , middle_name varchar(20), last_name varchar(20), email_id varchar(60) , phone_no varchar(12) , address varchar(100) , gender varchar(7) , dob date)'		
		cur = self.con.cursor()
		cur.execute(query)
		print("Created")

	#Insert Patient's Details
	def insert_user(self , u_first_name , u_middle_name , u_last_name , u_email_add , u_phone_no , u_address , u_gender,u_dob):
		query = "insert into patients(first_name , middle_name , last_name , email_id, phone_no , address , gender ,dob) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(u_first_name , u_middle_name , u_last_name , u_email_add,u_phone_no , u_address , u_gender,u_dob)
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()
		return cur.lastrowid

	#Fetching Patient's Data:= returns a tuple
	def fetch_single(self , patient_id):
		query = "select * from patients where patientId = '{}'".format(patient_id)
		cur = self.con.cursor(buffered = True)
		cur.execute(query)
		for row in cur:
			return row

	#returns a list of result
	def fetch_all(self):
		query = "select * from patients"
		cur = self.con.cursor(buffered = True)
		cur.execute(query)
		res = []
		for row in cur:
			res.append(row)
		return res

	def delete_user(self , patient_d):
		query = "delete from patients where patientId = {}".format(patient_id)
		cur = self.con.cursor()
		cur.execute(query)
		self.con.commit()

		
	def update_patient(self):
		pass

