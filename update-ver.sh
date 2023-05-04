#!/bin/bash


currVer=$(curl -X 'GET' -H 'accept: application/json' 'https://releases.revanced.app/patches' | \
jq -r '.[] | .compatiblePackages| .[] | select(.name=="com.google.android.youtube") | .versions | .[-1] | select( . != null )' | \
sort | uniq | head -1)
now=$(date -u +"%Y-%m-%dT%H:%M")
nowUnix=$(date +%s)

oldVer=$(cut -f1 -d '@' .conf/version)
lastUpdate=$(cut -f2 -d '@' .conf/version | cut -f1 -d '/')
lastUnix=$(cut -f2 -d '/' .conf/version)

rebuild=false

if [ "$oldVer" != "$currVer" ]; then
    # update all md files
    echo "Update version from $oldVer to $currVer"
    find ./ -type f -name "*.md" -exec sed -i "s/$oldVer/$currVer/g" "{}" \;

    echo "Update last update timestamp from $lastUpdate to $now"
    find ./ -type f -name "*.md" -exec sed -i "s/$lastUpdate/$now/g" "{}" \;

    # set local copy
    echo "$currVer"'@'"$now"'/'"$nowUnix" > .conf/version
    rebuild=true
fi

lessThanOneDay=86000

if [ "$(($nowUnix-$lastUnix))" -gt "$lessThanOneDay" ]; then
# not modified within 1 day, change last checked time anyway
    echo "Update last update timestamp from $lastUpdate to $now"
    find ./ -type f -name "*.md" -exec sed -i "s/$lastUpdate/$now/g" "{}" \;
    echo "$currVer"'@'"$now"'/'"$nowUnix" > .conf/version
    echo "bump=true" >> "$GITHUB_OUTPUT"
    rebuild=true
else
    echo "bump=false" >> "$GITHUB_OUTPUT"
fi

if [ $rebuild = true ]; then
    echo "rebuild=true" >> "$GITHUB_OUTPUT"
else
    echo "rebuild=false" >> "$GITHUB_OUTPUT"
fi