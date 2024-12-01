mkdir $1
cp -n base.py "${1}/${1}a.py"

SES=`cat ${HOME}/src/adventsession.txt`
curl https://adventofcode.com/2024/day/$1/input --cookie "session=${SES}" > "${1}/in.txt"
touch "${1}/s.txt"
