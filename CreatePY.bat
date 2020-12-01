cd C:/path/to/AutomatePythonProjects
py CreatePythonProject.py %1
cd C:/path/to/projects/%1
git init
git remote add origin https://github.com/<username>/%1.git
type nul >> README.txt
git add .
git commit -m "Initial commit"
git push -u origin master
code .
