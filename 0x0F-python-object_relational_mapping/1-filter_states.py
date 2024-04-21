#!/usr/bin/python3
"""
Script to list all states starting with 'N' from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

def list_states_starting_with_n(username, password, database):
    """
    Lists all states starting with 'N' from the specified database.
    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
    Returns:
        None
    """
    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cur = conn.cursor()

    # Execute SQL query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows
    rows = cur.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    list_states_starting_with_n(sys.argv[1], sys.argv[2], sys.argv[3])
