sudo curl https://raw.githubusercontent.com/ritwikd/SecureWallet/master/securewallet.py -o securewallet.py
echo "Finished download."
mv securewallet.py /usr/bin/securewallet.py
echo "Moved file to /usr/bin."
echo 'alias securewallet="python /usr/bin/securewallet.py"' >> ~/.bash_profile
echo 'alias securewallet="python /usr/bin/securewallet.py"' >> ~/.bashrc
echo 'alias securewallet="python /usr/bin/securewallet.py"' >> ~/.zshrc
echo "Added the aliases. Please reopen shell."
