# mail_integration/email_importer.py
import imaplib
import email
from email.header import decode_header
from .models import EmailMessage

def fetch_emails(username, password, server, port=993):
    # Подключение к серверу IMAP
    mail = imaplib.IMAP4_SSL(server, port)
    mail.login(username, password)
    mail.select("inbox")

    # Поиск всех сообщений
    status, messages = mail.search(None, 'ALL')
    email_ids = messages[0].split()

    for email_id in email_ids:
        # Получение письма
        status, msg_data = mail.fetch(email_id, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])

        # Парсинг сообщения
        subject = decode_header(msg.get("Subject"))[0][0].decode()
        sent_date = msg.get("Date")
        body = ""
        attachments = []

        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                if "attachment" in content_disposition:
                    filename = part.get_filename()
                    attachments.append(filename)
                
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
        else:
            body = msg.get_payload(decode=True).decode()

        # Сохранение сообщения в базе данных
        EmailMessage.objects.create(
            subject=subject,
            sent_date=sent_date,
            received_date=None,  # Можно установить текущую дату
            body=body,
            attachments=attachments
        )
    mail.logout()
