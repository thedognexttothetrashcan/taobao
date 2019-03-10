from flask import Flask,render_template
from flask_script import Manager
from flask_mail import Mail,Message
import time


app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_USERNAME'] = '69189668@qq.com'
# 授权码或者密码
app.config['MAIL_PASSWORD'] = 'xsaeccnuhttocaha'
mail = Mail(app) # 实例化邮件对象
manager = Manager(app)


@app.route('/send_mail/')
def send_mail():
    msg = Message(subject='邮件激活',recipients=['13383332752@163.com'],sender=app.config['MAIL_USERNAME'])
    msg.html = 'lallalla'
    mail.send(msg)
    return '发送邮件'

def haha():
    if __name__ == '__main__':
        app.run()
