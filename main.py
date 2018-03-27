from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = '''
<!DOCTYPE html> 
<html> 
	<head> 
		<style> 
			form {
				background-color: #eee;
				padding: 20px;
				margin: 0 auto;
				width: 540px;
				font: 16 px sans-serif;
				border-radius: 10px;
			}

			textarea{
				margin: 10px 0;
				width: 540px;
				height: 120px
			}
			
			</style>
		</head>
		<body>
			<form action="/add" method="post">
        		<label for="rot">Rotate by:</label>
            	<input type="text" name="rot" value="0"/>
				<textarea name = "text">  </textarea>
        		<input type="submit" value="Submit query"/>
			</form>
			
			
		</body>
	</html>'''
@app.route("/add", methods = ['POST'])
def encrypt():
	text = str(request.form['text'])
	rot = int(request.form['rot'])
	encrypted_text = rotate_string(text, rot)
	content = "<h1>" + encrypted_text + "</h1>"
	return content

@app.route("/")
def index():
    return form

app.run()