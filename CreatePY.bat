cd C:/myprojects/Aliases/CreateCommand
py CreatePythonProject.py %1
cd C:/myprojects/pythonprojects/%1
git init
git remote add origin https://github.com/KingOfJesters/%1.git
type nul >> README.txt
git add .
git commit -m "Initial commit"
git push -u origin master
code .