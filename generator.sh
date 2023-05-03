
if [[ "$1" == *"revanced-troubleshooting-guide"* ]]; then
    cd "$1"
    dir=$(pwd)
    echo "Going to deleting $(dirname "$dir")/${PWD##*/}.md and rebuilding it from $dir 's content."
    read -p "Are you sure? " -n 1 -r
    echo    # (optional) move to a new line
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo '' > ../${PWD##*/}.md && for i in *.md; do cat "$i" >> ../${PWD##*/}.md; echo -n '#' >> ../${PWD##*/}.md; done && truncate -s -1 ../${PWD##*/}.md
    else
        echo 'abort'
    fi
else
    echo 'use full path'
fi
