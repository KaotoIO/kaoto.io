#!/bin/bash

BACKEND="/home/runner/work/kaoto.io/kaoto.io/tmp/kaoto-backend"
FRONTEND="/home/runner/work/kaoto.io/kaoto.io/tmp/kaoto-ui"
KAOTO_NEXT="/home/runner/work/kaoto.io/kaoto.io/tmp/kaoto-next"
KAOTO_VSCODE="/home/runner/work/kaoto.io/kaoto.io/tmp/vscode-kaoto"

echo "Creating event per contributor!"
FOLDER="/home/runner/work/kaoto.io/kaoto.io"

cd $BACKEND
git shortlog -s --no-merges main > $FOLDER"/contributors.txt"
cd $FRONTEND
git shortlog -s --no-merges main >> $FOLDER"/contributors.txt"
cd $KAOTO_NEXT
git shortlog -s --no-merges main >> $FOLDER"/contributors.txt"
cd $KAOTO_VSCODE
git shortlog -s --no-merges main >> $FOLDER"/contributors.txt"
echo "Found the following contributors"
cat $FOLDER"/contributors.txt"
CONTRIBUTORS=0
while IFS= read -r line 
do
  CONTRIBUTORS=$(($CONTRIBUTORS + 1))
  cd $BACKEND
  DATE1=$(git log --author="${line:7}" --reverse --format=%ci | head -n 1)
  DATE1=${DATE1:0:10}
  cd $FRONTEND
  DATE2=$(git log --author="${line:7}" --reverse --format=%ci | head -n 1)
  DATE2=${DATE2:0:10}
  cd $KAOTO_NEXT
  DATE3=$(git log --author="${line:7}" --reverse --format=%ci | head -n 1)
  DATE3=${DATE3:0:10}
  cd $KAOTO_VSCODE
  DATE4=$(git log --author="${line:7}" --reverse --format=%ci | head -n 1)
  DATE4=${DATE4:0:10}
  FILE=${line:7}
  FILENAME=$FOLDER"/content/timeline/generated-contributor-${FILE// /-}.md"
  echo "---" > "$FILENAME"
  echo "title: \"${line:7}\" " >> "$FILENAME"
  echo "draft: false" >> "$FILENAME"
  echo "type: \"timeline\"" >> "$FILENAME"
  echo "Contributor: ${line:7} '$DATE1' '$DATE2' '$DATE3' '$DATE4'"
  
  sorted=()
  sorted+=("$DATE1")
  sorted+=("$DATE2")
  sorted+=("$DATE3")
  sorted+=("$DATE4")
  min=${sorted[0]}
  for i in "${sorted[@]}"; do
    if [ "$min" == "" ]; then
        min=$i;
    elif [ "$i" != "" ] && [ "$i" \< $min ]; then
        min=$i;
    fi
  done
  echo "date: \"$min\"" >> "$FILENAME"
  echo "---" >> "$FILENAME"
  echo "${line:7} made their first commit on Kaoto!" >> "$FILENAME"
done < $FOLDER"/contributors.txt"

echo "Remove bots"
rm $FOLDER/content/timeline/generated-contributor-*-Bot.md
rm $FOLDER/content/timeline/generated-contributor-*-bot.md
rm $FOLDER/content/timeline/generated-contributor-*\[bot\].md
