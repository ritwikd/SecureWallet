sudo curl http://online.ritwikd.com/ritwik/securewallet/raw/master/securewallet -o /usr/bin/securewallet
echo "Finished download."
sudo echo 'export PATH=$PATH:/usr/local/sbin:/usr/local/bin' >> ~/.bash_profile
sudo echo 'export PATH=$PATH:/usr/local/sbin:/usr/local/bin' >> ~/.bashrc
sudo echo 'export PATH=$PATH:/usr/local/sbin:/usr/local/bin' >> ~/.zshrc
sudo chmod +x /usr/bin/securewallet
export PATH=$PATH:/usr/local/sbin:/usr/local/bin
echo "Added the aliases. Please reopen shell."