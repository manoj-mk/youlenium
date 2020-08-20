# Youtube subscription automation using Selenium 😎
### Motivation 🕵️‍♂️
Recently, I had created a new gmail account with cool id. So I wanted to transfer all my data to new account from old one.I was able to transfer files,passwords,bookmarks and other things.
But I couldn't find a way to transfer my subscribed channels. And hence decided to use my programming skills to solve the problem.

-----------
#### Follow the below steps to accomplish the task 👣
###### step-1 ⭐
- The first thing you need to do is to go to your old Youtube account and download subscribers xml file. [See Here](https://www.thewindowsclub.com/transfer-youtube-subscriptions-from-one-account-to-another)
- Convert xml file into json online. [Here](https://www.freeformatter.com/xml-to-json-converter.html) 

###### step-2 ⭐⭐
- Import that json file in python and extract channel ids from it.
- Create new file and add links to all channel in it. for example https:/ /youtube/channel/CHANNEL_ID 

###### step-3 ⭐⭐⭐
- Login into google account using selenium
- Go through each link stored in file from step-2;
- Click subscribe button with selenium
👏👏👏🎉
