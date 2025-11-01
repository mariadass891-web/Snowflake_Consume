import pandas as pd
import numpy as np

def excel_to_sql(excel_path, sheet_name, table_name, output_file):
    # Read the Excel file
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    
    # Generate CREATE TABLE statement
    columns = []
    for col, dtype in df.dtypes.items():
        sql_type = 'VARCHAR(255)'  # default type
        if np.issubdtype(dtype, np.integer):
            sql_type = 'INTEGER'
        elif np.issubdtype(dtype, np.floating):
            sql_type = 'FLOAT'
        elif np.issubdtype(dtype, np.datetime64):
            sql_type = 'DATE'
        columns.append(f"{col} {sql_type}")
    
    create_table = f"CREATE TABLE IF NOT EXISTS {table_name} (\n    "
    create_table += ",\n    ".join(columns)
    create_table += "\n);\n\n"
    
    # Generate INSERT statements
    insert_statements = []
    for _, row in df.iterrows():
        values = []
        for val in row:
            if pd.isna(val):
                values.append('NULL')
            elif isinstance(val, (int, float)):
                values.append(str(val))
            else:
                values.append(f"'{str(val)}'")
        
        insert_stmt = f"INSERT INTO {table_name} ({', '.join(df.columns)}) "
        insert_stmt += f"VALUES ({', '.join(values)});"
        insert_statements.append(insert_stmt)
    
    # Write to SQL file
    with open(output_file, 'w') as f:
        f.write(create_table)
        f.write('\n'.join(insert_statements))
        f.write('\n')
    
    print(f"Successfully generated SQL in {output_file}")

if __name__ == "__main__":
    # Using our sample employee data
    excel_path = "sample_employees.xlsx"
    sheet_name = "Sheet1"
    table_name = "Mariaemployees"
    output_file = "Maria_Sql_Files.sql"
    
    excel_to_sql(excel_path, sheet_name, table_name, output_file)