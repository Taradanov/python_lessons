class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def get_total_income_worker(self):
        if isinstance(self._income, dict):
            return self._income.get('wage') + self._income.get('bonus')
        return 0

class Position(Worker):

    def __init__(self, name: str, surname: str, position: str, income: dict):
        Worker.__init__(self,  name, surname, position, income)

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self.get_total_income_worker()


income = {"wage": 100_000, "bonus": 30_000}

position = Position('Nikolai', 'Taradanov', 'programmist 1c', income)
print(position.get_full_name())
print(position.get_total_income())