import json
import sys

def jsontomas(file):
    with open(file) as json_file:
        data = json.load(json_file)
        new=[]
        for site in data['site']:
            for alert in site['alerts']:
                if "Informational (" not in alert['riskdesc'] and ("Low (" not in alert['riskdesc']):
                    for inst in alert['instances']:
                        new.append("site:"+site['@name']+";alertlevel:"+alert['riskdesc']+";url:"+inst['uri']+";cweid:"+alert['cweid'])
    return new

def main():
    f1=sys.argv[1]
    f2=sys.argv[2]
    for alert in jsontomas(f2):
        if alert not in jsontomas(f1):
                print(alert)

if __name__ == '__main__':
    main()

