sudo curl http://online.ritwikd.com/ritwik/securewallet/raw/master/securewallet -o securewallet
echo "Finished download."
mv securewallet /usr/bin/securewallet
echo "Moved file to /usr/bin."
sudo echo 'export PATH=$PATH:/usr/local/sbin:/usr/local/bin' >> ~/.bash_profile
sudo echo 'export PATH=$PATH:/usr/local/sbin:/usr/local/bin' >> ~/.bashrc
sudo echo 'export PATH=$PATH:/usr/local/sbin:/usr/local/bin' >> ~/.zshrc
sudo chmod +x /usr/bin/securewallet
export PATH=$PATH:/usr/local/sbin:/usr/local/bin
echo "Added the aliases. Please reopen shell."