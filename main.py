# This is a sample Python script.
import sqlite3
import datetime
import sys
from sqlite3 import Error

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Tasks:

    def create_table(conn):
        try:
            c = conn.cursor()
            tbl = ''' CREATE TABLE IF NOT EXISTS TASK(
                                    id integer PRIMARY KEY,
                                    message text NOT NULL,
                                    status text NOT NULL,
                                    started_at text NOT NULL,
                                    stopped_at text NOT NULL)'''
            c.execute(tbl)
        except Error as e:
            print(e)


    def list(conn):
        print("These are all the tasks in our current table:")
        print("ID  ,Message   ,Status   ,Starting Time      ,Stopped Time      ,Duration")

        try:
            c = conn.cursor()
            data = c.execute("SELECT * FROM TASK")
            current_time = "" + str(datetime.datetime.now().day) + "/" + str(datetime.datetime.now().month) + "/" + str(
                datetime.datetime.now().year) + "  " + str(datetime.datetime.now().hour) + ":" + str(
                datetime.datetime.now().minute)

            for row in data:
                if row[2] == "running":
                    durr = datetime.datetime.now()-datetime.datetime.strptime(row[3], "%d/%m/%Y %H:%M")
                else:
                    durr = datetime.datetime.strptime(row[4], "%d/%m/%Y %H:%M")-datetime.datetime.strptime(row[3], "%d/%m/%Y %H:%M")
                print(row, durr)
        except Error as e:
            print(e)


    def create(conn, txtstring):
        current_time = ""+ str(datetime.datetime.now().day) +"/"+ str(datetime.datetime.now().month) + "/"+ str(datetime.datetime.now().year) + "  "+ str(datetime.datetime.now().hour)+ ":"+ str(datetime.datetime.now().minute)
        try:
            c = conn.cursor()
            c.execute("""
                INSERT INTO TASK(message, status, started_at, stopped_at) 
                VALUES ( ?, "running", ?, "N/A")""",
                      (txtstring, current_time))
            conn.commit()
            return ("Your task: " + txtstring + " has been added!")
        except Error as e:
            print(e)

    def update(conn, ID, msg):
        try:
            c = conn.cursor()
            c.execute('''UPDATE TASK SET message = ? WHERE id=?;''',(msg, ID))
            conn.commit()
            return ("Task "+ str(ID) +" has been updated to: "+ msg)
        except Error as e:
            print(e)

    def delete(conn, ID):
        try:
            c= conn.cursor()
            res = c.execute("SELECT id FROM TASK WHERE id=?;", (ID,))
            if (res.fetchone() is None):
                return("Task "+ str(ID)+ " is not in table")
            else:
                c.execute('''DELETE FROM TASK WHERE id=?
                ''', (ID,))
                conn.commit()
                return("Task "+ str(ID) +" has been deleted")
        except Error as e:
            print(e)

    def stop(conn, ID):
        try:
            c = conn.cursor()
            res = c.execute("SELECT status FROM TASK WHERE id=?;", (ID,))
            status = (str(res.fetchone()[0]))
            if (status == "running"):
                curr_time = "" + str(datetime.datetime.now().day) + "/" + str(datetime.datetime.now().month) + "/" + str(
                    datetime.datetime.now().year) + "  " + str(datetime.datetime.now().hour) + ":" + str(
                    datetime.datetime.now().minute)
                c.execute("UPDATE TASK SET stopped_at = ? WHERE id=ID;", (curr_time,))
                c.execute('''UPDATE TASK SET status = "stopped" WHERE id=ID;''')
                conn.commit()
                return ("Task "+ str(ID) + " has been stopped")
            else:
                print("Task has already been stopped")
        except Error as e:
            print(e)


    def main():
        con = sqlite3.connect("database.db")

        Tasks.create_table(con)

        n = len(sys.argv)
        if n>1:
            if (sys.argv[1]=="list"):
                Tasks.list(con)
            elif(sys.argv[1] == "create"):
                print(Tasks.create(con, sys.argv[2]))
            elif(sys.argv[1] == "update"):
                print(Tasks.update(con,sys.argv[2],sys.argv[3]))
            elif(sys.argv[1] == "delete"):
                print(Tasks.delete(con,sys.argv[2]))
            elif(sys.argv[1] == "stop"):
                print(Tasks.stop(con, sys.argv[2]))
            else:
                print("your input is not recognised")
        else:
            print("please use a method along with the script to preform functions such as $ python main.py create 'txt'")




if __name__ == '__main__':
    Tasks.main()


