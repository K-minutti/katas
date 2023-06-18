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

    def compute_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        birthday = datetime(
            today.year,
            self.birth_date.month,
            self.birth_date.day
        )
        if today < birthday:
            age -= 1
        return age

    @classmethod
    def from_dict(cls, data_dict: dict):
        return cls(**data_dict)

    def __str__(self):
        return f"{self.name} is {self.compute_age()} years old"

    def __repr__(self):
        return (
            f"{type(self).__name__}("
            f"name='{self.name}', "
            f"birth_date='{self.birth_date.strftime('%Y-%m-%d')}'"
        )


if __name__ == "__main__":
    e = Employee("Happy", '2000-06-18')
    print(e.birth_date)
    print(e.compute_age())
    print(e)
    data = {"name": "Demboys", "birth_date": "2015-12-15"}
    d = Employee.from_dict(data)
    print(d)

