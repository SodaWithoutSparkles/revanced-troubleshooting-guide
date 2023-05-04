#!/bin/bash


currVer=$(curl -X 'GET' -H 'accept: application/json' 'https://releases.revanced.app/patches' | \
jq -r '.[] | .compatiblePackages| .[] | select(.name=="com.google.android.youtube") | .versions | .[-1] | select( . != null )' | \
sort | uniq | head -1)
now=$(date -u +"%Y-%m-%dT%H:%M")

oldVer=$(cut -f1 -d '@' .conf/version)
lastUpdate=$(cut -f2 -d '@' .conf/version)

if [ "$oldVer" != "$currVer" ]; then
    # update all md files
    echo "Update version from $oldVer to $currVer"
    find ./ -type f -name "*.md" -exec sed -i "s/$oldVer/$currVer/g" "{}" \;

    echo "Update last update timestamp from $lastUpdate to $now"
    find ./ -type f -name "*.md" -exec sed -i "s/$lastUpdate/$now/g" "{}" \;

    # set local copy
    echo "$currVer"'@'"$now" > .conf/version
fi

if [ $(find /path -mmin +1400 -type f -name ".conf/version" 2>/dev/null) ]; then
# not modified within 1 day, change last checked time anyway
    echo "Update last update timestamp from $oldVer to $currVer"
    find ./ -type f -name "*.md" -exec sed -i "s/$lastUpdate/$now/g" "{}" \;
    echo "$currVer"'@'"$now" > .conf/version
fi

