str = '2019-02-12 00:43:45,536 - ie_serving.server.service - DEBUG - PREDICT; input deserialization completed; rotatechestfrontalv2model_ie; 1; 0.194ms'
import re
import sys
import csv
input_deserialization_completed = "(?i)input\s+deserialization\s+completed\s(.*)\s+ms"
idc = ((input_deserialization_completed.split(';'))[-1])
def process_log(logfilename):
    parse_list = []
    with open(logfilename, "r")as logfile:
        logfile_lines = logfile.readlines()
    for log_line in logfile_lines:
        line =log_line.strip()
        in_des_comp = re.findall(idc, line)
        if in_des_comp:
            parse_dict = {}
            parse_dict['in_des_comp'] = idc[0]
            parse_list.append(parse_dict)
    return parse_list

if __name__=="__main__":
    parsed_result = process_log(sys.argv[1])
    with open("parsed_result.csv", 'w')as csvfile:
        fieldnames = ['inp_des_comp']
        writer =csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(parsed_result)

logfile = '/Users/mohanpraveenhazaru/Documents/alg/text.txt'
with open(logfile, 'r') as logfiler:
    logfilelines = logfiler.readlines()
    for log_line in logfilelines:
        line = log_line.split(';')[-1]
        print line
