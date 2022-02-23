# Scheduling Errors
## Tags: !join, !filter

## Data Model:
```
PROFESSOR
Name                Type            Description
ID                  Integer         A professor's ID in the inclusive range [1, 1000]. This is a primary key.
NAME                String          A professor's name. This field contains between 1 and 100 characters (inclusive).
DEPARTMENT_ID       Integer         A professor's department ID. This is a foreign key to DEPARTMENT.ID.
SALARY              Integer         A professor's salary in the inclusive range [5000, 40000].


DEPARTMENT
Name                Type            Description
ID                  Integer       A department ID in the inclusive range [1, 1000]. This is a primary key.
NAME                String          A department name. This field contains between 1 and 100 characters (inclusive).

COURSE
Name                Type            Description
ID                  Integer         A course ID in the inclusive range [1, 1000]. This is a primary key.
NAME                String          A course name. This field contains between 1 and 100 characters (inclusive).
DEPARTMENT_ID       Integer         A course's department ID. This is a foreign key to DEPARTMENT.ID.
CREDITS             Integer         The number of credits allocated to the course in the inclusive range [1, 10].

SCHEDULE
Name                Type            Description
PROFESSOR_ID        Integer         The ID of the professor teaching the course. This is a foreign key to PROFESSOR.ID.
COURSE_ID           Integer        The course's ID number. This is a foreign key to COURSE.ID.
SEMESTER            Integer         A semester ID in the inclusive range [1, 6].
YEAR                Integer         A calendar year in the inclusive range [2000, 2017].
```

## Solution
```
select distinct (
    p.name as professor_name
    ,c.name as course_name
)
from SCHEDULE as s 
join DEPARTMENT as d
    on d.id = s.course_id
join PROFESSOR as p
    on p.id = s.professor_id
where p.department_id <> s.course_id
```

# Largest Number of Orders