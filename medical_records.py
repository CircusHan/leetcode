# This file will contain classes and functions for managing medical records.

patient_data_store = {}

class Patient:
    def __init__(self, patient_id: str, name: str = "Unknown"):
        self.patient_id = patient_id
        self.name = name
        self.payment_status = "pending"  # Default status
        self.prescription_details = ""
        self.certificate_details = ""

    def mark_payment_complete(self):
        self.payment_status = "paid"

    def set_prescription_details(self, details: str):
        self.prescription_details = details

    def set_certificate_details(self, details: str):
        self.certificate_details = details

def record_payment(patient_id: str) -> bool:
  """Records a payment for a given patient_id.

  If the patient_id does not exist, a new Patient object is created.
  If the patient_id exists, the Patient object's payment_status is updated.

  Args:
    patient_id: The ID of the patient.

  Returns:
    True if the payment was successfully recorded or updated.
  """
  if patient_id not in patient_data_store:
    patient = Patient(patient_id=patient_id)
    patient.mark_payment_complete()
    patient_data_store[patient_id] = patient
  else:
    patient = patient_data_store[patient_id]
    patient.mark_payment_complete()
  return True

def generate_prescription(patient_id: str) -> str:
  """Generates a prescription for a given patient_id.

  Args:
    patient_id: The ID of the patient.

  Returns:
    A string containing the prescription or an error message.
  """
  patient = patient_data_store.get(patient_id)
  if not patient or patient.payment_status != "paid":
    return f"Prescription cannot be generated: Payment not completed or patient not found for patient ID {patient_id}"
  return f"Prescription for patient {patient.patient_id} ({patient.name}): {patient.prescription_details if patient.prescription_details else '[Details placeholder]'}"

def generate_medical_certificate(patient_id: str) -> str:
  """Generates a medical certificate for a given patient_id.

  Args:
    patient_id: The ID of the patient.

  Returns:
    A string containing the medical certificate or an error message.
  """
  patient = patient_data_store.get(patient_id)
  if not patient or patient.payment_status != "paid":
    return f"Medical certificate cannot be generated: Payment not completed or patient not found for patient ID {patient_id}"
  return f"Medical Certificate for patient {patient.patient_id} ({patient.name}): {patient.certificate_details if patient.certificate_details else '[Details placeholder]'}"
