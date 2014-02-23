sudo curl http://online.ritwikd.com/ritwik/securewallet/raw/master/securewallet -o securewallet
echo "Finished download."
mv securewallet /usr/bin/securewallet
echo "Moved file to /usr/bin."
sudo echo 'alias securewallet="./usr/bin/securewallet"' >> ~/.bash_profile
sudo echo 'alias securewallet="./usr/bin/securewallet"' >> ~/.bashrc
sudo echo 'alias securewallet="./usr/bin/securewallet"' >> ~/.zshrc
sudo echo 'sudo export PATH=$PATH:/usr/local/sbin:/usr/local/bin' >> ~/.bash_profile
sudo echo 'sudo export PATH=$PATH:/usr/local/sbin:/usr/local/bin' >> ~/.bashrc
sudo echo 'sudo export PATH=$PATH:/usr/local/sbin:/usr/local/bin' >> ~/.zshrc
sudo chmod +x /usr/bin/securewallet
export PATH=$PATH:/usr/local/sbin:/usr/local/bin
echo "Added the aliases. Please reopen shell."