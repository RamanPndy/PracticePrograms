from systemdesign.google_sheet.impl import ConcreteSheet, Formula
'''
Design Patterns Used
Observer Pattern: To notify dependent cells when a referenced cell changes.
Strategy Pattern: For different evaluation strategies in the Formula class.
Composite Pattern: To manage cells and sheets as a composite structure.
'''

if __name__ == "__main__":
    sheet = ConcreteSheet(10, 10)

    sheet.set_cell(0, 0, 10)  # A1 = 10
    sheet.set_cell(1, 1, 20)  # B2 = 20

    formula = Formula("A1+B2", sheet)
    sheet.set_formula(2, 2, formula)  # C3 = A1 + B2

    sheet.evaluate()

    print(sheet.get_cell(2, 2).get_value())  # Should print 30
