'''
Created on Aug 27, 2016
@author: Burkhard
'''
# Scheduling imports
import schedule

# Windows Service imports
import win32service
import win32serviceutil  
import win32event                              

import os
import os.path
import importlib.util

path_to_run_script = os.getcwd()
path_to_run_script = os.path.join(path_to_run_script, 'ActivateEngine.py')

#spec = importlib.util.spec_from_file_location("ActivateEngine.Engine", path_to_run_script)
#activate_engine = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(activate_engine)
#from ActivateEngine import Engine


class PythonTaskSvc(win32serviceutil.ServiceFramework):  
    _svc_name_ = "PythonTaskSvc"    
    _svc_display_name_ = "Python Task Scheduling Service"   
    _svc_description_ = "This Python service schedules tasks"  
      
    def __init__(self, args):  
        win32serviceutil.ServiceFramework.__init__(self,args)  
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)  
        
    def SvcDoRun(self):  
        def job():
            with open("c:\\13.txt", 'a') as g:
                g.write("Job_")
                g.write("hello")
                g.write(os.linesep)
                #g.write(str(activate_engine))
                try:
                    print("Hello")
                    #g.write(str(activate_engine))
                    #eng = activate_engine.Engine()
                    #g.write(str(eng))
                    #eng.run()
                except Exception as er:
                   g.write(str(er))

        schedule.every(1).minutes.do(job)
        
        rc = None
        while rc != win32event.WAIT_OBJECT_0:
            schedule.run_pending()
            rc = win32event.WaitForSingleObject(self.hWaitStop, 5000)  
            
    def SvcStop(self):  
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)  
        win32event.SetEvent(self.hWaitStop)  


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonTaskSvc)  
    




#===============================================================================
# python Task_Scheduler_Svc.py install
# python Task_Scheduler_Svc.py remove

# Usage: 'Task_Scheduler_Svc.py [options] install|update|remove|start [...]|stop|restart [...]|debug [...]'
# Options for 'install' and 'update' commands only:
#  --username domain\username : The Username the service is to run under
#  --password password : The password for the username
#  --startup [manual|auto|disabled|delayed] : How the service starts, default = manual
#  --interactive : Allow the service to interact with the desktop.
#  --perfmonini file: .ini file to use for registering performance monitor data
#  --perfmondll file: .dll file to use when querying the service for
#    performance data, default = perfmondata.dll
# Options for 'start' and 'stop' commands only:
#  --wait seconds: Wait for the service to actually start or stop.
#                  If you specify --wait with the 'stop' option, the service
#                  and all dependent services will be stopped, each waiting
#                  the specified period.
#===============================================================================
