def get_similar(cmd, i):
    n = len(cmd)
    cnt = 1
    if i > 0 and cmd[i - 1] != cmd[i]:
        cnt += 1
    if i < n - 1 and cmd[i + 1] != cmd[i]:
        cnt += 1
    if i > 0 and i < n - 1 and cmd[i - 1] == cmd[i + 1] and cmd[i] != cmd[i - 1]:
        cnt -= 1
    # print '###', i, cnt
    return cnt

def get_count(cmd):
    n = len(cmd)
    # print 'n:', n
    cnt = 1
    for i in xrange(n):
        cnt *= get_similar(cmd, i)
    
    return cnt

if __name__ == '__main__':
    fr = open('./A-large.in', 'r')
    fw = open('./LZresult.in', 'w')
    T = int(fr.readline())

    for i in xrange(T):
        cmd = fr.readline().strip()
        # print 'cmd:', cmd
        count = get_count(cmd)
        fw.write('Case #%d: %d\n' % ((i + 1), count % 1000000007))
        
    fr.close()
    fw.close()