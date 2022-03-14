i=1
for eachFile in *.json; do
    cat json-$i.json | jq -r '.[] | {column1: .path.to.data, column2: .path.to.data} | [.[] | tostring] | @csv' > extract-$i.csv
    echo "converted $i of many json files..."
    ((i=i+1))
done

i=1
for eachFile in *.csv; do
    cat extract-$i.csv >> concatenate.csv
    ((i=i+1))
done
