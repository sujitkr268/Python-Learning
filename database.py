import os
import sqlite3


# The database file lives next to this file. Using an absolute path means the
# app always opens the SAME file, no matter which folder you start uvicorn
# from. (A relative path like "opportunity.db" would silently create a second,
# empty database whenever the working directory is different.)
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "opportunity.db")


def get_connection():
    # Opens (or creates) the database file and gives back a "connection" object.
    # A connection = your phone line to the database.
    connection = sqlite3.connect(DB_PATH)

    # Makes every row come back as a Row object that you can read by column name.
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_connection()
    try:
        connection.execute("""CREATE TABLE IF NOT EXISTS opportunities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL
            )
        """)

        # Saves the change permanently. Without this, close() would throw it away.
        connection.commit()
    finally:
        connection.close()


def get_all_opportunities():
    """Read every row from the opportunities table."""
    # 1. Open the database
    connection = get_connection()
    try:
        # 2. Run the SQL. "SELECT * FROM opportunities" = "give me all rows, all columns"
        #    execute() gives back a cursor (a pointer at the results).
        rows = connection.execute(
            "SELECT id, title, category FROM opportunities ORDER BY id"
        ).fetchall()

        # 3. Turn each row into a plain dict so FastAPI/JSON can understand it.
        #    This is a list comprehension: do the same thing for every row.
        return [dict(row) for row in rows]
    finally:
        # 4. Close the connection (hang up the phone) - even if something failed.
        connection.close()


def search_opportunities(search_term):
    """Return every opportunity whose title OR category contains search_term.

    The match is case-insensitive. The search term is escaped so that a user
    typing '%' or '_' searches for those literal characters instead of
    turning them into SQL wildcards.
    """
    pattern = "%" + escape_like(search_term) + "%"

    connection = get_connection()
    try:
        rows = connection.execute(
            """
            SELECT id, title, category FROM opportunities
            WHERE LOWER(title) LIKE LOWER(?) ESCAPE '\\'
               OR LOWER(category) LIKE LOWER(?) ESCAPE '\\'
            ORDER BY id
            """,
            (pattern, pattern),
        ).fetchall()

        return [dict(row) for row in rows]
    finally:
        connection.close()


def filter_opportunities(category="", title=""):
    """Return the opportunities matching the given category and/or title.

    An empty filter is ignored, so calling it with no arguments returns
    every opportunity.
    """
    clauses = []
    params = []

    if category:
        clauses.append("LOWER(category) LIKE LOWER(?) ESCAPE '\\'")
        params.append("%" + escape_like(category) + "%")

    if title:
        clauses.append("LOWER(title) LIKE LOWER(?) ESCAPE '\\'")
        params.append("%" + escape_like(title) + "%")

    sql = "SELECT id, title, category FROM opportunities"
    if clauses:
        sql += " WHERE " + " AND ".join(clauses)
    sql += " ORDER BY id"

    connection = get_connection()
    try:
        rows = connection.execute(sql, params).fetchall()
        return [dict(row) for row in rows]
    finally:
        connection.close()


def get_opportunity_by_id(opportunity_id):
    """Return one opportunity by its primary key, or None if it does not exist."""
    connection = get_connection()
    try:
        row = connection.execute(
            "SELECT id, title, category FROM opportunities WHERE id = ?",
            (opportunity_id,),
        ).fetchone()
        return dict(row) if row else None
    finally:
        connection.close()


def add_opportunity(title, category):
    """Insert one new row into the opportunities table and return it (with its id)."""
    connection = get_connection()
    try:
        # The ? marks are PLACEHOLDERS for values.
        # We never paste the values into the SQL text itself - that is what keeps
        # us safe from SQL injection, and it also handles quotes/apostrophes for us.
        cursor = connection.execute(
            "INSERT INTO opportunities (title, category) VALUES (?, ?)",
            (title, category)
        )

        connection.commit()

        # lastrowid is the id SQLite generated for the row we just inserted.
        new_id = cursor.lastrowid
        row = connection.execute(
            "SELECT id, title, category FROM opportunities WHERE id = ?",
            (new_id,)
        ).fetchone()

        return dict(row)
    finally:
        connection.close()


def update_opportunity_by_title(title, new_title, new_category):
    """Update the opportunity whose title matches `title` (case-insensitive).

    Returns the updated row as a dict, or None when no opportunity matches.
    """
    connection = get_connection()
    try:
        # Step 1: find the id of the row to update. ORDER BY id + LIMIT 1 makes
        # the choice deterministic even if several rows share the same title.
        row = connection.execute(
            """
            SELECT id FROM opportunities
            WHERE LOWER(title) = LOWER(?)
            ORDER BY id
            LIMIT 1
            """,
            (title,),
        ).fetchone()

        if row is None:
            return None

        opportunity_id = row["id"]

        # Step 2: update THAT row by its id (never by title - titles can change
        # and can be duplicated, ids cannot).
        connection.execute(
            "UPDATE opportunities SET title = ?, category = ? WHERE id = ?",
            (new_title, new_category, opportunity_id)
        )
        connection.commit()

        # Step 3: read the row back by its id so we return what is really stored.
        updated = connection.execute(
            "SELECT id, title, category FROM opportunities WHERE id = ?",
            (opportunity_id,),
        ).fetchone()

        return dict(updated)
    finally:
        connection.close()


def delete_opportunity_by_title(title):
    """Delete the opportunity whose title matches `title` (case-insensitive).

    Returns the deleted row as a dict, or None when no opportunity matches.
    """
    connection = get_connection()
    try:
        row = connection.execute(
            """
            SELECT id, title, category FROM opportunities
            WHERE LOWER(title) = LOWER(?)
            ORDER BY id
            LIMIT 1
            """,
            (title,),
        ).fetchone()

        if row is None:
            return None

        # Delete by id so we remove exactly the row we just looked at.
        connection.execute(
            "DELETE FROM opportunities WHERE id = ?",
            (row["id"],)
        )
        connection.commit()

        return dict(row)
    finally:
        connection.close()


def escape_like(value):
    """Escape the SQL LIKE wildcards (%, _ and the escape char itself)."""
    return value.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")


if __name__ == "__main__":
    create_table()

    # Only seed sample data the first time (when the table is empty),
    # so running this again does not create duplicates.
    if not get_all_opportunities():
        add_opportunity("Python Internship", "internship")
        add_opportunity("AI Competition", "competition")

    for row in get_all_opportunities():
        print(row)
