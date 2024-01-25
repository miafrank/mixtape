import psycopg

"""
    *** Only intended for testing in local dev environment ***
"""

# TODO: Update to helpers to create, drop database in local dev env
with psycopg.connect("user=postgres", autocommit=True) as conn:
    cur = conn.cursor()
    conn.execute("CREATE DATABASE mixtape")
