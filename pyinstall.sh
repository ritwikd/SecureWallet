curl -o	http://online.ritwikd.com/ritwik/securewallet/raw/master/securewallet.py securewallet.py
echo "Finished download."
mv securewallet.py /usr/bin/securewallet.py
echo "Moved file to /usr/bin."
echo 'securewallet = "python /usr/bin/securewallet.py"' >> ~/.bash_profile
echo 'securewallet = "python /usr/bin/securewallet.py"' >> ~/.bashrc
echo "Added the aliases."