import re

from backend.src.parser_generic import MedicalDocParser


class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            "patient_name": self.get_field("patient_name"),
            "patient_address": self.get_field("patient_address"),
            "medicines": self.get_field("medicines"),
            "directions": self.get_field("directions"),
            "refills": self.get_field("refills")
        }

    def get_field(self, fieldName):
        pattern_dict = {
            "patient_name": {"pattern": "Name:(.*)Date", "flags": 0},
            "patient_address": {"pattern": "Address:(.*)\n", "flags": 0},
            "medicines": {"pattern": "Address[^\n]*(.*)Directions", "flags": re.DOTALL},
            "directions": {"pattern": "Directions:(.*)Refill", "flags": re.DOTALL},
            "refills": {"pattern": "Refill:(.*)times", "flags": 0},
        }

        pattern_object = pattern_dict.get(fieldName)
        if pattern_object:
            matches = re.findall(
                pattern_object["pattern"], self.text, flags=pattern_object["flags"])
            if len(matches) > 0:
                return matches[0].strip()


if __name__ == "__main__":
    document_text = '''Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Maria Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

Prednisone 20 md
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mig every 3 days,
Finish in 2.5 weeks ,
Ltalda - take 2 pill everyday for 1 month

Refill: 2. times'''

    pp = PrescriptionParser(document_text)
    print(pp.parse())
