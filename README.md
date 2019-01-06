# NOGACab-Raspberry
## How to install Raspbian OS on SD card with OS X
1. With `$ disk util`, find out which disk mounts the SD card.
    - ex) `dev/disk2`
2. Unmount the SD card: <br> `$ unmountDisk /dev/disk[no. of disk]`
3. Dump the image file: <br> `$ sudo dd bs=4m if=[image file name].img 
of=/dev/rdisk*` <br> Watch out for the `rdisk*` not `disk*`. It takes about 5 
minuites, check the progress with <kbd>Ctl</kbd>+<kbd>T</kbd>.

## How to configure Raspbian OS
### Internet connection

#### 1. Wired LAN
1. Open configuration file: <br> `$ sudo nano /etc/dhcpcd.conf`
2. Uncomment the following lines:

        interface eth0
        static ip_address=[IP address]
        static routers=[Gateway]
        static domain_name_servers=[Gateway]8.8.8.8 ...

    and add `static netmask=[Netmask]` at the end of the uncommented block. Then
 `$ sudo reboot`.
 
#### 2. WIFI (Welcome_KAIST)
1. Open configuration file: <br> `$ sudo nano 
/etc/wpa_supplicant/wpa_supplicant.conf` 
2. Add the following lines at the end of the file.

    For Welcome_KAIST:

        network={
            ssid="Welcome_KAIST"
            priority=1
            proto=RSN
            key_mgmt=WPA-EAP
            pairwise=CCMP
            auth_alog=OPEN
            epa=PEAP
            identity="[your id]"
            password="[your password]"
            phase1="peaplable=0"
            pahse2="auth=MSCHAPV2"
        }
        
    For NOGACab-Raspberry:
        
        network={
            ssid="NOGACab-Raspberry"
            key_mgmt=NONE
            priotity=1
        }
3. `$ sudo reboot`

### Update `apt-get`
Update `apt-get` before any other package installation.

        $ sudo apt-get update
        $ sudo apt-get upgrade

### Configure iptime router
1. Allocate static internal IP address to Raspberry-pi: [link](http://studyforus.tistory.com/41).
2. Configure port forward: [link](http://studyforus.tistory.com/35).



### Configure ssh server
#### 1. Basic ssh configuration
Refer to [this blog](https://jimnong.tistory.com/713).
1. Check whether `openssh-server` is installed:<br> `$ dpkg -l | grep 
openssh`<br>
 If not, install it: <br>`$ sudo apt-get install openssh-server`
2. Start ssh server service: <br>`$ sudo service ssh start`
3. Check whether the service is working: <br> `$ service --status-all | grep 
+`<br>, and the port number: <br>`$ sudo netstat -antp`<br> Normally, it 
occupies 
port 22.
#### 2. Run ssh on startup
Normally, service must be started automatically on startup. If it doesn't, 
let the starting script run on startup. Refer to [StackExchage](https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up).
1. Make sure you are in the home directory: <br>`$ cd ~`
2. Create a starting script file: <br> `$ sudo nano /etc/init.d/[script name]`
3. Make the script executable: <br>`$ sudo chmod 755 /etc/init.d/[script 
name]`
4. Register script to be run at startup: <br> `$ sudo update-rc.d [scrip name] 
defaults`
5. Open `/etc/rc.loacal` and add `./etc/init.d/[script name]` at the end of 
the file.
6. `$ sudo reboot` and check whether ssh service started automatically.

### Install python3.6
Refer to [Github](https://gist.github.com/dschep/24aa61672a2092246eaca2824400d37f).
1. Install the required build-tools:

        $ sudo apt-get update
        $ sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
2. Download and install Python3.6:

        $ wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
        $ tar xf Python-3.6.5.tar.xz
        $ cd Python-3.6.5
        $ ./configure
        $ make
        $ sudo make altinstall
        
### Make a virtual environment
1. Clone the online git repository: <br>
`$ git clone https://github.com/SeungsuKim/NOGACab-Raspberry.git`
2. Change directory to the cloned repository: <br>
`$ cd NOGACab-Raspberry`
3. Check where python3.6 is located: <br>
`$ whereis python3.6`
4. Make new virtual environment with python3.6: <br>
`$ virtualenv --python=[path of python3.6] env_NOGACab-Raspberry`
5. Install every required packages: <br>
`$ sudo pip install -r requirements.txt`

If you want to apply the updates from online git repository after you cloned
 it,
1. Pull the changed files: <br>
`$ git pull origin master`
2. Install new required packages: <br>
`$ sudo pip install -r requirements.txt`
