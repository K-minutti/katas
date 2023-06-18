from datetime import datetime, date

class Employee:
    company = "Class Var, Inc."

    def __init__(self, name: str, birth_date: str):
        self.name: str = name
        self.birth_date: str = birth_date

    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value: str):
        self._birth_date = datetime.fromisoformat(value)


if __name__ == "__main__":
    e = Employee("Happy", str(date.today()))
    print(e.birth_date)