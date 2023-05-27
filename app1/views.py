from django.shortcuts import render

from django.http import HttpResponse
import sqlite3

def home(request):
	con = sqlite3.connect("db.sqlite3")
	cur = con.cursor()
	res = cur.execute("SELECT name FROM sqlite_master")
	tables = res.fetchall()
	if ('book',) not in tables:
		cur.execute("CREATE TABLE book(title, year, price)")
	
	title = request.GET.get('title')
	year = request.GET.get('year')
	price = request.GET.get('price')

	data = [
		( title , year, price ),
	]
	cur.executemany("INSERT INTO book VALUES(?, ?, ?)", data)
	
	con.commit()
	
	return render(request,"home.html")

def about(request):
	# return HttpResponse("<h1>About us<h1>")
	return render(request, "about.html")