import logging
from logging.handlers import SMTPHandler
from logging import Formatter

ADMINS = (
    "your_email@azcentral.com"
)

def setup_error_mail_handler(server, port):
  error_mail_handler = SMTPHandler((server, port),
                             'server-error@app_name.azcentral.com',
                             ADMINS, 'Dispatch Error')
  error_mail_handler.setLevel(logging.ERROR)
  error_mail_handler.setFormatter(Formatter('''
  Message type:       %(levelname)s
  Location:           %(pathname)s:%(lineno)d
  Module:             %(module)s
  Function:           %(funcName)s
  Time:               %(asctime)s

  Message:

  %(message)s
  '''))
  return error_mail_handler
