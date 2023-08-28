#!/bin/bash

# TODO: fix get curr ver method by extracting from Git repo instead of api

#currVer=$(curl --no-progress-meter -X 'GET' -H 'accept: application/json' 'https://releases.revanced.app/patches' |
#    jq -r '.[] | .compatiblePackages| .[] | select(.name=="com.google.android.youtube") | .versions | .[-1] | select( . != null )' |
#    sort | uniq | head -1)
currVer='18.32.39'
now=$(date -u +"%Y-%m-%dT%H:%M")
nowUnix=$(date +%s)

oldVer=$(cut -f1 -d '@' .conf/version)
lastUpdate=$(cut -f2 -d '@' .conf/version | cut -f1 -d '/')
lastUnix=$(cut -f2 -d '/' .conf/version)

dashOld=$(echo "$oldVer" | tr '.' '-')
dashNew=$(echo "$currVer" | tr '.' '-')

if [[ "$GITHUB_ACTIONS" != "true" ]]; then
    echo 'running locally, set $GITHUB_OUTPUT to /dev/null'
    GITHUB_OUTPUT="/dev/null"
fi

if ! echo "${currVer}" | grep '[0-9]' >/dev/null; then
    echo "currVer $currVer is invalid, exiting with status code 1..."
    exit 1
fi

rebuild=false

if [[ "$oldVer" != "$currVer" ]]; then
    # update all md files
    echo "Update version from $oldVer to $currVer"
    # modify 03-get-file.md's link first
    find ./ -type f -name "*.md" -exec sed -i "s/$dashOld/$dashNew/g" "{}" \;

    find ./ -type f -name "*.md" -exec sed -i "s/$oldVer/$currVer/g" "{}" \;

    echo "Update last update timestamp from $lastUpdate to $now"
    find ./ -type f -name "*.md" -exec sed -i "s/$lastUpdate/$now/g" "{}" \;

    # set local copy
    echo "$currVer"'@'"$now"'/'"$nowUnix" >.conf/version
    rebuild=true

    # update badge
    echo "Version changed, update badge"
    curl --no-progress-meter -o ./step-by-step/02.png 'https://raster.shields.io/badge/Latest%20Supported%20Version-'"$currVer"'-ff0000.png?style=for-the-badge&logo=youtube'
else
    echo "Remote: $currVer   Local: $oldVer"
    echo "No need to change"
fi

echo "ver=$currVer" >>"$GITHUB_OUTPUT"

# 1 week
keepAliveTime=604800

if (( "$(($nowUnix - $lastUnix))" > "$keepAliveTime" )) || [[ "$EVENT" == 'workflow_dispatch' ]]; then
    if [[ "$EVENT" == 'workflow_dispatch' ]]; then
        echo "Updating timestamp forcefully because of manual dispatch"
    else
        echo "now: $nowUnix    last: $lastUnix"
        echo "diff: $(($nowUnix - $lastUnix)) > $keepAliveTime"
    fi
    # not modified within 1 week, change last checked time anyway to show that we are alive
    echo "Update last update timestamp from $lastUpdate to $now"
    find ./ -type f -name "*.md" -exec sed -i "s/$lastUpdate/$now/g" "{}" \;
    echo "$currVer"'@'"$now"'/'"$nowUnix" >.conf/version
    echo "bump=true" >>"$GITHUB_OUTPUT"
    echo "bump=true"
    rebuild=true
else
    echo "no need to update last update timestamp"
    echo "bump=false" >>"$GITHUB_OUTPUT"
    echo "bump=false"
fi

if [ "$rebuild" = true ]; then
    echo "rebuild=true" >>"$GITHUB_OUTPUT"
    echo "rebuild=true"
else
    echo "rebuild=false" >>"$GITHUB_OUTPUT"
    echo "rebuild=false"
fi
