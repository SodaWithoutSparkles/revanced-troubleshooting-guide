
cd ./troubleshoot/

for d in */ ; do
    cd "$d"
    dir=$(pwd)
    echo "Deleting $(dirname "$dir")/${PWD##*/}.md and rebuilding it from $dir 's content."
    rm -f ../${PWD##*/}.md
    for i in *.md; do
        cat -s "$i" >> ../${PWD##*/}.md;
        echo '' >> ../${PWD##*/}.md;
        echo -n '#' >> ../${PWD##*/}.md;
    done
    # remove extra new lines
    sed -i '/\S/,/^\s*$/!d' ../${PWD##*/}.md;
    # cut trailing '#'
    truncate -s -1 ../${PWD##*/}.md
    # remove new lines in case last command caused one
    sed -i '/\S/,/^\s*$/!d' ../${PWD##*/}.md;
    cd ..
done
