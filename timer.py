#from __future__ import print_function
import datetime 
import sys 
import signal
import time
import os

class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self,signum, frame):
        self.kill_now = True


def load_db():
    db = {} 
    file_address=os.path.join(os.path.split(__file__)[0], 'log.db')
    with open(file_address, 'r') as f:
        for line in f: 
            key, value = line.split('\t')
            value = int(value)
            db[key] = value 
            print '{}:\t{}'.format(key, hms(value))
    return db

def save_db(db):
    file_address=os.path.join(os.path.split(__file__)[0], 'log.db')
    with open(file_address, 'w') as f:
        for key, val in db.iteritems():
            f.write('{}\t{}\n'.format(key, val))

def hms(t): 
    return '{}:{}:{}'.format(int(t/(60*60)), int(t/60)%60, int(t%60), )


if __name__ == '__main__': 
    if len(sys.argv) < 2:
        raise Exception('Tell me what you doin')

    category = sys.argv[1]
    start = datetime.datetime.now()

    killer = GracefulKiller()
    db = load_db()
    saved_t = db.get(category, 0)
    db[category] = saved_t
    while not killer.kill_now: 
        end = datetime.datetime.now()
        time.sleep(1)
        during = end - start
        ts = during.total_seconds()
        print  '\r', '{}:{}\t|total:\t{}'.format(category, hms(ts), hms(ts+saved_t) ), 
        sys.stdout.flush()
    db[category] += int(during.total_seconds())
    save_db(db)
    print  '\nSaved {}:{}\t|total:\t{}'.format(category, hms(ts), hms(ts+saved_t) ), 
    
