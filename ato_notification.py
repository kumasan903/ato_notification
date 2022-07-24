from plyer import notification
import datetime
import time
import schedule

def job():
    notification.notify(
    title='AirTycoonOnline Turn over',
    message='The turn of AirTycoonOnline has changed.',
    app_name='app name',
    app_icon='./icon.ico'
    )

schedule.every().day.at("01:10").do(job)
schedule.every().day.at("03:10").do(job)
schedule.every().day.at("05:10").do(job)
schedule.every().day.at("07:10").do(job)
schedule.every().day.at("19:10").do(job)
schedule.every().day.at("11:10").do(job)
schedule.every().day.at("13:10").do(job)
schedule.every().day.at("15:10").do(job)
schedule.every().day.at("19:10").do(job)
schedule.every().day.at("21:10").do(job)
schedule.every().day.at("23:10").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)