# Sylla Source
#### Online project repository and blog

This website is using the [Pelican static site generator](https://blog.getpelican.com/) with the [Attila Theme](https://github.com/arulrajnet/attila/tree/02dcad911ba1eb2d797a79ec008a810d89a2fde1). If you're interested in the mods I made to the theme checkout my [Attila fork.]()


**How to run in development**
Apply content and theme directory and start dev server. You have to run these commands each time you make a change to your theme or content (which is slightly annoying).
`pelican content -s pelicanconf.py -t ../attila`
`pelican -l`

**Quick Post Notes**
Local LAMP Stack development in a Debian Linux subsystem for Windows
1. Install a Debian based Linux distro from the Windows store.
2. Run the commands below.
```
sudo apt-get install apache2
sudo apt-get install php

sudo apt-get install wget
sudo apt-get install gnupg
sudo apt-get install lsb-release 

cd /tmp
wget https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb
sudo dpkg -i mysql-apt-config*
sudo apt update
sudo apt install mysql-server

# select MYSQL 8 and proceed to set root password

```


Super quick Windows MYSQL installation, I forget how to do this often.
1. Download MYSQL installer [64 bit MYSQL installer link](https://dev.mysql.com/downloads/file/?id=496745)
2. Include pics of your config.
3. Map exe path `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\MySQL\MySQL Server 8.0`