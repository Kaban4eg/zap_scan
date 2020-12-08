import json
import sys
#f1=""
#f2=""
# f1="D:\\zap_report\\admin.beta.json" #standart
# f2="D:\\zap_report\\new.admin.beta.json" #new scan

def findalert(file,siteurl,url):
    with open(file) as json_file:
        data = json.load(json_file)
        for site in data['site']:
            if site['@name']==siteurl:
                for alert in site['alerts']:
                    if alert['riskdesc'].find('Informational'):
                        # print(alert['riskdesc'])
                        #if alert['cweid'] == cwe:
                            for inst in alert['instances']:
                                if inst['uri'] == url:
                                    status = 1
                                    return status
                                else:
                                    status = 0
    return status


def main():

    #for param in sys.argv:
    f1=sys.argv[1]
    f2=sys.argv[2]
    #f1="D:\\zap_report\\ino.json" #standart
    #f2="D:\\zap_report\\new.ino.json" #new scan

    with open(f2) as json_file:
        data = json.load(json_file)
        #print(data['site'][1]['alerts'])
        for site in data['site']:
            #print(site)
            for alert in site['alerts']:
                #print(alert)
                if (alert['riskdesc'].find('Informational')):
                    #print(alert['riskdesc'])
                    for inst in alert['instances']:
                        #print(inst)
                        #al = findalert(f1, site['@name'],alert['cweid'], inst['uri'])
                        al = findalert(f1, site['@name'], inst['uri'])
                        #al=1
                        if al == 0:
                            print(inst['method'] + ' : ' + alert['riskdesc']+ ' : ' + inst['uri'] )



if __name__ == '__main__':
    main()

