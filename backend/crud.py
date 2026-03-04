from database import get_db

def get_all_projects():
    try:
        conn = get_db()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Projects")
        projects = cursor.fetchall()

        cursor.close()
        conn.close()

        return projects

    except:
        # fallback demo data if DB fails on Render
        return [
            {
                "project_id": 1,
                "project_name": "Demo Project",
                "client_id": 1
            }
        ]