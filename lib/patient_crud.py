from lib import db_models
from lib.crud import Table

class Patient(Table):
    def __init__(self):
        super().__init__(db_models.Patient)