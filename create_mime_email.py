from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def mail_report(to, ticker_name):
    outer = MIMEMultipart()
    outer['Subject'] = 'Stock report for ' + ticker_name
    outer['From'] = '67501688@qq.com'
    outer['To'] = to

    # Internal text container
    inner = MIMEMultipart('alternative')
    text = 'Here is the stock report for ' + ticker_name
    html = """\
    <html>
        <head></head>
        <body>
            <p>Here is the stock report for <b> """ + ticker_name + """</b></p>
        </body>
    </html>
    """
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    inner.attach(part1)
    inner.attach(part2)
    outer.attach(inner)

    filename = 'stocktracker-%s.csv' % ticker_name
    csv_text = ''.join(file(filename).readlines())
    csv_part = MIMEText(csv_text, 'csv')
    csv_part.add_header('Content-Disposition', 'attachment', filename=filename)
    outer.attach(csv_part)
    return outer


def send_message(message):
    s = smtplib.SMTP('smtp.qq.com')
    s.login('67501688@qq.com', 'myscaubaidu')
    s.sendmail(message['From'], message['To'], message.as_string())
    s.close()
if __name__ == '__main__':
    email = mail_report('winstar1688@qq.com', 'GOOG')
    send_message(email)

















