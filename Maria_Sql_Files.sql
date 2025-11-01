CREATE TABLE IF NOT EXISTS Mariaemployees (
    employee_id INTEGER,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    salary INTEGER,
    hire_date VARCHAR(255),
    department VARCHAR(255)
);

INSERT INTO Mariaemployees (employee_id, first_name, last_name, salary, hire_date, department) VALUES (1, 'John', 'Doe', 50000, '2024-01-15', 'IT');
INSERT INTO Mariaemployees (employee_id, first_name, last_name, salary, hire_date, department) VALUES (2, 'Jane', 'Smith', 60000, '2024-02-01', 'HR');
INSERT INTO Mariaemployees (employee_id, first_name, last_name, salary, hire_date, department) VALUES (3, 'Bob', 'Johnson', 55000, '2024-03-10', 'IT');
INSERT INTO Mariaemployees (employee_id, first_name, last_name, salary, hire_date, department) VALUES (4, 'Alice', 'Williams', 65000, '2024-01-20', 'Finance');
INSERT INTO Mariaemployees (employee_id, first_name, last_name, salary, hire_date, department) VALUES (5, 'Charlie', 'Brown', 52000, '2024-02-15', 'Marketing');
