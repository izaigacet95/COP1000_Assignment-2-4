# Variables

# Added new salary and dependents
salary = 60000.0
num_dependents = 3

# Calculate state withholding tax (6.5%)
state_tax = salary * 0.065

# Calculate federal withholding tax (28.0%)
federal_tax = salary * 0.28

# Calculate dependent deductions (2.5% of salary for each dependent)
dependent_deduction = salary * 0.025 * num_dependents

# Calculate total withholding
total_withholding = state_tax + federal_tax + dependent_deduction

# Calculate take-home pay
take_home_pay = salary - total_withholding

# Output statements
print(f"State Tax: ${state_tax}")
print(f"Federal Tax: ${federal_tax}")
print(f"Dependents: ${dependent_deduction}")
print(f"Salary: ${salary}")
print(f"Take-Home Pay: ${take_home_pay}")
