This project was made as an exercise for the Cloud Computing for Analytics subject, taught in the High Performance Data Analytics course offered by CY-TECH

The goal of this project is to learn to use docker and create a semi complex infrastructure for an app. 
I chose to create a simple front end that hosts a text field, and via php sends an api call to the back end of the app to generate
a small poem through this model : https://huggingface.co/ismaelfaro/gpt2-poems.en

It uses a docker compose to organises the service into the website and the poetry generator into separate container, they communicate through api calls.

The base image for the back end is a pytorch 13 image wich is 5gb so it is quite heavy.
The poem generation can also be quite slow, and doesn't handle scentences very well. 