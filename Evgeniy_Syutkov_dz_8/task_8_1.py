import re


def email_parse(email_address):
    RE_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[\w]+\.\w+)', re.IGNORECASE)
    if not RE_email.match(email_address):
        raise ValueError(f'wrong email {email_address}')
    print(RE_email.match(email_address).groupdict())


try:
    email_parse('someone@geekbrains.ru')
    email_parse('someone@geekbrainsru')
except ValueError as err:
    print(err)
