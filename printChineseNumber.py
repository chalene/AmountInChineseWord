# coding: utf-8
'''
导入文件后直接调用方法 convertChiNum()
输入：千万以下整数，值域[0,99999999]
输出：中文大写数字

'''
d={0:'零',1:'壹',2:'贰',3:'叁',4:'肆',5:'伍',6:'陆',7:'柒',8:'捌',9:'玖'}
unit = {0:'',1:'拾',2:'佰',3:'仟',4:'万'}
def transferMoney(b,s,outOfRange):
    s.append('万') if outOfRange else s.append('圆')
    cnt = 0
    flag = False
    if b == 0: 
        s.append(d[0])
    else:
        while b:
            if b%10:
                flag = True
                s.append(unit[cnt])
            if flag:
                s.append(d[b%10])
            b/=10
            cnt+=1

def convertChiNum(a):
    
    b = abs(a)
    s=[]
    transferMoney(b%10000,s,False)
    if b >= 10000:
        transferMoney(b/10000,s,True)

    if a < 0:
        s.append('负')
    print "".join(s[::-1])+"整"
    return "".join(s[::-1])+"整"


def main():
    convertChiNum(346326)
    
if __name__ == '__main__':
    main()
