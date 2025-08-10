from models import init_db, add_user, get_user
import bcrypt

if __name__ == "__main__":
    init_db()
    # create demo user if not exists
    if not get_user("demo"):
        pw = "password123"
        ph = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt()).decode()
        add_user("demo", ph)
        print("Created demo user: demo / password123")
    else:
        print("Demo user exists.")
