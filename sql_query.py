create_user_table = """
CREATE TABLE users(
    id INTEGER PRIMARY KEY,
    name  TEXT,
    username TEXT
    );
"""

insert_query_user = """
INSERT INTO users (id , name , username) VALUES (? , ? , ?);
"""

select_query_allusers = """
SELECT * FROM users;
"""
select_one_user = """
SELECT * FROM users WHERE id = ?;
"""