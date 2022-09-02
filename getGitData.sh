#!/bin/bash


BACKEND="/home/runner/work/kaoto.io/kaoto.io/tmp/kaoto-backend"
FRONTEND="/home/runner/work/kaoto.io/kaoto.io/tmp/kaoto-ui"

echo "Creating event per contributor!"
FOLDER="/home/runner/work/kaoto.io/kaoto.io/"
cd $BACKEND
git shortlog -s --no-merges main > $FOLDER"/contributors.txt"
cd $FRONTEND
git shortlog -s --no-merges main >> $FOLDER"/contributors.txt"
echo "Found the following contributors"
cat $FOLDER"/contributors.txt"
CONTRIBUTORS=0
while IFS= read -r line 
do
  cd $BACKEND
  DATE1=$(git log --author="${line:7}" --reverse --format=%ci | head -n 1)
  DATE1=${DATE1:0:10}
  cd $FRONTEND
  DATE2=$(git log --author="${line:7}" --reverse --format=%ci | head -n 1)
  DATE2=${DATE2:0:10}
  FILE=${line:7}
  FILENAME=$FOLDER"/content/timeline/generated-contributor-${FILE// /-}.md"
  echo "---" > "$FILENAME"
  echo "title: ${line:7} " >> "$FILENAME"
  echo "draft: false" >> "$FILENAME"
  echo "type: timeline" >> "$FILENAME"
  
  echo "Contributor: ${line:7} '$DATE1' '$DATE2'"
  if [ "$DATE2" == "" ]  && [ "$DATE1" == "" ]; then
    rm "$FILENAME"
  elif [ "$DATE1" != "" ] && ([ "$DATE1" \< "$DATE2" ] || [ "$DATE2" == "" ]); then
    echo "date: $DATE1" >> "$FILENAME"
    echo "---" >> "$FILENAME"
    echo "${line:7} made their first commit on Kaoto!\n" >> "$FILENAME"
    echo "Now we have "$((++CONTRIBUTORS))" in Kaoto." >> "$FILENAME"
  else
    echo "date: $DATE2" >> "$FILENAME"
    echo "---" >> "$FILENAME"
    echo "${line:7} made their first commit on Kaoto!" >> "$FILENAME"
    echo "Now we have "$((++CONTRIBUTORS))" in Kaoto." >> "$FILENAME"
  fi
done < $FOLDER"/contributors.txt"


echo "Remove bots"
rm $FOLDER/content/timeline/generated-contributor-*-Bot.md
rm $FOLDER/content/timeline/generated-contributor-*-bot.md
  

