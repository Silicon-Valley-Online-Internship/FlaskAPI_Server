import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def render_file():
    return render_template('upload.html')

# Create = POST
# Read = GET
# Update = PUT
# Delete = DELETE

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        File = request.files['file']
        File.save(secure_filename(File.filename))
        #저장할 경로 및 파일명 입력(root dir 하위 upload directory)

        return 'File upload complete! (%s)' % secure_filename(File.filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)