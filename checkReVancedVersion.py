#!/usr/bin/python3

import requests
import json
from datetime import datetime
from packaging import version
import os
import logging

JSON_FILE = '.conf/python/update.ver.json'
STATE_FILE = '.conf/python/update.state'  # for last update
# lookup table, pkgname to common name
LUT_FILE = '.conf/python/update.lut.json'
TEMPLATE_FILE = '.conf/python/update.template'
OUT_FILE = '05-versions.md'

if os.getenv('GITHUB_ACTIONS') != 'true':
    EXPORT = None
    if os.getenv('FORCE') != None:
        FORCED = True
    else:
        FORCED = False
else:
    EXPORT = os.getenv('GITHUB_OUTPUT')
    if os.getenv('EVENT') == 'workflow_dispatch':
        # manually run, force update
        FORCED = True
    else:
        FORCED = False

API = 'https://api.revanced.app/v2/patches/latest'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d: [%(levelname)s] %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

modified = False


def compVer(ver1: str, ver2: str):
    # 1 if ver1 > ver2
    # 0 if ver1 = ver2
    # -1 if ver1 < ver2
    # ANY should be ranked last
    # oh wait i know why
    # i am finding the LOWEST of the comp
    # so any should be ranked FIRST
    # print(ver1, ver2, end='')
    if (ver1 == ver2) and (ver1 == 'ANY'):
        return 0
    if ver1 == 'ANY':
        # print(ver1, ver2)
        return 1
    if ver2 == 'ANY':
        return 0
    try:
        # semantic version compare
        pver1 = version.parse(ver1)
        pver2 = version.parse(ver2)
        if pver1 > pver2:
            return 1
        elif pver1 < pver2:
            return -1
        return 0
    except:
        # strcmp
        if ver1 > ver2:
            return 1
        elif ver1 < ver2:
            return -1
        return 0


def findVer(versions: list):
    # Find Latest Supported Version (LSV)
    # input **SORTED** list of {'pkgName': pkgName, 'ver': LSV}
    # return list of {'pkgName': pkgName, 'ver': LSV, 'count': count} ...?

    # init 3 parallel arrays
    pkgName = []
    lsv = []
    patchCount = []

    curr = ''
    # checking if we hit another pkg, start a new entry in parallel arrays
    for item in versions:
        # new pkg?
        next = False
        if item['pkgName'] != curr:
            curr = item['pkgName']
            pkgName.append(curr)
            next = True
            patchCount.append(0)
            logging.debug(f'Found new pkgName {curr}')
        if next:
            lsv.append(item['ver'])
            logging.debug(f'Set {curr} version to {lsv[-1]}')
        patchCount[-1] += 1
        # if latest supported > current
        if compVer(lsv[-1], item['ver']) == 1:
            # change lsv to current
            logging.debug(
                f'Bump {curr} version from {lsv[-1]} to {item["ver"]}')
            lsv[-1] = item['ver']

    out = []
    for i, name in enumerate(pkgName):
        out.append({'pkgName': name, 'ver': lsv[i], 'count': patchCount[i]})

    return out


def getJson():
    # get json obj and save to JSON_PATH
    logging.info('Requesting API...')
    data = requests.get(API).json()
    with open(JSON_FILE, 'w') as f:
        json.dump(data, f)
    return


def parseJson():
    # return list of sorted {'pkgName': pkgName, 'ver': maxVer}, extracted from json
    # note: this rely on API to ensure the maxVer is ordered last
    logging.info('Parsing response...')
    rawJson = ''
    with open(JSON_FILE, 'r') as f:
        rawJson = json.loads(f.read())['patches']
    out = []
    for item in rawJson:
        try:
            try:
                # TODO: parse and get max semantic ver, fail to string comp
                maxVer = item['compatiblePackages'][0]['versions'][-1]
            except:
                # support all versions
                maxVer = 'ANY'
            pkgName = item['compatiblePackages'][0]['name']
            out.append({'pkgName': pkgName, 'ver': maxVer})
        except IndexError:
            # universal patches w/o pkgName or ver
            # ignore them
            pass
        except Exception as e:
            logging.critical(e)

    return sorted(out, key=lambda d: d['pkgName'])


def fillTemplate(lsv: list):
    logging.info('Filling template...')
    rawJson = ''
    table = []
    with open(LUT_FILE, 'r') as f:
        rawJson = json.loads(f.read())
    table.append('| Common Name | Version | Package Name |\n')
    table.append('|---|---|---|\n')
    for item in lsv:
        # Handle common name column
        try:
            commonName = rawJson[item['pkgName']][0]
        except KeyError:
            commonName = '_unknown_'
            logging.warning(
                f'Unable to find common name for {item["pkgName"]}, using _unknown_ instead'
            )
        except Exception as e:
            logging.critical(e)
        # Handle version override
        try:
            versionToUse = rawJson[item['pkgName']][1]
            logging.warning(
                f"Version override for {item['pkgName']} to {versionToUse}"
            )
            versionToUse += ' [^1]'
        except IndexError:
            versionToUse = item['ver']
        except Exception as e:
            print(e)
            logging.critical(e)

        table.append(
            f"| {commonName} | {versionToUse} | {item['pkgName']} |\n")

    with open(TEMPLATE_FILE, "r") as t:
        # contents = t.readlines()
        with open(OUT_FILE, 'w') as f:
            for line in t:
                if line == '{table}\n':
                    f.writelines(table)
                elif line == '{date}\n':
                    timestring = datetime.utcnow().isoformat(
                        sep=" ", timespec="seconds") + ' UTC'
                    logging.info(f'Set last update timestamp to {timestring}')
                    f.write(f'Last Update: {timestring}\n')
                elif line == '{footnote}\n':
                    f.write('[^1]: Version override is used')
                else:
                    f.write(line)


def exportOutput(key: str, value: str):
    # export the key:value pair to gh action output
    if EXPORT != None:
        print(f'{key}={value}', file=EXPORT)
    return


def main():
    global modified
    getJson()
    with open(STATE_FILE, 'r') as f:
        lastUpdated = int(f.readline())
        lastResult = f.readline()
    # lastUpdated = 1
    # lastResult = ''

    result = sorted(findVer(parseJson()),
                    key=lambda d: d['count'],
                    reverse=True)
    timeNow = int(datetime.utcnow().strftime('%s'))

    if str(result) != lastResult:
        modified = True
        logging.info('Patches info updated, modifing state file')

    # not modified within 1 week
    if (timeNow - lastUpdated) > 604800:
        logging.info('Last update over 1 week ago, bumping timestamp')
        modified = True

    if modified or FORCED:
        with open(STATE_FILE, 'w') as f:
            f.write(str(timeNow)+'\n')
            f.write(str(result))
        exportOutput('modified', 'true')
        logging.info(f'Need to update output, {modified=}, {FORCED=}')
        fillTemplate(result)
    else:
        exportOutput('modified', 'false')
        logging.info('No changes made, no need to update')
    logging.info('Done')


if __name__ == '__main__':
    main()
# print(json.dumps(result))

# findVer('com.google.android.youtube', )
