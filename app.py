import os
from flask import Flask, request
from main import *
UPLOAD_FOLDER = './'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file1.save(path)
        return '''
         <h1>click to start press q to quit</h1>
        <a href="/fr">
        <input type="submit"/>
        </a>
        '''

        return 'ok'

    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''

@app.route('/fr', methods=['GET', 'POST'])
def fr():
    find_face()
    return '''
    <h1>back to home</h1>
     <a href="/">
        <input type="submit"/>
        </a>
    '''

if __name__ == '__main__':
    app.run()