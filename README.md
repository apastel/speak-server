## About

Click this image to see a video demonstration.  
[![Click me](https://img.youtube.com/vi/KADqW056f9k/3.jpg)](https://www.youtube.com/watch?v=KADqW056f9k)

[The website](https://www.speaktomenow.tk/) created from this code allows a visitor to type in a string of text. That text gets sent to a back-end Flask server running on a [Raspberry Pi](https://www.raspberrypi.org/) computer with a [Sense-HAT ](https://www.raspberrypi.org/blog/sense-hat-projects/) attached. That Raspberry Pi computer is in my bedroom. The text is displayed on the LEDs of the HAT sensor, and at the same time it is translated to audio and spoken out loud on an attached speaker. It provides a funny and terrifying way for the public to interact with me and invade my personal life.

All text is logged to the server so that I may view it later if I missed it. No identifying information is collected or logged. Steps were taken to lock down the Raspberry Pi server itself from intruders.

Guides used:
* [How To Serve Flask Applications with uWSGI and Nginx on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)
* [How to Deploy a React + Flask Project](https://blog.miguelgrinberg.com/post/how-to-deploy-a-react--flask-project)

For security lockdown: [Initial Server Setup with Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04)

Which I turned into an Ansible project for automation: https://github.com/apastel/rpi-ansible

## Technologies used
* [Microsoft Web Template Studio](https://github.com/Microsoft/WebTemplateStudio)
* Python
* [Google Text-to-Speech](https://gtts.readthedocs.io/en/latest/) (Python module)
* [React](https://reactjs.org/)
* [Gunicorn](https://gunicorn.org/)