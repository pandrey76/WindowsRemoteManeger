import os
from subprocess import PIPE, Popen
import win32process

# import codecs
# from chardet.universaldetector import UniversalDetector

from time import sleep

class RunPowerShellScript:
    """

    """

    def __init__(self):
        """

        """
        self.__PowerShell = "powershell.exe"

    def run_script(self, full_script_path):
        """

        :param full_script_path:
        :return:
        """
        space = ' '
        run_string = self.__PowerShell
        run_string += space

        run_string += '"'

        run_string += full_script_path

        run_string += '"'

        os.system(run_string)

    def run_ps_script(self, full_script_path, args):
        """

        :param full_script_path:
        :param args:
        :return:
        """
        space = ' '
        run_string = self.__PowerShell
        run_string += space

        run_string += '"'

        run_string += full_script_path

        run_string += '"'

        if len(args) > 0:
            for ar in args:
                run_string += space
                run_string += '"'
                run_string += ar
                run_string += '"'

        os.system(run_string)

    def run_ps(self, full_path_2_ps, args):
        """

        """
        cmd_arg = [self.__PowerShell, full_path_2_ps]
        if len(args) > 0:
            for ar in args:
                cmd_arg.append(ar)
        process = Popen(cmd_arg, stdout=PIPE)
        data = process.communicate()
        for line in data:
            print(line)
        code = process.wait()
        print(code)  # 0

    def run_ps_with_dispatching_process(self, full_path_2_ps, seconds_delay):
        """

        """
        cmd_arg = [self.__PowerShell, full_path_2_ps]
        # if len(args) > 0:
        #     for ar in args:
        #         cmd_arg.append(ar)
        # process = Popen(cmd_arg, shell=False, creationflags=win32process.CREATE_NEW_CONSOLE)
        process = Popen(cmd_arg, shell=False, close_fds = True)
        sleep(seconds_delay)
        # data = process.communicate()
        # for line in data:
        #     print(line)
        # code = process.wait()
        # print(code)  # 0

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
    with open(temp_file, 'r', encoding='utf-16') as g:
        res = g.read()

    return res


def block_user(user):
    """
    :param user:
    :return:
    """


if __name__ == "__main__":
    run_script = RunPowerShellScript()
    # run_script.run_script("..//PS//RecoverUserFromBan.ps1")
    # run_script.run_ps("../PS/RecoverUserFromBan.ps1", [])
    # run_script.run_script("..//PS//BanUser.ps1")
    # run_script.run_script("..//PS//LogoffUser.ps1")
    arg = ["TempUser"]
    run_script.run_ps("../PS/LogoffUser.ps1", arg)
    # run_script.run_ps("../PS/BanUser.ps1", arg)
    #print(os.path.expanduser(os.getenv('USERPROFILE')))
    #print(get_calculater_appid())

