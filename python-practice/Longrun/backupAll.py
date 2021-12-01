import shutil
import os
import logging
import time

CURRENT_TIME = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
TARGET_ROOT_PATH = "."
TARGET_PATH = os.path.abspath(TARGET_ROOT_PATH + "\\test_backup_" + CURRENT_TIME)

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)

def backupLogs():
    logging.info("Backuping logs of NavSever...")
    copyFolder("C:\\NAV\\NavServer\\Bin\\logs", TARGET_PATH + "\\logs")
    copyFolder("C:\\NAV\\NavServer\\Bin\\Log", TARGET_PATH + "\\Log")
    copyFolder("C:\\NAV\\Kafka\\logs", TARGET_PATH + "\\Kafka\\logs")
    copyFolder("C:\\var\\log", TARGET_PATH + "\\ts\\log")


def copyFolder(old_path, new_path):
    src_path = os.path.abspath(old_path)
    tgt_path = os.path.abspath(new_path)

    if os.path.exists(src_path):
        shutil.copytree(src_path, tgt_path)
        logging.info("successfully copied %s to %s", src_path, tgt_path)


def dumpDB(db_name):
    cmd1 = 'set PGPASSWORD=kuka'
    cmd2 = 'pg_dump --host=127.0.0.1 --port=5432 --username=postgres -Fc ' + db_name + ' > ' + TARGET_PATH + '\\' + db_name + '.dump'
    os.system(cmd1 + '&&' + cmd2)
    logging.info("successfully dump " + db_name + " to " + TARGET_PATH)


if __name__ == '__main__':
    backupLogs()
    dumpDB("NavBaseDB")
    dumpDB("db_task_scheduler")
    

