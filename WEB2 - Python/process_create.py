#!python

import cgi

form = cgi.FieldStorage()
title = form.getvalue("title")
description = form.getvalue("description")

opened_file = open('data/'+title, 'w')
opened_file.write(description)
opened_file.close()

#Redirection
print("Location: index.py?id="+title)
print()

#데이터를 어떻게 받아서 어떻게 저장하는지에 대해서 살펴보았다.