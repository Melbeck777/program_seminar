import os
import subprocess as sb
from pathlib import Path
import sys

args = sys.argv
folder = args[1]
runFile = args[2]

for path in Path(os.path.join(folder, "input")).glob("*.txt"):
    with open(path, "r", encoding="utf-8") as f:
        try:
            result  = sb.run(["py", runFile], stdout=sb.PIPE, stdin=f, check=True).stdout
        except sb.CalledProcessError:
            raise Exception("The code has an error")
        print(str(result).replace("\\r","").replace("\\n","").replace("b'","").replace("'", ""))