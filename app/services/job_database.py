from app.database.database import get_connection


def save_job(job):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO jobs
        (title, company, location, url, description, source)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        job.get("title", ""),
        job.get("company", ""),
        job.get("location", ""),
        job.get("url", ""),
        job.get("description", ""),
        job.get("source", "")
    ))

    connection.commit()

    job_id = cursor.lastrowid

    connection.close()

    return job_id


def get_all_jobs():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM jobs
        ORDER BY created_at DESC
    """)

    jobs = [dict(row) for row in cursor.fetchall()]

    connection.close()

    return jobs
