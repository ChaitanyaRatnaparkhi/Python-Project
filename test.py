import subprocess
import os
from difflib import Differ


print("hi")

def diff(output_expected,output_got):
    d = Differ()
    compare = list(d.compare(output_expected.split(),output_got.split()))
    print("\n".join(compare))

def run(cmd,stdin=None):
    result = subprocess.run(cmd.split(' '),capture_output=True,text=True,stdin=stdin)
    return result

def testing_wc(inputFile,outputFile):
    
    result = run('python prog/wc.py '+inputFile)
    assert result.returncode == 0 ,result.stderr
    with open(outputFile,"r") as f:
        output_expected = f.read()
        if output_expected != result.stdout:
            print("expected")
            print(output_expected)
            print("received")
            print(result.stdout)
            diff(output_expected,result.stdout)
    assert output_expected.rstrip() == result.stdout.rstrip()

if __name__ == '__main__':

    for filename in os.listdir('test'):
        if filename.startswith('wc') and filename.endswith('in'):
            testing_wc('test/'+filename,'test/'+filename.replace('in','out'))
