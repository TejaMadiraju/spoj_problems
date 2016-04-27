
testcases = int(raw_input());
out=[]
while testcases !=0:
    N = int(raw_input());
   # for val in range(0,N):
    op=0;
    men = map(int, raw_input().split());
    women = map(int, raw_input().split());
    men.sort();
    women.sort();
    for i in range (0,N):
        op = op+ men[i]*women[i];
    out.append(op)
    testcases = testcases-1;
for k in out :
    print k








