#!python

import cgi, os

form = cgi.FieldStorage()
pageId = form.getvalue("pageId")
title = form.getvalue("title")
description = form.getvalue("description")

opened_file = open('data/'+pageId, 'w')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageId,'data/'+title)

# Redirection
print("Location: index.py?id="+title)
print()

#데이터를 어떻게 받아서 어떻게 저장하는지에 대해서 살펴보았다.