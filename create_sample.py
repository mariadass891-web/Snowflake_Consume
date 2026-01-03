import pandas as pd

# Create sample employee data
data = {
    'employee_id': [1, 2, 3, 4, 5],
    'first_name': ['John', 'Jane', 'Bob', 'Alice', 'Charlie'],
    'last_name': ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown'],
    'salary': [50000.00, 60000.00, 55000.00, 65000.00, 52000.00],
    'hire_date': ['2024-01-15', '2024-02-01', '2024-03-10', '2024-01-20', '2024-02-15'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'Marketing']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
excel_path = 'sample_employees.xlsx'
df.to_excel(excel_path, index=False)
print(f"Sample Excel file created: {excel_path}")