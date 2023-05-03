
if [[ "$1" == *"revanced-troubleshooting-guide"* ]]; then
    cd "$1"
    dir=$(pwd)
    echo "Going to deleting $(dirname "$dir")/${PWD##*/}.md and rebuilding it from $dir 's content."
    read -p "Are you sure? " -n 1 -r
    echo    # (optional) move to a new line
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        rm -f ../${PWD##*/}.md
        for i in *.md; do
            cat -s "$i" >> ../${PWD##*/}.md;
            echo '' >> ../${PWD##*/}.md;
            echo -n '#' >> ../${PWD##*/}.md;
        done
        sed -i '/\S/,/^\s*$/!d' ../${PWD##*/}.md;
        truncate -s -1 ../${PWD##*/}.md
        sed -i '/\S/,/^\s*$/!d' ../${PWD##*/}.md;
    else
        echo 'abort'
    fi
else
    echo 'use full path'
fi
