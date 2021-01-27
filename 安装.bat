git init 
git remote add origin https://github.com/apieceof2/maik.git
git fetch --all
git reset --hard origin/master
git pull origin master

pip install -r requirement.txt