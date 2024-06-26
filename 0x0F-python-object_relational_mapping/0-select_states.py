#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa.
"""
# Lists all states from the database hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY id ASC")
    [print(state) for state in cur.fetchall()]
    cur.close()
    conn.close()
