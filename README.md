# NOGACab-Raspberry
## How to install Raspbian OS on SD card with OS X
1. With `disk util`, find out which disk mounts the SD card.
    - ex) `dev/disk2`
2. Unmount the SD card with `unmountDisk /dev/disk[no. of disk]`.
3. Dump the image file with `sudo dd bs=4m if=[image file name].img 
of=/dev/rdisk*`. Watch out for the `rdisk*` not `disk*`. It takes about 5 
minuites, check the progress with <kbd>Ctl</kbd>+<kbd>T</kbd>.

## How to configure Raspbian OS
### Internet connection

#### 1. Wired LAN
1. Open configuration file with `sudo nano /etc/dhcpcd.conf`.
2. Uncomment the following lines:

        interface eth0
        static ip_address=[IP address]
        static routers=[Gateway]
        static domain_name_servers=[Gateway]8.8.8.8 ...

    and add `static netmask=[Netmask]` at the end of the uncommented block. Then
 `sudo reboot`.
 
#### 2. WIFI (Welcome_KAIST)
1. Open configuration file with `sudo nano 
/etc/wpa_supplicant/wpa_supplicant.conf`. 
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
3. `sudo reboot`

### Update `apt-get`
Update `apt-get` before any other package installation.

        sudo apt-get update
        sudo apt-get upgrade
      
### Configure ssh server
#### 1. Basic ssh configuration
Refer to [this blog](https://jimnong.tistory.com/713).
1. Check whether `openssh-server` is installed with `dpkg -l | grep openssh`.
 If not, install it with `sudo apt-get install openssh-server`.
2. Start ssh server service with `sudo service ssh start`
3. Check whether the service is working with `service --status-all | grep 
+`, and the port number with `sudo netstat -antp`. Normally, it occupies 
port 22.
#### 2. Run ssh on startup
Normally, service must be started automatically on startup. If it doesn't, 
let the starting script run on startup. Refer to [StackExchage](https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up).
