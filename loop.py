import subprocess

print("LOOP: START subprocess")
while True:
    try:
        res = subprocess.Popen(
            ['python', 'raritygems.py'], stdout=subprocess.PIPE,
            universal_newlines=True, stderr=subprocess.STDOUT)
        print(res.communicate())
    except Exception as e:
        print(e.stdout[:-1])
