import mysql.connector
from datetime import datetime

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change to your MySQL user
        password="hafeez", # change to your MySQL password
        database="quiz_db"
    )

def admin_login():
    username = input("Enter Admin Username: ")
    password = input("Enter Password: ")

    db = connect_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM admin WHERE username=%s AND password=%s", (username, password))
    admin = cur.fetchone()

    if admin:
        print("\n Login Successful!\n")
        admin_menu()
    else:
        print("\n Invalid Credentials!\n")

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Question")
        print("2. Modify Question")
        print("3. Delete Question")
        print("4. View All Questions")
        print("5. View All Users & Scores")
        print("6. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            add_question()
        elif choice == "2":
            modify_question()
        elif choice == "3":
            delete_question()
        elif choice == "4":
            view_questions()
        elif choice == "5":
            view_users()
        elif choice == "6":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice, try again.")

def add_question():
    tech = input("Enter Technology: ")
    q_text = input("Enter Question: ")
    opt1 = input("Option 1: ")
    opt2 = input("Option 2: ")
    opt3 = input("Option 3: ")
    opt4 = input("Option 4: ")
    correct = int(input("Correct Option (1-4): "))

    db = connect_db()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO questions (technology, question_text, option1, option2, option3, option4, correct_answer)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, (tech, q_text, opt1, opt2, opt3, opt4, correct))
    db.commit()
    print(" Question Added!")

def modify_question():
    qid = input("Enter Question ID to modify: ")

    new_q = input("Enter New Question Text: ")
    new_o1 = input("New Option 1: ")
    new_o2 = input("New Option 2: ")
    new_o3 = input("New Option 3: ")
    new_o4 = input("New Option 4: ")
    new_correct = int(input("New Correct Option (1-4): "))

    db = connect_db()
    cur = db.cursor()
    cur.execute("""
        UPDATE questions
        SET question_text=%s, option1=%s, option2=%s, option3=%s, option4=%s, correct_answer=%s
        WHERE q_id=%s
    """, (new_q, new_o1, new_o2, new_o3, new_o4, new_correct, qid))
    db.commit()
    print(" Question Updated!")

def delete_question():
    qid = input("Enter Question ID to delete: ")

    db = connect_db()
    cur = db.cursor()
    cur.execute("DELETE FROM questions WHERE q_id=%s", (qid,))
    db.commit()
    print(" Question Deleted!")

def view_questions():
    db = connect_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM questions")
    rows = cur.fetchall()
    print("\n--- All Questions ---")
    for row in rows:
        print(row)

def view_users():
    db = connect_db()
    cur = db.cursor()
    cur.execute("""
        SELECT u.username, u.mobile, r.technology, r.score, r.quiz_time
        FROM users u
        JOIN results r ON u.user_id=r.user_id
    """)
    rows = cur.fetchall()
    print("\n--- Users & Scores ---")
    for row in rows:
        print(row)

def user_login():
    username = input("Enter Your Name: ")
    mobile = input("Enter Mobile Number: ")

    db = connect_db()
    cur = db.cursor()

    cur.execute("SELECT * FROM users WHERE username=%s AND mobile=%s", (username, mobile))
    user = cur.fetchone()

    if not user:
        cur.execute("INSERT INTO users (username, mobile) VALUES (%s,%s)", (username, mobile))
        db.commit()
        cur.execute("SELECT * FROM users WHERE username=%s AND mobile=%s", (username, mobile))
        user = cur.fetchone()
        print("\n New User Registered!\n")
    else:
        print("\n Welcome Back!\n")

    user_menu(user[0])   # pass user_id

def user_menu(user_id):
    while True:
        print("\n--- User Menu ---")
        print("1. Take Quiz")
        print("2. View Top 3 Scores")
        print("3. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            take_quiz(user_id)
        elif choice == "2":
            top_scores()
        elif choice == "3":
            print("Logging out...\n")
            break
        else:
            print("Invalid choice. Try again.")

def take_quiz(user_id):
    tech = input("Enter Technology (Python/MySQL/etc): ")

    db = connect_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM questions WHERE technology=%s", (tech,))
    questions = cur.fetchall()

    if not questions:
        print(" No Questions Available for this technology!")
        return

    score = 0
    for q in questions:
        print(f"\nQ{q[0]}: {q[2]}")
        print(f"1. {q[3]}  2. {q[4]}  3. {q[5]}  4. {q[6]}")
        ans = int(input("Your Answer (1-4): "))

        if ans == q[7]:
            score += 1

    print(f"\n Quiz Completed! Your Score = {score}/{len(questions)}")

    cur.execute("""
        INSERT INTO results (user_id, technology, score, quiz_time)
        VALUES (%s,%s,%s,%s)
    """, (user_id, tech, score, datetime.now()))
    db.commit()
    print("Result Saved!")

def top_scores():
    db = connect_db()
    cur = db.cursor()
    cur.execute("""
        SELECT u.username, u.mobile, r.technology, r.score
        FROM results r
        JOIN users u ON r.user_id=u.user_id
        ORDER BY r.score DESC
        LIMIT 3
    """)
    rows = cur.fetchall()

    print("\n--- Top 3 Scores ---")
    for row in rows:
        print(f"Name: {row[0]}, Mobile: {row[1]}, Tech: {row[2]}, Score: {row[3]}")

def main():
    while True:
        print("\n==== QUIZ SYSTEM ====")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            admin_login()
        elif choice == "2":
            user_login()
        elif choice == "3":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
