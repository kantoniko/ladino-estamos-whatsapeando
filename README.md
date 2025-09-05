# Estamos Whatsapeando

See the content of [Estamos Whatsapeando](https://kantoniko.com/)

Copyright of the sound and text files: Albert Israel 2023

Copyright of the code: Gabor Szabo 2023

License: [Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/)


## GitHub pages

The root directory of this project is published as "GitHub pages" on the URL https://whatsapeando.kantoniko.com
The WhatsApp pages will use the ogg and jpeg files hosted on this URL.

## Adding entry

```
git clone git@github.com:kantoniko/ladino-estamos-whatsapeando.git
git@github.com:kantoniko/ladino-diksionaryo-code.git
```

Installing Python requirements

```
pip install -r ../ladino-diksionaryo-code/requirements.txt
```

The following command will check the entries:

```
./check.sh
```

or:

```
python ../ladino-diksionaryo-code/ladino/whatsapeando.py .
```

Successful result will look like this:

```
All read properly.
Last published:   2023.05.14 - Akel tyempo - Musa Moiz Eskenazi 15
Today is          2023.01.05
```

The "Last published" started out as a real date, but now it is just counter. New messages should be published with dates after the "Last published". As Albert does not publish every day, after a few months we'll catch up and we'll be able to use the same date as the original post.


* Vist the page in the archive of Ladinokomunita: [topic](https://ladinokomunita.groups.io/g/main/topics) and find the post by Albert. For example [this post](https://ladinokomunita.groups.io/g/main/message/68773)
* Copy `skeleton.yaml` to `text/` basing the name of the file on the title. We prefer the version where each line has its own translation.
    The single `text` entry was for the messages where we did not have the Hebrew translation as they were sent before I joined the WhatsApp group.
```
teksto:
  - ladino:
    ebreo:
  - ladino:
    ebreo:
```
* Copy the text from the WhatsApp message.
* Right-click "save image as" them nove that image to  `img/` using the same filename as the `.yaml` file, but with `.jpeg` extension.
* Right-click on the .ogg file and "Save link as". Move the .ogg file to `sound/`   with the same name and `.ogg` extension.


## Merging sound files

Sometimes the sound is split into two files. This can merge them:

```
opusdec a.ogg a.wav
opusdec b.ogg b.wav
sox a.wav b.wav c.ogg
```




