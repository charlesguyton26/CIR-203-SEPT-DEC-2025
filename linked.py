LinkedDict = {
    'Name': ['Stal', 'Bilo', 'Charles', 'Guyton', 'Sil', 'Tya'],
    'AdmNo': ['CIS 214', 'CIS 252', 'CIT 107', 'CIT 756', 'CIS 925', 'CIS 394'],
    'Grades': {
        'CIR 203': [80, 90, 70, 89, 60, 70],
        'CIR 205': [50, 60, 70, 80, 90, 56],
        'CIT 211': [100, 90, 80, 70, 60, 50]
    },
    'Next': None
}
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert new student at the end
    def insert(self, name, adm_no, cir203, cir205, cit211):
        new_node = {
            "name": name,
            "adm_no": adm_no,
            "grades": {
                "CIR 203": cir203,
                "CIR 205": cir205,
                "CIT 211": cit211
            },
            "next": None
        }

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse to end
        current = self.head
        while current["next"] is not None:
            current = current["next"]

        current["next"] = new_node

    # Display all students
    def display(self):
        current = self.head
        while current is not None:
            print("Name:", current["name"])
            print("Admission No:", current["adm_no"])
            print("Grades:", current["grades"])
            print("-" * 30)
            current = current["next"]

# Create list
students = LinkedList()

students.insert("John Doe", "ADM123", 78, 82, 90)
students.insert("Mary Wanjiku", "ADM456", 85, 88, 92)
students.insert("Brian Otieno", "ADM789", 65, 70, 73)

# Display all nodes
students.display()
