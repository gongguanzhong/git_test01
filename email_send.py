# coding:utf-8
import time, os, datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# 定义发送邮件
def sentmail(file_new):
    # 发送邮件
    mail_from = '18872206315@163.com'
    # 收信邮箱
    # mail_to = '9261904@qq.com'
    mail_to = ["9261904@qq.com", "346985191@qq.com"]
    # 读文件
    with open(file_new, 'rb') as f:
        mail_body = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = u'志愿填报接口测试'
    msg['form'] = mail_from
    msg['to'] = ",".join(mail_to)
    # msg['to'] = mail_to
    # 正文,发送unittest的报告时会出现html显示问题，可以把正文注释掉，自定义内容，然后把报告通过附件传
    body = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(body)
    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment;filename="test_report.html"'
    msg.attach(att)
    # 定义发送时间（不定义可能有的邮件客户端不显示发送时间）
    # msg['date'] = time.strftime('%a, %d %b %Y  %H:%M:%S  %z')
    smtp = smtplib.SMTP()
    # 连接SMTP服务器，此处用的163的smtp服务器
    smtp.connect('smtp.163.com')

    # 用户名密码
    smtp.login('18872206315@163.com', 'q9261904')
    smtp.sendmail(mail_from, mail_to, msg.as_string())
    smtp.quit()
    print('email has send out !')


# 查找测试报告，调用发邮件功能
def sendreport():
    result_dir = 'E:\\report\\'
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not
    os.path.isdir(result_dir + "\\" + fn) else 0)
    print(u'上一次测试生成的报告:' + lists[-1])
    file_new = os.path.join(result_dir, lists[-1])
    print(file_new)
    # 调用发邮件模块
    sentmail(file_new)


if __name__ == "__main__":
    # 执行发邮件
    sendreport()
