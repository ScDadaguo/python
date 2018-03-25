import smtplib
from email.mime.text import MIMEText
class send_emall:
    @staticmethod
    def send_emall(title,content):
        msg_from = '891792055@qq.com'  # 发送方邮箱
        passwd = 'dczomctucbpdbcge'  # 填入发送方邮箱的授权码
        msg_to = '891792055@qq.com'  # 收件人邮箱

        subject = title  # 主题     　　  # 正文
        # content = "这是我使用python smtplib及email模块发送的邮件"
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print("发送成功")

        except:
            print("失败")
        finally:
            s.quit()