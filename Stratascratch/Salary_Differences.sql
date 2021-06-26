-- Official Solution
SELECT
    (SELECT max(salary)
    FROM db_employee emp
    INNER JOIN db_dept dept ON emp.department_id = dept.id
    WHERE department = 'marketing') -
    (SELECT max(salary)
    FROM db_employee emp
    INNER JOIN db_dept dept ON emp.department_id = dept.id
    WHERE department = 'engineering') AS salary_difference
