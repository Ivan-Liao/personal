import os
import datetime
import pendulum
import time

def main():

    start = pendulum.parse('12:00', tz='US/Eastern')
    end = pendulum.parse('18:00', tz='US/Eastern')

    while True:
        # start = pendulum.parse('00:00')
        # end = pendulum.parse('06:00')
        print('start: ', start,'end: ', end)

        now = pendulum.now("US/Eastern")
        print('now: ', now)
        if now > start and now < end:
            print('In between')
            time.sleep(180)
            os.system('shutdown -s')

if __name__ == '__main__':
    main()