pacman -S uwsgi uwsgi-plugin-python
python3 -m venv .venv
source .venv/bin/active
pip install django==2.2
./manage.py makemigrations
./manage.py migrate
copy rootfs / # https://github.com/akoidan/pychat/blob/master/download_content.sh
systemctl enable pychatApi
systemctl start pychatApi
