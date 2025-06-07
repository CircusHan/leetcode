import unittest
from medical_records import patient_data_store, record_payment, generate_prescription, generate_medical_certificate, Patient

class TestMedicalRecords(unittest.TestCase):

    def setUp(self):
        # Clear the data store before each test
        patient_data_store.clear()
        # You might also want to add some default patient data for testing
        # For example, a patient who has paid and one who hasn't
        self.paid_patient_id = "patient123"
        self.unpaid_patient_id = "patient456"
        self.unknown_patient_id = "patient789"

        # Add a patient who will have their payment recorded
        # We need to set a name for this patient for consistent testing
        patient_paid = Patient(patient_id=self.paid_patient_id, name="Paid Pat")
        patient_data_store[self.paid_patient_id] = patient_paid
        record_payment(self.paid_patient_id) # This will mark them as paid

        # Add a patient who exists but hasn't paid (for testing generation logic)
        # We need to manually add them here as record_payment marks them paid
        new_patient = Patient(patient_id=self.unpaid_patient_id, name="Unpaid Pat")
        patient_data_store[self.unpaid_patient_id] = new_patient


    def test_record_payment_new_patient(self):
        test_patient_id = "new_patient_rp"
        self.assertTrue(record_payment(test_patient_id))
        self.assertIn(test_patient_id, patient_data_store)
        self.assertEqual(patient_data_store[test_patient_id].payment_status, "paid")
        self.assertEqual(patient_data_store[test_patient_id].name, "Unknown") # Default name

    def test_record_payment_existing_patient(self):
        # First ensure unpaid_patient is actually pending
        self.assertEqual(patient_data_store[self.unpaid_patient_id].payment_status, "pending")
        self.assertTrue(record_payment(self.unpaid_patient_id))
        self.assertEqual(patient_data_store[self.unpaid_patient_id].payment_status, "paid")

    def test_generate_prescription_payment_complete(self):
        patient = patient_data_store[self.paid_patient_id]
        patient.set_prescription_details("Take two pills daily.")
        prescription = generate_prescription(self.paid_patient_id)
        self.assertIn(f"Prescription for patient {self.paid_patient_id} ({patient.name})", prescription)
        self.assertIn("Take two pills daily.", prescription)

    def test_generate_prescription_payment_pending(self):
        prescription = generate_prescription(self.unpaid_patient_id)
        self.assertIn("Prescription cannot be generated", prescription)
        self.assertIn(self.unpaid_patient_id, prescription)

    def test_generate_prescription_unknown_patient(self):
        prescription = generate_prescription(self.unknown_patient_id)
        self.assertIn("Prescription cannot be generated", prescription)
        self.assertIn(self.unknown_patient_id, prescription)

    def test_generate_medical_certificate_payment_complete(self):
        patient = patient_data_store[self.paid_patient_id]
        patient.set_certificate_details("Fit for work.")
        certificate = generate_medical_certificate(self.paid_patient_id)
        self.assertIn(f"Medical Certificate for patient {self.paid_patient_id} ({patient.name})", certificate)
        self.assertIn("Fit for work.", certificate)

    def test_generate_medical_certificate_payment_pending(self):
        certificate = generate_medical_certificate(self.unpaid_patient_id)
        self.assertIn("Medical certificate cannot be generated", certificate)
        self.assertIn(self.unpaid_patient_id, certificate)

    def test_generate_medical_certificate_unknown_patient(self):
        certificate = generate_medical_certificate(self.unknown_patient_id)
        self.assertIn("Medical certificate cannot be generated", certificate)
        self.assertIn(self.unknown_patient_id, certificate)

if __name__ == '__main__':
    unittest.main()
