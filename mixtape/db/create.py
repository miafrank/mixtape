import psycopg

with psycopg.connect("user=postgres", autocommit=True) as conn:
    cur = conn.cursor()
    conn.execute("CREATE DATABASE mixtape")
