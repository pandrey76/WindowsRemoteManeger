import os


def get_calculater_appid():
    """
    :param user:
    :return:
    """
    run_string = "powershell.exe"

    run_string.join(" ")
    run_string.join(os.getcwd())
    run_string.join(os.pathsep)
    run_string.join("Finding_culculater.ps1")

    run_string.join(" ")
    run_string.join(">")
    run_string.join(" ")

    temp_file = "out.txt"
    run_string.join(temp_file)

    os.system('run_string')

    with open(temp_file, 'r') as g:
        res = g.read()

    return res


def block_user(user):
    """
    :param user:
    :return:
    """


if __name__ == "__main__":
    print(get_calculater_appid)
