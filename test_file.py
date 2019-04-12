import pandas as pd
from django.core.mail import send_mail


def read_file(csv_file_path):
    data = pd.read_csv(csv_file_path)

    if data is not None:
        send_email(data)

def send_email(data):

    send_mail(
        'Subject',
         data,
        from@sender.com,
        ['to@receiver.com'],
        fail_silently=False,
    )

custom_input = input("Enter location of your csv file: ")
## for example "/home/file_name.csv"
res = read_file(custom_input)
