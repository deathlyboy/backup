import time

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import db
import schedule


gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)


def upload_file(file_path):
    try:
        file = drive.CreateFile()
        file.SetContentFile(file_path)
        file.Upload()

        db.set_drive_id(file_path, file['id'])
        return 'File was uploaded'
    except Exception as ex:
        print('upload error')
        return f'{ex}'


def update_file(file_path):
    try:
        file = drive.CreateFile({'id': db.get_drive_id(file_path)})
        file.SetContentFile(file_path)
        file.Upload()

        return 'File was updated'
    except Exception as ex:
        print('update error')
        return f'{ex}'


def main():
    path = r'C:\Users\deathly\AppData\Roaming\Flashnote\notes2.db'
    schedule.every().day.at('12:00').do(update_file, path)
    schedule.every().day.at('16:00').do(update_file, path)
    schedule.every().day.at('20:00').do(update_file, path)

    while True:
        time.sleep(55)
        schedule.run_pending()


if __name__ == '__main__':
    main()
