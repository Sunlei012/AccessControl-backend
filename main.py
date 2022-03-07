import json
import os

from compreface import CompreFace
from compreface.collections import FaceCollection, Subjects
from compreface.service import RecognitionService
from flask import Flask, request
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'upload/'

DOMAIN: str = 'http://localhost'
PORT: str = '8000'
API_KEY: str = '89814d5c-8e1f-4409-a026-6a3ea6ffd11d'

compre_face: CompreFace = CompreFace(DOMAIN, PORT)

recognition: RecognitionService = compre_face.init_face_recognition(API_KEY)

face_collection: FaceCollection = recognition.get_face_collection()

subjects: Subjects = recognition.get_subjects()

def recognition(image_path,subject):
    face_collection.add(image_path=image_path, subject=subject)

@app.route('/api/face',methods=['POST'])
def hello_world1():  # put application's code here
    print(face_collection)
    f = request.files['img']
    print(request.files)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    recognition("upload/123.png",request.form['pwid']+"-"+request.form['name'])
    return request.form['pwid']



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"




@app.route('/api/login/account', methods=['POST'])
def login():
    aa=request.get_data();
    username = request.values.get("username");
    bb=json.loads(aa.decode("utf-8")).get("username")
    return {
        "status": "ok",
        "type": "POST",
        "currentAuthority": "admin"
    }

@app.route('/api/currentUser')
def user_info():
    return {
        "success": "true",
        "data": {
            "name": 'Serati Ma',
            "avatar": 'https://gw.alipayobjects.com/zos/antfincdn/XAosXuNZyF/BiazfanxmamNRoxxVxka.png',
            "userid": '00000001',
            "email": 'antdesign@alipay.com',
            "signature": '海纳百川，有容乃大',
            "title": '交互专家',
            "group": '蚂蚁金服－某某某事业群－某某平台部－某某技术部－UED',
            "tags": [
                {
                    "key": '0',
                    "label": '很有想法的',
                },
            ],
            "notifyCount": 12,
            "unreadCount": 11,
            "country": 'China',
            "access": "admin",
            "geographic": {
                "province": {
                    "label": '浙江省',
                    "key": '330000',
                },
                "city": {
                    "label": '杭州市',
                    "key": '330100',
                },
            },
            "address": '西湖区工专路 77 号',
            "phone": '0752-268888888',
        }
    }
@app.route('/api/intruder')
def intruder():
    return {
        "data":{
            "list":[
                {
                    "age":233,
                    "img":"https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fupload-images.jianshu.io%2Fupload_images%2F13055508-7b2246905fb4f095.png&refer=http%3A%2F%2Fupload-images.jianshu.io&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1648734001&t=f94399ac3d5d9c9eb711259858c80a38"
                },
                {
                    "age": 233,
                    "img": "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fupload-images.jianshu.io%2Fupload_images%2F13055508-7b2246905fb4f095.png&refer=http%3A%2F%2Fupload-images.jianshu.io&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1648734001&t=f94399ac3d5d9c9eb711259858c80a38"
                }
            ]
        }
    }
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
