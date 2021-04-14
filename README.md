# faceRecognition

Code For Attendance Management using face recognition\
Technology used :\
-openCV (Opensource Computer Vision)\
-Python\
-tkinter GUI interface\
-mysql\

How to run the program :\
1.Run the train.py file\
2.enter the id and name\
3.then click on take image\
4.train the images\
5.click on track images to start recognizing the faces\ 
6.press q to stop \
7.when done click on quit to quit the program\ 

After quiting ur attendance will be stored in a csv file as well as in a mysql database called attendancedb and in a table called attendance.\

**p.s
you might have to create the db and table by urself if its create by itself
the following is the description of the table\ 

+---------------+--------------+------+-----+---------+-------+\
| Field         | Type         | Null | Key | Default | Extra |\
+---------------+--------------+------+-----+---------+-------+\
| Id            | varchar(255) | YES  |     | NULL    |       |\
| NAME          | varchar(255) | YES  |     | NULL    |       |\
| DATEOFARRIVAL | date         | YES  |     | NULL    |       |\
| TIME          | varchar(255) | YES  |     | NULL    |       |\
+---------------+--------------+------+-----+---------+-------+\

***you need to change the mysql username and password in train.py for the program to connect to database.*** 
