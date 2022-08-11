# Usage
1. Install requests lib `pip install requests`
2. Open `sites.txt` and write site. Only one site on line.
3. Run `python main.py`

# Settings
You can change check time here `time.sleep(10)`
```python
if __name__ == '__main__':
    while True:
        main()
        time.sleep(10)
 ```
 
 # Why?
This script checks the response code of each site in the `sites.txt` file every 10 seconds. If the response code is 200, then everything is fine, if there is another one, the script will let you know about it. Also, the time of checking the list of sites can be changed. In the future I plan to launch a script for telegrams and slack.

![](https://i.ibb.co/hyYshvp/Screenshot-2022-08-11-at-19-25-14.png)
