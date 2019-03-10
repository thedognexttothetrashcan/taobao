# import argparse
# import os
# import re
#
# li = ['   ', '  6288', '   ', '   ', '   ', '  6288', '   ', '   ', '   ', '  6298', '   ', '   ', '   ', '  4898', '   ', '   ', '   ', '  5399', '   ', '   ', '   ', '  3068', '   ', '   ', '   ', '  3988', '   ', '   ', '   ', '  8688', '   ', '   ', '   ', '  5898', '   ', '   ', '   ', '  6299', '   ', '   ', '   ', '  6208', '   ', '   ', '   ', '  6888', '   ', '   ', '   ', '  6388', '   ', '   ', '   ', '  6188', '   ', '   ', '   ', '  6198', '   ', '   ', '   ', '  6588', '   ', '   ', '   ', '  9588', '   ', '   ', '   ', '  6299', '   ', '   ', '   ', '  11866', '   ', '   ', '   ', '  4288', '   ', '   ', '   ', '  3998', '   ', '   ', '   ', '  6288', '   ', '   ', '   ', '  6399', '   ', '   ', '   ', '  6288', '   ', '   ', '   ', '  6278', '   ', '   ', '   ', '  6298', '   ', '   ', '   ', '  6288', '   ', '   ', '   ', '  6288', '   ', '   ', '   ', '  5859', '   ', '   ', '   ', '  6288', '   ', '   ', '   ', '  6188', '   ', '   ', '   ', '  6568', '   ', '   ', '   ', '  6238', '   ', '   ', '   ', '  7638', '   ', '   ', '   ', '  6999', '   ', '   ', '   ', '  8988', '   ', '   ', '   ', '  6299', '   ', '   ', '   ', '  6288', '   ', '   ', '   ', '  11799', '   ', '   ', '   ', '  4978', '   ', '   ']
#
# li = [int(i.strip()) for i in li if not i.strip()=='']
#
# # for i in li:
# #     print(type(i), i)
#     # if i.isdigit():
#     #     print(i.strip())
#
# str = 'https://detail.tmall.com/item.htm?id=562099309982&skuId=3535167481896&pic=//img.alicdn.com/bao/uploaded/i3/TB1zK1TDOrpK1RjSZFhUNhSdXXa_043502.jpg_790x10000Q50s50.jpg_.webp&itemTitle=Apple/%E8%8B%B9%E6%9E%9C%20iPhone%20X&price=6288.00&from=h5'
# mode = re.compile(r'\d+')
# print(mode.search(str).group())

# def haha():
#     print('asda')

#
#
# a = 'ha'+'ha'
# b = a.strip("'")
# print(b + '()')
# parser = argparse.ArgumentParser()
# parser.add_argument('-tnum', type=int, default=1)
# parser.add_argument('-bid', type=int, default=0)
#
# args = parser.parse_args()
# _bid = args.bid
# _tnum = args.tnum
# print(_bid)
# print(_tnum)


# import queue
# q = queue.Queue()
# q.put('1')
# q.put('2')
# q.put('3')
# q.put('4')
# print(q.qsize())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(exit())
# print(os.system('python -mail.py'))





from flask import Flask, request
from flask_mail import Mail,Message


app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_USERNAME'] = '69189668@qq.com'
# 授权码或者密码
app.config['MAIL_PASSWORD'] = 'xsaeccnuhttocaha'
mail = Mail(app) # 实例化邮件对象
# '@app.route('/arg/<name>/')'
@app.route('/send_mail/')
def send_mail():
    con = request.args.getlist('name','pwd')
    msg = Message(subject='而推欧赔第三方第三方',recipients=['1338332752@163.com'],sender=app.config['MAIL_USERNAME'])
    msg.html = con
    mail.send(msg)
    return '发送邮件1234567890'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True, threaded=True)
