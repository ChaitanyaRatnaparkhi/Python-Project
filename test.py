import subprocess
import os
from difflib import Differ



def diff(output_expected,output_got):
    d = Differ()
    compare = list(d.compare(output_expected.split(),output_got.split()))
    print("\n".join(compare))

def run(cmd,stdin=None):
    result = subprocess.run(cmd.split(' '),capture_output=True,text=True,stdin=stdin)
    return result
def runCat(cmd):
    result = subprocess.Popen(cmd.split(' '),stdout=subprocess.PIPE)
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
    passed['wc']+=1
    print(inputFile)
    stdinInput = runCat('cat '+inputFile)
    
    result = run('python prog/wc.py',stdin=stdinInput.stdout)
    
    with open(outputFile.replace('.out','.stdin.out'),"r") as f:
        output_expected = f.read()
        if output_expected != result.stdout:
            print("expected")
            print(output_expected)
            print("received")
            print(result.stdout)
            diff(output_expected,result.stdout)
    assert output_expected.rstrip() == result.stdout.rstrip()
    passed['wc']+=1
    


def testing_gron(inputFile,outputFile,base=''):
    print(base)
    baseflag = ''
    if base != '':
        baseflag = ' --obj '+ base

    print(baseflag)
    result = run('python prog/gron.py'+baseflag+' '+inputFile)
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
    passed['gron']+=1
    print(inputFile)
    stdinInput = runCat('cat '+inputFile)
    
    result = run('python prog/gron.py'+baseflag,stdin=stdinInput.stdout)
    
    with open(outputFile,"r") as f:
        output_expected = f.read()
        if output_expected != result.stdout:
            print("expected")
            print(output_expected)
            print("received")
            print(result.stdout)
            diff(output_expected,result.stdout)
    assert output_expected.rstrip() == result.stdout.rstrip()
    passed['gron']+=1




def testing_cc(inputFile,outputFile,base=''):
    print(base)
    baseflag = ''
    if base != '':
        baseflag = ' -f '+ base

    print(baseflag)
    result = run('python prog/cc.py'+baseflag+' '+inputFile)
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
    passed['cc']+=1
    print(inputFile)
    stdinInput = runCat('cat '+inputFile)
    
    result = run('python prog/cc.py'+baseflag,stdin=stdinInput.stdout)
    
    with open(outputFile,"r") as f:
        output_expected = f.read()
        if output_expected.rstrip() != result.stdout.rstrip():
            print("expected")
            print(output_expected)
            print("received")
            print(result.stdout)
            diff(output_expected,result.stdout)
    assert output_expected.rstrip() == result.stdout.rstrip()
    passed['cc']+=1


passed = {'wc':0,'gron':0,'cc':0}
failed = {'wc':0,'gron':0,'cc':0}

if __name__ == '__main__':

    for filename in os.listdir('test'):
        if filename.startswith('wc') and filename.endswith('in'):
            try:
                testing_wc('test/'+filename,'test/'+filename.replace('in','out'))
            except Exception  or AssertionError as e:
                failed['wc']+=1
                print(e)

        if filename.startswith('gron') and filename.endswith('in') and not '-' in filename:
            try:
                testing_gron('test/'+filename,'test/'+filename.replace('in','out'))
            except Exception  or AssertionError as e:
                failed['gron']+=1
                print(e)
        
        if filename.startswith('cc')  and filename.endswith('in'):
           
            try:
                testing_cc('test/'+filename,'test/'+filename.replace('in','out'),'encrypt')
            except Exception  or AssertionError as e:
                failed['cc']+=1
                print(e)
            
            try:
                testing_cc('test/'+filename.replace('in','out'),'test/'+filename,'decrypt')
            except Exception  or AssertionError as e:
                failed['cc']+=1
                print(e)

    if failed['wc'] != 0 or  failed['cc'] != 0 or  failed['gron'] != 0:

        exit(1)
    

    print("Total test cases", sum([number for key,number in passed.items()])+sum([number for key,number in failed.items()]) )

    print('passed test cases', passed)
    print("failed test cases", failed)
