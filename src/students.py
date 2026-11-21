def add_student(conn, name, score, subject):
    cursor = conn.cursor()
    
    query = "INSERT INTO students (name, score, subject) VALUES (%s, %s, %s)"
    
    values = (name, score, subject)
    cursor.execute(query, values)
    conn.commit()
    print(f"Successfully added {name} to the database")

def view_all(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    
    for row in results:
        print(f"ID: {row[0]} | {row[1]} | {row[2]} | {row[3]}")

def by_subject(conn, subject):
    cursor = conn.cursor()
    query = "SELECT * FROM students WHERE subject = %s"
    value = (subject)
    cursor.execute(query, (value,))
    result =   cursor.fetchall()

    for row in result:
        print(f"ID: {row[0]} | {row[1]} | {row[2]} | {row[3]}")
    

def class_average(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(score) FROM students")
    result = cursor.fetchone()
    if result and result[0] is not None:
        print(f"The class average is {result[0]:.2f}")
    else:
        print("No scores in the database yet.")

def top_scorer(conn):
    cursor = conn.cursor()
    query = "SELECT name, score FROM students ORDER BY score DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    if result is not None:
        print(f"Top scorer: {result[0]} with a score of {result[1]}")
    else:
        print("No student found")