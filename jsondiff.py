import sys
from deepdiff import DeepDiff
import json

def main():
    #f1=sys.argv[1]
    f2=sys.argv[2]
    #f1 = "D:\\zap_report\\ino.json"  # standart
    #f2 = "D:\\zap_report\\new.ino.json"  # new scan
    #with open(f1) as json_file:
    #    data1 = json.load(json_file)
    data1=sys.argv[1]
    with open(f2) as json_file:
        data2 = json.load(json_file)
    ddiff = DeepDiff(data1, data2, ignore_order=True)
    for inst in ddiff['iterable_item_added']:
        print(ddiff['iterable_item_added'][inst]['uri'] + " : " + ddiff['iterable_item_added'][inst]['method'])

if __name__ == '__main__':
    main()
