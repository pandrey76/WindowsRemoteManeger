import os
import codecs

#from chardet.universaldetector import UniversalDetector


def get_calculater_appid():
    """
    :param user:
    :return:
    """
    run_string = "powershell.exe"
    space = ' '

    run_string += space

    run_string += '"'

    run_string += os.path.join(os.getcwd(), "Finding_culculater.ps1")

    run_string += space
    run_string += '>'
    run_string += space

    temp_file = os.path.join(os.path.expanduser(os.getenv('USERPROFILE')), "out.txt")
    run_string += temp_file
    run_string += '"'

    status = os.system(run_string)



#    detector = UniversalDetector()
#    with open('test.txt', 'rb') as fh:
#        for line in fh:
#            detector.feed(line)
#            if detector.done:
#                break
#        detector.close()
#    print(detector.result)
    with open(temp_file, 'r', encoding='utf-16') as g: #codecs.open(temp_file, 'r', encoding='utf-16') as g:
        res = g.read()

    return res


def block_user(user):
    """
    :param user:
    :return:
    """


if __name__ == "__main__":
    print(os.path.expanduser(os.getenv('USERPROFILE')))
    print(get_calculater_appid())
