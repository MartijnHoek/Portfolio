# VIN decoding website
The goal of this project was designing and maintaining a website
on which vehicle VINs can be decoded and have a basic database with some information about the vehicles. 

If you are interested the website can be found [here](https://vintrospect.com/).


## Goals
Before this project I had no prior experience with setting up a website
or programming in HTML, PHP or JavaScript and only worked a little bit with APIs.

My goal was to develop a basic understanding of these programming languages and get
an insight if I would enjoy this kind of work. 

## Reflection

**Backend**

This project has learned me alot. The early versions of had alot of duplicate code for each manufacturer or even model.
Which made small changes to an API response require alot of files to be changed. 

Because of this I tried to make the code more object based and make more use of inheritance but still have flexibility for
custom solutions.

There are still some things that I'm not 100% happy with like the use of imports.
Another improvement or something that I think would be an improvement is not using a database to store some
(or all) of the data and only use Python for logic.

**Frontend**

I didn't have any prior experience with frontend development, because of this I struggled alot at the beginning with
choosing between languages and design layouts. 

I started the project with PHP but switched over halfway to HTML and JavaScript because I couldn't get something to work 
in PHP. 

With both languages I still have a long way to go, but I gave me a better understanding about how a website functions.

I think that a major improvement would be to implement most of the data in a database and have a script that is able to 
generate the HTML files with this data. This would create a "one truth" between the backend and frontend and decrease
development time when adding new supported models. 

## Project structure
In this portfolio repository I'm sharing partial code snippets from this project.

```
Portfolio
└─ Projects
    └─ VinDecodingWebsite
        ├─ Backend
        |   ├─ VinDecoder (VIN decoder logic)
        |   |   ├─ Core (Generic objects and a handler for decoding)
        |   |   └─ ManufacturerSpecific (Manufacturer specific objects and classes)
        |   |       ├─ ManufacturerSpecificModelHandlers
        |   |       ├─ ModelDefinitions
        |   |       └─ VinDecoders
        |   ├─ app (Management of the Flask API)
        |   |   ├─ decoder
        |   |   ├─ __init__.py
        |   |   ├─ config.py
        |   |   └─ routes.py
        |   └─ wsgi.py
        └─ Frontend
            ├─ components
            ├─ data
            ├─ js
            ├─ pages
            |   ├─ assembly-plant
            |   ├─ engine
            |   ├─ model
            |   ├─ platform
            |   ├─ contact.html
            |   ├─ decoding-results.html
            |   └─ vehicle-information.html
            ├─ index.html    
            └─ style.css

```