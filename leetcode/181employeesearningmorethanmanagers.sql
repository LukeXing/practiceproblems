SELECT Name AS Employee
FROM (
SELECT  emp1.id, 
        emp1.name AS Name, 
        emp1.salary, 
        emp2.id, 
        emp2.salary 
FROM Employee emp1 
JOIN Employee emp2
ON emp1.managerId = emp2.id
WHERE emp1.salary > emp2.salary)
;
