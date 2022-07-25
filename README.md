## Getting Started:

This project was implemented for the course AI1 (YS02), during the winter semester 2021-2022, CS NKUA. 

The goal of this project is to define an exam timetabling problem as a CSP problem in timetable.py. Then use the already implemented algorithms from csp.py to analyze the results and come to a conclusion about the best performing algorithm. 

Also in the csp.py file is implemented the Dom/Wdeg heuristic according to this paper: http://www.frontiersinai.com/ecai/ecai2004/ecai04/pdf/p0146.pdf paragraph 3.3. 

### Some useful information about the implementetion of the project:

- The duration of the examination of each course is 3 hours.
- The duration of the examination period of all courses is 21 days(Weekends are excluded).
- There are 3 slots for each examination day.
- Only one course per slot per day.
- If a course has a lab examination, the lab examination can be scheduled right after the main course examination and only on the   same day.
- Some courses are more difficult than other, so difficult courses must be at least 2 days apart. For example one can be examined   on Monday and the next on Wednesday.
- Courses of the same Proffesor must be examined in different days.
- Courses of the same semester must be examined in different days.
- All information about different courses can be extracted from the .csv file.

#### More about the project:
[hw3.pdf](https://github.com/panagiotiskon/AI-Project3/files/9176446/hw3.pdf)
