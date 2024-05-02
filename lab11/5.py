import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1234"
)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        phone VARCHAR(50)
    )
""")
conn.commit()
cur.execute("""
CREATE OR REPLACE PROCEDURE delete_data(
    p_username VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_username IS NOT NULL THEN
        DELETE FROM phonebook WHERE first_name || ' ' || last_name = p_username;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = p_phone;
    ELSE
        RAISE EXCEPTION 'Specify either username or phone number to delete data.';
    END IF;
END;
$$;
""")
conn.commit()
def delete_data(username=None, phone=None):
    cur.execute("CALL delete_data(%s, %s)", (username, phone))
    conn.commit()
delete_data('John Doe', None)
cur.close()
conn.close()
