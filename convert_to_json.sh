for f in ./data/*.webloc;
do
    filename=`basename "$f"`
    title="${filename%.*}"

    echo "Converting webloc to json - '$filename'"
    plutil -convert json "$f"

    echo "Rewrite '$filename' -> '$title.json'"
    jq -cr "{url: .URL,\"title\": \"$title\"}" "$f" > "./data/$title.json"

    echo
done
