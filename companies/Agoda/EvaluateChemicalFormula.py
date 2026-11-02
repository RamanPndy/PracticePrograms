'''
Question — Evaluate a nested chemical formula
Problem: Parse a chemical formula and return the count of each element. Parentheses multiply the counts inside them.

Example:
Input: formula = "H2O"
Output: {"H": 2, "O": 1}

Input: formula = "Mg(OH)2"
Output: {"Mg": 1, "O": 2, "H": 2}

Input: formula = "K4(ON(SO3)2)2"
Output: {"K": 4, "O": 14, "N": 2, "S": 4}

Approach:
1. Use a stack to keep track of the current context of element counts.
2. Iterate through the formula character by character.
3. When encountering an element, add it to the current context with its count.
4. When encountering an opening parenthesis '(', push the current context onto the stack and start a new context.
5. When encountering a closing parenthesis ')', pop the previous context from the stack and multiply the counts 
inside the parentheses by the following number.
6. Merge the multiplied counts with the previous context.
7. Continue until the end of the formula.
8. Return the final counts of each element.

Why this works:
The algorithm works by maintaining a stack of contexts for element counts. 
Each time a parenthesis is opened, a new context is created, and when it is closed, the counts are multiplied and merged
with the previous context. 
This ensures that nested structures are correctly evaluated and the final counts reflect the entire formula.

Time Complexity: O(n), where n is the length of the formula.
Space Complexity: O(n), for the stack and the element count contexts.
'''
def evaluate_chemical_formula(formula):
    import collections
    stack = [collections.Counter()]
    i = 0
    while i < len(formula):
        if formula[i] == '(':
            stack.append(collections.Counter())
            i += 1
        elif formula[i] == ')':
            top = stack.pop()
            i += 1
            i_start = i
            while i < len(formula) and formula[i].isdigit(): # Continue parsing digits for the multiplier after closing parenthesis
                i += 1
            multiplier = int(formula[i_start:i] or 1)
            for elem, count in top.items():
                stack[-1][elem] += count * multiplier # Multiply the count by the multiplier and add to the previous context
        else:
            # Parse the element name and its count
            i_start = i
            i += 1
            while i < len(formula) and formula[i].islower(): # Continue parsing lowercase letters for the element name
                i += 1
            elem = formula[i_start:i]
            i_start = i
            while i < len(formula) and formula[i].isdigit(): # Continue parsing digits for the element count
                i += 1
            count = int(formula[i_start:i] or 1)
            stack[-1][elem] += count # Add the count of the element to the current context
    return dict(stack[-1])
# Example usage:
formula = "H2O"
print(evaluate_chemical_formula(formula))  # Output: {"H": 2, "O": 1}

formula = "Mg(OH)2"
print(evaluate_chemical_formula(formula))  # Output: {"Mg": 1, "O": 2, "H": 2}

formula = "K4(ON(SO3)2)2"
print(evaluate_chemical_formula(formula))  # Output: {"K": 4, "O": 14, "N": 2, "S": 4}

'''
In production code, validate malformed formulas, unmatched parentheses, invalid symbols, and numeric overflow if using a fixed-width integer language.
'''
def validate_chemical_formula(formula):
    # Basic validation for chemical formula
    import re
    if not formula:
        raise ValueError("Formula cannot be empty")
    if not re.match(r'^[A-Za-z0-9()]+$', formula):
        raise ValueError("Formula contains invalid characters")
    stack = []
    for char in formula:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                raise ValueError("Unmatched closing parenthesis")
            stack.pop()
    if stack:
        raise ValueError("Unmatched opening parenthesis")
    # Additional validation for element names and counts
    import re
    pattern = r'([A-Z][a-z]*)(\d*)'
    i = 0
    while i < len(formula):
        if formula[i].isalpha():
            match = re.match(pattern, formula[i:])
            if not match:
                raise ValueError(f"Invalid element at position {i}")
            i += len(match.group(0))
        elif formula[i].isdigit():
            raise ValueError(f"Unexpected digit at position {i}")
        else:
            i += 1
    return True  # If no exceptions were raised, the formula is considered valid

'''
Given 3 atoms with weights (C -> 12, H -> 1, O -> 8), you're given a chemical formula. Need to compute the total weight.
e.g CH4 = 16, H(CH4)2 = 33

Approach:
1. Use the previously defined `evaluate_chemical_formula` function to get the count of each element.
2. Multiply the count of each element by its corresponding weight.
3. Sum up the contributions of all elements to get the total weight.
'''
def compute_chemical_weight(formula):
    weights = {"C": 12, "H": 1, "O": 8}
    element_counts = evaluate_chemical_formula(formula)
    total_weight = 0
    for elem, count in element_counts.items():
        if elem not in weights:
            raise ValueError(f"Unknown element: {elem}")
        total_weight += weights[elem] * count
    return total_weight

# Example usage:
print(compute_chemical_weight("CH4"))        # Output: 16
print(compute_chemical_weight("H(CH4)2"))    # Output: 33

'''
Can it be solved without a stack using recursion?
Approach:
1. Define a recursive function that processes the formula from left to right.
2. When encountering an element, add its count to the current context.
3. When encountering '(', recursively process the sub-formula until the matching ')'.
4. When encountering ')', return the accumulated counts to the previous context.
5. Multiply the counts inside parentheses by the following number if present.
6. Continue until the entire formula is processed.
'''
def evaluate_chemical_formula_recursive(formula):
    import re
    pattern = r'([A-Z][a-z]*)(\d*)'

    def helper(index):
        element_counts = {}
        while index < len(formula):
            if formula[index] == '(':
                sub_counts, index = helper(index + 1)
                multiplier = 1
                if index < len(formula) and formula[index].isdigit(): # Check if there's a multiplier after the closing parenthesis
                    start = index
                    while index < len(formula) and formula[index].isdigit(): # Continue until the end of the number
                        index += 1
                    multiplier = int(formula[start:index])
                for elem, count in sub_counts.items():
                    element_counts[elem] = element_counts.get(elem, 0) + count * multiplier
            elif formula[index] == ')':
                return element_counts, index + 1
            else:
                match = re.match(pattern, formula[index:])
                if not match:
                    raise ValueError(f"Invalid element at position {index}")
                elem = match.group(1)
                count = int(match.group(2)) if match.group(2) else 1
                element_counts[elem] = element_counts.get(elem, 0) + count
                index += len(match.group(0))
        return element_counts, index

    counts, _ = helper(0)
    return counts

'''
What if an atom has a multi-digit multiplier, such as C12H22O11?
The current implementation already handles multi-digit multipliers correctly. 
The regular expression pattern r'([A-Z][a-z]*)(\d*)' captures the element symbol and its following number, 
regardless of the number of digits. 
The code then converts this number to an integer, ensuring that multi-digit multipliers are processed accurately.
'''