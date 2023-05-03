sed -i 's/##/£#/g' *.md

csplit *.md --suffix-format="%02d.md" --prefix="" /^£.*/ {*}

sed -i 's/£#/#/g' *.md

rm merged.md && \
for i in *.md; do cat "$i" >> merged.md; echo -n '#' >> merged.md; done && \
truncate -s -1 merged.md
