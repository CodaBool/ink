# Requirements
- create a `/data/count.txt`, `/data/release_count.txt` and a `/key.json` file to run
- use `just run` and VS Code live server to display the index.html file
- set the browser resolution to 800px by 480px

# Install
## cron 

```
*/15 * * * * cd /home/codabool/ink/ && cron_script.sh
0 * * * * cd /home/codabool/ink && git pull
```


## install firefox

`sudo apt install snapd`
`sudo snap install firefox`

## ssh server

`sudo apt install openssh-server`

`sudo systemctl enable ssh && sudo systemctl start ssh`

## ink

[guide](https://core-electronics.com.au/guides/raspberry-pi/colour-e-ink-display-raspberry-pi/)

`sudo apt-get install python3-smbus i2c-tools`

Menu -> Preferences -> Raspberry Pi Configuration, then under the ‘Interfaces’ tab, select I2C and SPI as ‘enabled’

`i2cdetect -y 1`

if you get a file issue. You might be necessary to reboot `sudo reboot`