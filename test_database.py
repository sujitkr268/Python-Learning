import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from database import create_table, get_connection

def test_table_exists():
    create_table()
    connection = get_connection()
    rows = connection.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='opportunities'"
    ).fetchall()
    connection.close()

    if len(rows) == 1:
        print("PASS: opportunities table exists")
    else:
        print("FAIL: opportunities table not found")

def test_columns():
    connection = get_connection()
    rows = connection.execute("PRAGMA table_info(opportunities)").fetchall()
    connection.close()

    columns = [row["name"] for row in rows]
    print("Columns:", columns)

    if columns == ["id", "title", "category"]:
        print("PASS: columns are correct")
    else:
        print("FAIL: unexpected columns")

def test_row_factory():
    connection = get_connection()
    cursor = connection.execute(
        "INSERT INTO opportunities (title, category) VALUES (?, ?)",
        ("Data Analyst Intern", "Data"),
    )
    connection.commit()

    # Read back the row we just inserted. Looking it up by its id (not with
    # "LIMIT 1") matters: the table already holds other rows, so LIMIT 1 would
    # return the first row of the table instead of the new one.
    new_id = cursor.lastrowid
    row = connection.execute(
        "SELECT title, category FROM opportunities WHERE id = ?",
        (new_id,)
    ).fetchone()

    # Remove the test row again so running this file does not fill the
    # database with "Data Analyst Intern" copies.
    connection.execute("DELETE FROM opportunities WHERE id = ?", (new_id,))
    connection.commit()
    connection.close()

    print("Row as dict:", dict(row))

    if row["title"] == "Data Analyst Intern":
        print("PASS: row_factory works (row['title'])")
    else:
        print("FAIL: row_factory not working")

if __name__ == "__main__":
    test_table_exists()
    test_columns()
    test_row_factory()
