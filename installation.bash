cd 

sudo apt update && sudo apt upgrade -y

#UI installations

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.bashrc
nvm install node

pip install Flask
pip install Flask-Cors

#DM installations: