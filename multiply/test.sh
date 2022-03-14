

i=1
for eachFile in *.json; do
	
    tr -d '\n\r' < multiply$i.json |  jq -r '.[] | [.id, .user_id, .text, .classifier, .classification] | @csv' > extract-$i.csv
    echo "converted $i of many json files..."
    ((i=i+1))
done

i=1
for eachFile in *.csv; do
    cat extract-$i.csv >> concatenate.csv
    ((i=i+1))
done
