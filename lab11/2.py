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
CREATE OR REPLACE PROCEDURE insert_or_update_user(
    p_first_name VARCHAR(50),
    p_last_name VARCHAR(50),
    p_phone VARCHAR(50)
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- Check if the user already exists
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_first_name AND last_name = p_last_name) THEN
        -- Update phone number
        UPDATE phonebook
        SET phone = p_phone
        WHERE first_name = p_first_name AND last_name = p_last_name;
    ELSE
        -- Insert new user
        INSERT INTO phonebook (first_name, last_name, phone)
        VALUES (p_first_name, p_last_name, p_phone);
    END IF;
END;
$$;
""")
conn.commit()
def insert_or_update_user(first_name, last_name, phone):
    cur.execute("CALL insert_or_update_user(%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
insert_or_update_user('John', 'Doe', '3456789')
cur.close()
conn.close()
