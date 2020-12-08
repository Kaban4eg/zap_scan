import sys
#from deepdiff import DeepDiff
import jsondiff
import json

def main():
    f1=sys.argv[1]
    f2=sys.argv[2]
    #f1 = "D:\\zap_report\\ino.json"  # standart
    #f2 = "D:\\zap_report\\new.ino.json"  # new scan
    with open(f1) as json_file:
        data1 = json.load(json_file)
        #data1 = json_file.read().replace('\\', '/')

    with open(f2) as json_file:
        data2 = json.load(json_file)
        #data2 = json_file.read().replace('\\', '/')
    #ddiff = DeepDiff(data1, data2, ignore_order=True)
    #print(ddiff)
    #for inst in ddiff['iterable_item_added']:
    #    print(ddiff['iterable_item_added'][inst]['uri'] + " : " + ddiff['iterable_item_added'][inst]['method'])
    ddiff=jsondiff.diff(data1,data2)

    for site in ddiff['site']:
        for i in ddiff['site'][site]:
            for alert in ddiff['site'][site][i]:
                for inst in ddiff['site'][site][i][alert]:
                    for ins in ddiff['site'][site][i][alert][inst]:
                        for j in ddiff['site'][site][i][alert][inst][ins]:
                            print(j)


if __name__ == '__main__':
    main()

