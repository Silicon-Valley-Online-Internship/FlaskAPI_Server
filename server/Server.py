import os
from subprocess import call
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/upload')
def renderFile():
    return render_template('upload.html')

# Create = POST
# Read = GET
# Update = PUT
# Delete = DELETE

# 단순 파일 업로드용 api
@app.route('/store')
def Renderfile():
    return render_template('store.html')

@app.route('/simpleUpload', methods = ['GET', 'POST'])
def simpleUploadfile():
    if request.method == 'POST':
        f = request.files['file']
        #단순히 파일 저장에 필요한 기능을 하는 API
        f.save(secure_filename(f.filename))

        return 'The file has been stored!'
#여기서 받아들여진 파일을 매개로 바로 알고리즘을 돌린다면?

@app.route('/fileUpload', methods = ['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':
        File = request.files['file']
        # 저장할 경로 및 파일명 입력(root dir 하위 upload directory)
        File.save(secure_filename(File.filename))

        #해당 if문 내부에서 subshell 실행해서 foodetector를 실행시킴
        call('python3 foodetector.py %s' % secure_filename(File.filename), shell=True)

        return 'The Class of filaname = (%s) is determined! ' % secure_filename(File.filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)