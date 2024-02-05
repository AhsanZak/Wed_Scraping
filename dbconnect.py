import sqlite3


def create_database():
    conn = sqlite3.connect('movie_database.db')

    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS movies (
        movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_name TEXT NOT NULL,
        release_date TEXT NOT NULL
    );
    '''

    cursor.execute(create_table_query)

    conn.commit()
    conn.close()

    conn = sqlite3.connect('movie_database.db')
    cursor = conn.cursor()


def get_query(sql_query):
    try:
        conn = sqlite3.connect('movie_database.db')
        cursor = conn.cursor()
        cursor.execute(sql_query)

        results = [row[0] for row in cursor.fetchall()]

        conn.commit()
        conn.close()
        print("SQL query executed successfully.")
        return results

    except sqlite3.Error as e:
        print(f"Error executing SQL query: {e}")


def insert_movies_rows(movie_dict):
    try:
        
        movie_list = get_all_movies()

        conn = sqlite3.connect('movie_database.db')
        cursor = conn.cursor()

        # Insert rows into the 'movies' table using a loop
        for movie_name, release_date in movie_dict.items():
            if not movie_name in movie_list:
                insert_query = '''
                INSERT INTO movies (movie_name, release_date)
                VALUES (?, ?);
                '''

                cursor.execute(insert_query, (movie_name, release_date))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print("Rows inserted into the 'movies' table successfully.")

    except sqlite3.Error as e:
        print(f"Error inserting rows into the 'movies' table: {e}")



def get_all_movies():
    sql = "SELECT movie_name FROM movies"
    data = list(get_query(sql))
    return data

# create_database()
