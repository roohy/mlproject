

def invited_info_loader(file_name):
    result = []
    with open(file_name,'r') as file:
        header = file.readline()
        first_len = 0
        second_len = 0
        counter = 0
        for line in file:
            item = (line[:-2]).split(',')
            '''if len(item)!= 3:
                print "error on ",counter
            if first_len == 0 :
                first_len = len(item[0])
            if second_len == 0:
                second_len = len(item[1])
            if first_len != len(item[0]):
                print "first error ",counter
            if second_len != len(item[1]):
                print "second error ",counter
            counter +=1'''
            result.append(item)
    print "invited --- ",result[-4:]
    print len(result)
    return result


def write_results(file_name,res):
    with open(file_name, 'w') as f:
        f.write("qid,uid,label\n")
        for item in res:
            #print type(item[0])
            f.write(str(item[0])+','+str(item[1])+','+str(item[2])+'\n')

def read_negs(file_name):
    result = []
    with open(file_name,'r') as file:
        for line in file:
            item = float(line[:-2])
            result.append(item)
    return result

def write_results2(file_name,res, an):
    with open(file_name, 'w') as f:
        f.write("qid,uid,label\n")
        print len(res)
        for i in range(len(res)):
            #print type(item[0])
            f.write(an[i][0]+','+an[i][1]+','+str(res[i])+'\n')

an = invited_info_loader("./bytecup2016data/validate_nolabel.txt")
res = read_negs("validate_result.txt")
write_results2('herhe.csv',res,an)

