import mysql.connector as connector

class PatientFileHelper:
	def __init__(self):
		self.con = connector.connect(host = 'localhost', port = '3306', user='root', password = '858684Arsh123!',database = 'final_year_project')
		query = 'create table if not exists patients_files(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,patient_id INT NOT NULL , FOREIGN KEY(patient_id) References patients(patientId),file LONGBLOB NOT NULL,file_type varchar(3))'
		cur = self.con.cursor()
		cur.execute(query)
		print("Created")

	def insert_user_files(self , patient_id, file , file_type):
		sql_insert_blob_query = """insert into patients_files(patient_id,file,file_type) values(%s,%s,%s)"""
		file_blob = file.read()
		print(file_blob)
		insert_blob_tuple = (patient_id,file_blob,file_type)
		cur = self.con.cursor()
		result = cur.execute(sql_insert_blob_query,insert_blob_tuple)
		self.con.commit()
		print("Inserted Successfully")


helper = PatientFileHelper()
