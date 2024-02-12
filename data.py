import csv
import random

# Function to generate data for the CSV file
def generate_doctor_data(num_doctors=1000):
    doctor_data = []
    
    for doctor_id in range(1000, 1000 + num_doctors):
        doctor_age = random.randint(30, 70)
        daily_average = round(random.uniform(5,15),2)
        row = [doctor_id, doctor_age, daily_average]
        doctor_data.append(row)
    
    return doctor_data

def generate_patient_data(doctor_id, daily_average, num_patients=5):
    patient_data = []
    
    for patient_id in range((doctor_id - 1000) * num_patients + 1, (doctor_id - 1000) * num_patients + 1 + num_patients):
        patient_age = random.randint(18, 90)
        patient_disease_id = random.randint(1, 100)
        prev_visited = random.choice([1,0])
        average_time_p = round(random.uniform(5,15),2)  # Added average_time_p

        time=((daily_average+average_time_p)/2)+prev_visited*2+random.randint(-5,5)
        time+= 2 if patient_disease_id>50 else 0

        time=round(time)
        
        row = [patient_id, patient_age,patient_disease_id,average_time_p,doctor_id,doctor_age,prev_visited,daily_average,time]
        patient_data.append(row)
    
    return patient_data

# Function to write data to a CSV file
def write_to_csv(filename, header, data):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write header
        csv_writer.writerow(header)
        
        # Write data
        csv_writer.writerows(data)

# Define CSV file parameters
csv_filename = 'data.csv'
csv_header = ['patient_id', 'patient_age', 'patient_disease_id', 'average_time_p', 'doctor_id', 'doctor_age', 'prev_visited','daily_average','time']

# Generate doctor data
doctor_data = generate_doctor_data()

# Generate patient data for each doctor
all_data = []
for doctor_info in doctor_data:
    doctor_id, doctor_age, _ = doctor_info  # Ignore daily_average for patients
    patients_data = generate_patient_data(doctor_id,_)
    all_data.extend(patients_data)  # Append patient data

# Write data to CSV file
write_to_csv(csv_filename, csv_header, all_data)

print(f"CSV file '{csv_filename}' has been generated successfully.")
