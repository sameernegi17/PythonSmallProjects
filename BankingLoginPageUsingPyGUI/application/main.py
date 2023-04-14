from view.loginpage import *

def verify():
    window = create_login_window()
    username, password = get_login_details(window).values()
    window.close()
    while True:
        if username == "sameer" and password == "123":
            show_success_window()
            break
        else:
            if show_failure_window():
                window = create_login_window()
                username, password = get_login_details(window).values()
                window.close()

if __name__ == "__main__":
    verify()