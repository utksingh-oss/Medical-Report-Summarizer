import streamlit as st 
from add_patient_connector import PatientHelper
from adding_patients_files import PatientFileHelper
from adding_patients_diag import PatientDiagHelper
from NER_Negation import Get_Info

selection = st.sidebar.radio("Navigation",["Add Patient","Add Patient's Diagnosis","Get Patient's Info"])
if selection == "Add Patient":
	st.title("Patient's Registration Form")
	first,middle,last = st.columns(3)

	first_val = first.text_input("First Name")
	mid_val = middle.text_input("Middle Name")
	last_val = last.text_input("Last Name")

	email,number = st.columns(2)

	email_val = email.text_input("Email Add.")
	num_val = number.text_input("Mobile No.")

	add_val = st.text_area("Address")

	gender, dob = st.columns(2)
	gender_val = gender.selectbox("Gender",["Male","Female","Other"])
	dob_val = dob.date_input("DOB")

	blank1 , sub , blank2 = st.columns(3)
	sub_val = sub.button("Submit Patient Details")

	if sub_val:
		patient_helper = PatientHelper()
		patient_helper.insert_user(first_val,mid_val,last_val,email_val, num_val, add_val,gender_val,dob_val)


elif selection == "Add Patient's Diagnosis":
	st.title("Add Patient's Diagnosis")
	patient_id = st.text_input("Patient's Id")
	patient_diag_det = st.text_area("Patient's Diagnosis Details")
	doctor_comment = st.text_area("Doctor's Comments")
	st.subheader("OR")
	file_type = st.selectbox("Type of File",["TXT" , "PDF" , "DOC"])
	uploaded_files = st.file_uploader("Upload Existing Files: ",accept_multiple_files = True)

	
	if st.button("Submit"):
		if len(uploaded_files) != 0:
			st.write(uploaded_files[0])
			file_upload = PatientFileHelper()
			for file in uploaded_files:
				file_upload.insert_user_files(patient_id , file , file_type)

		patient_diag_upload = PatientDiagHelper()
		patient_diag_upload.insert_patients_diag(patient_id,patient_diag_det, doctor_comment)

elif selection == "Get Patient's Info":
	st.title("Patient's Analysis")
	patient_diag_upload = PatientDiagHelper()
	patient_id = st.text_input("Patient's Id")
	text_content = ''
	if st.button("Submit"):
		get_info = Get_Info()
		res = get_info.get_data(patient_id)
		date = res[0]
		if len(res[1]) != 0:
		  st.write("The problems faced by the patient on date {} are as follows :  ".format(date))
		  text_content += "\nThe problems faced by the patient on date {} are as follows :  ".format(date)
		  count = 1
		  for k in res[1].keys():
		    st.write("[",count,"]",k)
		    text_content += "\n[" + str(count) + "]" + k
		    count+=1
		else:
		  st.write("No issues were found for patient on date {}".format(date))
		  text += "\nNo issues were found for patient on date {}".format(date)

		if len(res[2]) != 0:
		  st.write("The treatments taken by patient on {} are as follows : ".format(date))
		  text_content += "\nThe treatments taken by patient on {} are as follows : ".format(date)
		  count = 1
		  for k in res[2].keys():
		    st.write("[" , count ,"]" , k)
		    text_content +=  "\n[" + str(count) +"]"+ k
		    count+=1
		else :
		  st.write("Tests performed on patients on {} were as follows".format(date))
		  text_content += "\nTests performed on patients on {} were as follows".format(date)
		
		count = 1
		if len(res[3]) != 0:
		  st.write("Treatment and medications: ")
		  text_content += "\nTreatment and medications: "
		  for k in res[3].keys():
		    st.write("[" , count , "]" , k)
		    text_content += "\n[" + str(count) + "]" + k
		    count += 1
		else :
		  st.write("No tests performed on patient on {}".format(date))
		  text_content += "No tests performed on patient on {}".format(date)

		st.download_button('Download as Text' , text_content )
