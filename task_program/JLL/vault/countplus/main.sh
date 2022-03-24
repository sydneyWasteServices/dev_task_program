i=0
while true; do
  if [[ "$i" -gt 3 ]]; then
       exit 1
  fi
  echo i: $i
  ((i++))
done



