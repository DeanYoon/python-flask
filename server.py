from flask import Flask
import random
app  = Flask(__name__)



topics = [
    {'id':1, 'title':'html', 'body':'html is ...'},
    {'id':2, 'title':'css', 'body':'css is ...'},
    {'id':3, 'title':'JS', 'body':'JS is ...'},
]

def template(contents, content):
    return f'''
    <!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}

        </body>
    </html>
    '''

def getContents():

    liTags = ''
    for topic in topics:
        liTags = liTags + f"<li><a href='/read/{topic['id']}'> {topic['title']} </a></li>"
    return liTags


@app.route('/')
def index():



    return template(getContents(),'<h2>Welcome</h2>Hello , Web')

@app.route('/hello')
def hello():
    return 'Hello world'

@app.route('/read/<int:id>')
def read(id):
   
    title = ''
    body = ''
    for topic in topics:
        if id== topic['id']:
            title = topic['title']
            body = topic['body']


    print(title,body)

    return template(getContents(), f'<h2>{title}</h2>{body}')

app.run(debug=True)