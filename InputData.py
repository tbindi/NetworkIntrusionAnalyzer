import csv
import numpy as np


target_names = {"back": 2, "buffer_overflow": 3, "ftp_write": 4,
                "guess_passwd": 4, "imap": 4,
                "ipsweep": 1, "land": 2, "loadmodule": 3, "multihop": 4,
                "neptune": 2, "nmap": 1,
                "normal": 0, "perl": 3, "phf": 4, "pod": 2, "portsweep": 1,
                "rootkit": 3, "satan": 1,
                "smurf": 2, "spy": 4, "teardrop": 2, "warezclient": 4,
                "warezmaster": 4, "apache2": 2,"httptunnel": 4,"mailbomb": 2,
                "mscan": 1,"named": 4,"processtable": 2,"ps": 3,"rootkit": 3,
                "saint": 1, "sendmail": 4, "snmpgetattack": 4, "snmpguess":
                    4, "sqlattack": 3, "udpstorm": 2, "worm": 4, "xlock": 4,
                "xsnoop": 4, "xterm": 3}


def get_test(filename):
    with open(filename, "rb") as f:
        test_data = list()
        test_target = list()
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            test_data.append(np.asarray(line[:-1], dtype=np.float))
            # temp = np.array([0, 0, 0, 0, 0])
            # temp[target_names[line[-1]]] = 1
            # test_target.append(np.asarray(temp))
            test_target.append(target_names[line[-1]])
    return test_data, test_target


def int_or_float(a):
    try:
        return int(a)
    except ValueError:
        return float(a)


def get_plain_text(filename):
    with open(filename, "rb") as f:
        data = list()
        target = list()
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            data.append(np.asarray(line[:-1], dtype=np.float))
            # target.append(np.asarray(target_names[line[-1]], dtype=np.int))
            temp = np.array([0, 0, 0, 0, 0])
            temp[target_names[line[-1]]] = 1
            target.append(np.asarray(temp))
            # target.append(target_names[line[-1]])
    return data, target


def get_plain(filename):
    with open(filename, "rb") as f:
        data = list()
        target = list()
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            data.append(np.asarray(line[:-1], dtype=np.float))
            # target.append(np.asarray(target_names[line[-1]], dtype=np.int))
            # temp = np.array([0, 0, 0, 0, 0])
            # temp[target_names[line[-1]]] = 1
            # target.append(np.asarray(temp))
            target.append(target_names[line[-1]])
    return data, target


def get_data(filename):
    data = list()
    with open(filename, "rb") as f:
        reader = csv.reader(f, delimiter=",")
        for i, line in enumerate(reader):
            data.append(line)
    for line in data:
        for i, value in enumerate(line):
            if i == 0 or 4 <= i <= 40:
                line[i] = int_or_float(value)
            elif i == 41:
                line[i] = line[i].replace('.', '')
    for i, line in enumerate(data):
        if line[1] == 'tcp':
            data[i] = line[:1] + list([1, 0, 0]) + line[2:]
        elif line[1] == 'udp':
            data[i] = line[:1] + list([0, 1, 0]) + line[2:]
        elif line[1] == 'icmp':
            data[i] = line[:1] + list([0, 0, 1]) + line[2:]
        else:
            data[i] = line[:1] + list([0, 0, 0]) + line[2:]

        if line[3] == 'REJ':
            data[i] = data[i][:4] + list([1, 0, 0, 0]) + data[i][6:]
        elif line[3] == 'S0' or line[3] == 'S1' or line[3] == 'S2' or line[3]\
                == 'S3' or line[3] == 'S4' or line[3] == 'SS':
            data[i] = data[i][:4] + list([0, 1, 0, 0]) + data[i][6:]
        elif line[3] == 'SF':
            data[i] = data[i][:4] + list([0, 0, 1, 0]) + data[i][6:]
        elif line[3] == 'RSTO' or line[3] == 'RSTOSO' or line[3] == 'RSTR':
            data[i] = data[i][:4] + list([0, 0, 0, 1]) + data[i][6:]
        else:
            data[i] = data[i][:4] + list([0, 0, 0, 0]) + data[i][6:]
    return data


if __name__ == "__main__":
    data = get_data('../corrected')
    f = open('../corrected.out.2', 'wb')
    for i in data:
        f.write(','.join(str(j) for j in i))
        f.write('\n')
