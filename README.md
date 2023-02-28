# Click Counter Program.     
This program is created to converting link into a bitlink  and returns the click counts for the specified link.
## Prerequisites:
*For successful script run you will need to get API token.*
+ Sign up here: [Bitly.com](https://bitly.com)
+ Once signed up, you need to generate API token from account settings.
  > API token looks like this (example): **775108fc43e1752bca27181d8094dac029fc4267**       
## Installing:
+ You should download the repository ClickCounter from *GitHub* to your device.
+ Install Python3 latest version.
   > To isolate the project, I'd recommend to use a virtual environment model. [vertualenv/venv](https://docs.python.org/3/library/venv.html)
## Preparing to run the script.
*Further, I'll show you how to run the program through the console (terminal). In my case it's zsh shell.*
+ Create a virtualenv:
```zch
% virtualenv counter
```
+ Activate the environment:
```zch
% source counter/bin/activate
```
+ Then use pip (or pip3, there is a conflict with Python2) to install the dependencies (use the requirements.txt file):
```zch
% python3 -m pip install -r requirements.txt
```
> *__Remark__: If you get an error, for example: "No such file or directory", then try to use full path to the requirements.txt file.*
+ Export your private API token by this command:
```zch
% export BITLY_TOKEN="write_your_token_here"
```
> *__Remark__: In this way, environment variable works only for the duration that shell is live. If you close the shell and restart it, you have to set environmental variable again. Python-dotenv prevents us from doing this repetitive work. For permanent set, create .env file and add variables in this format:*
> *BITLY_TOKEN = "write_your_token_here"* 
## Running the program.
*It's all set. Time to run the script.*
 ### ___Converting link into bitlink.___
For test run, try to convert this link: __*mail.ru*__:
```zch
% python3 main.py mail.ru
```
Output:
```zsh 
(counter) denischukchin@Deniss-Air counter % python3 main.py mail.ru
Битлинк: https://bit.ly/3HIH5Vq
```
>*__Remark__: If you get an error, for example: "No such file or directory", then try to use full path to the main file.*
### ___Click counts for the specified link.___
Let's count how many times someone get through the bitlink:
```zch
% python3 main.py https://bit.ly/3HIH5Vq
```
Output:
```zsh
(counter) denischukchin@Deniss-Air counter % python3 main.py https://bit.ly/3HIH5Vq
По вашей ссылке прошли: 10 раз(а)
```
>*__Remark__: If you get an error, for example: "No such file or directory", then try to use full path to the main file.*
## Project goal.
*The program was designed by a student from online web development courses for educational purposes [Devman](https://dvmn.org).*