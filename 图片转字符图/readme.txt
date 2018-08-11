41.delete  from score where student_id = 2 and course_id = 1 ;
40.select student_id from score where course_id = 4  and num <60  ;


39.select t1.student_id,t1.avg_num from (select student_id, avg(num) as avg_num  from score  group by student_id) as t1  
    inner join  
 (select student_id ,count(student_id) as new_num   from score where num < 60  group by student_id having new_num  =2 or new_num>2 ) as t2
on t1.student_id = t2.student_id;
	
38,查询没学过“李平”老师讲授的任一门课程的学生姓名；

  
  
select sname from student where sid in (
  select  student from (select * from ( select course_id,   group_concat(student_id) as student from score group by course_id) as t1 
    inner join 
	(select course.cname, course.cid,teacher.tname as name from course  left join teacher on teacher_id = tid) as
	t2  on t2.cid = t1.course_id) as t3 where t3.name  != '李平老师');

37,查询全部学生都选修的课程的课程号和课程名；

 select * from (select * from ( select course_id,   group_concat(student_id separator ',') as student from score group by course_id) as t1 
    inner join 
	(select course.cname, course.cid,teacher.tname as name from course  left join teacher on teacher_id = tid) as
	t2  on t2.cid = t1.course_id) as t4 ; 
36,检索至少选修两门课程的学生学号；
    select  student_id,  count(course_id) as num   from score group by student_id  having num>2 or num = 2;
35、查询每门课程成绩最好的前两名；
