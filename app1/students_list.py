from django.shortcuts import render
import sqlite3

def main(request):

	con = sqlite3.connect("db.sqlite3")
	cursor = con.cursor()

	students = cursor.execute("SELECT * FROM students").fetchall()
	print(students[0][0])
	data = {
		"students" : students
	}
	
	return render(request, "students_list.html", data)