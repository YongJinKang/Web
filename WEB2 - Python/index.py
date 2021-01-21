#!python

print("content-type: text/html; charset=euc-kr\n")

import cgi, os, view



form = cgi.FieldStorage()

if 'id' in form:
    pageId = form.getvalue("id")
    description = open('data/'+pageId,'r').read()
    description = description.replace('<','&lt;')
    description = description.replace('>','&gt;')
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action = "process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type = "submit" value="delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = "Hello, This is introduction of Show me the rapper season 9 Final rappers"
    update_link = ''
    delete_action= ''
    
print('''<!DOCTYPE html>

<html>
    <head>
        <title>WEB1 - the rappers of Show me the money season.9 the Final</title>
        <meta charset="euc-kr">
    </head>

    <body>
        <h1><a href="index.py">Show me the Money 9 Final Rapper</a></h1>
        <ol>
            {listStr}
        </ol>
        <a href = "create.py">create</a>
        {update_link}
        {delete_action}
        <h2>{title}</h2>
        <p>{desc}</p>
    </body>
</html>
'''.format(title=pageId, 
           desc=description, 
           listStr=view.getList(), 
           update_link = update_link, 
           delete_action=delete_action))

##물음표 뒷쪽은 쿼리스트링, URL 파라미터라고 불림
###:웹서버에게 어떠한 질의를 할 때 사용하는 문자
###우린 ID값이 HTML인 웹페이지를 질의합니다라는 뜻-->이런걸 query string

###어떻게 CGI를 이용해서 쿼리스트링을 파이썬 방식으로 알아낼 수 있는가 ?

###CGI 

##사용자들이 직접 데이터 입력

##데이터 입력받는 양식을 form이라고 한다.
