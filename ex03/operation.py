class Operation:
    def __init__(self, cents: int, operation_type: str,description: str):
        self.cents = cents
        self.operation_type = operation_type
        self.description = description

    try:
        if (cents > 0):
            operation_type = 'credit'
        if (cents < 0):
            operation_type = 'debit'
    except ValueError:
        print("O valor deve ser diferente de zero")
