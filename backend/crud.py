from database import get_db

def get_all_projects():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Projects")
    projects = cursor.fetchall()

    cursor.close()
    conn.close()

    return projects