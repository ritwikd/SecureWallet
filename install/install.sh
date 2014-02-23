sudo curl http://online.ritwikd.com/ritwik/securewallet/raw/master/securewallet -o securewallet
echo "Finished download."
mv securewallet /usr/bin/securewallet
echo "Moved file to /usr/bin."
echo 'alias securewallet="./usr/bin/securewallet"' >> ~/.bash_profile
echo 'alias securewallet="./usr/bin/securewallet"' >> ~/.bashrc
echo 'alias securewallet="./usr/bin/securewallet"' >> ~/.zshrc
echo "Added the aliases. Please reopen shell."