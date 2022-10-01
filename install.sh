systemctl stop suspend-hack.service
systemctl disable suspend-hack.service
cp suspend-hack.service /etc/systemd/system
cp suspend-hack.py /usr/local/src
systemctl daemon-reload
systemctl enable suspend-hack.service
systemctl start suspend-hack.service
