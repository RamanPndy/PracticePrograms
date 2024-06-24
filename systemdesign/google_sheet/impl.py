from systemdesign.google_sheet.interface import Cell, Sheet


class ConcreteCell(Cell):
    def __init__(self):
        self.value = None
        self.formula = None
        self.dependents = []
        self.dependencies = []

    def get_value(self):
        if self.formula:
            return self.formula.evaluate()
        return self.value

    def set_value(self, value):
        self.value = value
        self.formula = None
        self.notify_dependents()

    def set_formula(self, formula):
        self.formula = formula
        self.notify_dependents()

    def add_dependency(self, cell):
        self.dependencies.append(cell)

    def remove_dependency(self, cell):
        self.dependencies.remove(cell)

    def notify_dependents(self):
        for dependent in self.dependents:
            dependent.update()

    def update(self):
        self.notify_dependents()

class ConcreteSheet(Sheet):
    def __init__(self, rows, cols):
        self.grid = [[ConcreteCell() for _ in range(cols)] for _ in range(rows)]

    def get_cell(self, row, col):
        return self.grid[row][col]

    def set_cell(self, row, col, value):
        cell = self.get_cell(row, col)
        cell.set_value(value)

    def set_formula(self, row, col, formula):
        cell = self.get_cell(row, col)
        cell.set_formula(formula)

    def evaluate(self):
        for row in self.grid:
            for cell in row:
                cell.get_value()  # Trigger evaluation

    def create_context(self):
        context = {}
        for row_idx, row in enumerate(self.grid):
            for col_idx, cell in enumerate(row):
                context[f'{chr(65+col_idx)}{row_idx+1}'] = cell.get_value()
        return context


class Formula:
    def __init__(self, expression, sheet):
        self.expression = expression
        self.sheet = sheet

    def evaluate(self):
        # Example: Parse the expression and evaluate it
        # This is a simplified example and can be extended to handle complex expressions
        # Assuming expression is something like "=A1+B2"
        result = eval(self.expression, {}, self.sheet.create_context())
        return result
