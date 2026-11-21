from database import get_connection, create_table
from students import add_student
from students import view_all
from students import by_subject
from students import class_average
from students import top_scorer

def main():
    conn = get_connection()
    
    if conn is not None:
        create_table(conn)

        while True:
            print("\n----OPTION----")
            print("1. Add Students")
            print("2. View All")
            print("3. View by subject")
            print("4. Class average")
            print("5. Top Scorer")
            print("6`. EXit")

            option = input("Choose: ")

            if option == "1":
                name = input("Enter name: ")

                score = int(input("Enter score: "))

                subject = input("Enter subject: ")

                add_student(conn, name, score, subject)

            elif option == "2":
                view_all(conn)

            elif option == "3":
                subject = input("Enter subject: ")
                by_subject(conn, subject)

            elif option == "4":
                class_average(conn)

            elif option == "5":
                top_scorer(conn)
        

            elif option == "6":
                conn.close()
                print("Thanks for using STUDENT GRADEBOOK")
                break

            else:
                print("Invalid choice")

if __name__ == "__main__":
    main()





            