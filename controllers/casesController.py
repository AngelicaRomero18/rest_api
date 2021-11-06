import config.database as database


def get_cases():
    conn = database.get_connection()
    cases = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM casos")
        cases = cursor.fetchall()
    conn.close()
    return cases
