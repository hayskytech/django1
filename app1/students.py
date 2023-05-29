from django.shortcuts import render
import sqlite3
def main(request):

	con = sqlite3.connect("db.sqlite3")
	cursor = con.cursor()
	res = cursor.execute("SELECT name FROM sqlite_master")
	tables = res.fetchall()
	if ("students",) not in tables:
		cursor.execute("CREATE TABLE students (student, class, phone)")
		con.commit()

	student = request.GET.get('student')
	classname = request.GET.get('class')
	phone = request.GET.get('phone')
	
	if student:
		data = (student,classname,phone)
		cursor.execute("INSERT INTO students VALUES (?,?,?)" , data)
		con.commit()

	return render(request, "students.html")
	pass