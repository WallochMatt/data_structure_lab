class FamilyMember:
    def __init__(self, first_name, last_name, relation):
        self.first_name = first_name
        self.last_name = last_name
        self.relation = relation

    def introduce_family(self):
         print(f"{self.first_name} is my {self.relation}")
