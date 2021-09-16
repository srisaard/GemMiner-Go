import subprocess
from time import sleep


def checkHash():
    print("START CHECK HASH RATE PLEASE WAIT")
    res = subprocess.check_output(
        ['./main.exe',
         '-callCheckHash', "Yes"],
        universal_newlines=True,
        stderr=subprocess.STDOUT)
    print(res)
    print("HASH RATE CHECK DONE")
    print("####################")


def restart(sProcesses):
    for i in range(len(sProcesses)):
        try:
            sProcesses[i].terminate()
            print(f"Terminate Thread#{i}")
        except:
            print(f"Terminate FAILED Thread#{i}")
            pass
        sProcesses[i] = subprocess.Popen(
                    ['python', 'raritygems.py'], stdout=subprocess.PIPE,
                    universal_newlines=True, stderr=subprocess.STDOUT)
        print(f"Start Thread#{i}")
        sleep(10)
    return sProcesses


checkHash()
print("LOOP: START subprocess")
sProcesses = [None, None, None]


while True:
    try:
        for i, sProcess in enumerate(sProcesses):
            try:
                if not sProcess:  # any thread send Tx and close itself
                    raise AttributeError

                if sProcess.poll() is None:
                    print(f"Thread {i} is runing")
                else:  # any thread has error
                    raise AttributeError
                    # print(f"Restart Thread#{i}")

            except AttributeError:
                sProcesses = restart(sProcesses)
                print("RESTART ALL THREAD : DONE")
                break
        sleep(10)
    except Exception as e:
        print(e.stdout[:-1])
