# Estamos Whatsapeando

See the content of [Estamos Whatsapeando](https://kantoniko.com/)

Copyright of the sound and text files: Albert Israel 2023

Copyright of the code: Gabor Szabo 2023

License: [Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/)


## Adding entry

Installing Python requirements

```
pip install -r requirements.txt
```

The following command will check the entries:

```
python ladino/whatsapeando.py
```

Successful result will look like this:

```
All read properly.
Last published:   2023.05.14 - Akel tyempo - Musa Moiz Eskenazi 15
Today is          2023.01.05
```

The "Last published" started out as a real date, but now it is just counter. New messages should be published with dates after the "Last published". As Albert does not publish every day, after a few months we'll catch up and we'll be able to use the same date as the original post.


* Vist the page in the archive of Ladinokomunita: [page](https://ladinokomunita.groups.io/g/main/message/68773)
* Copy `skeleton.yaml` to `text/` basing the name of the file on the title.
* Right-clkick "save image as" them nove that image to  `img/` using the same filename as the `.yaml` file, but with `.jpeg` extension.
* Right-click on the .ogg file and "Save link as". Move the .ogg file to `sound/`   with the same name and `.ogg` extension.


## Merging sound files

Sometimes the sound is split into two files. This can merge them:

```
opusdec a.ogg a.wav
opusdec b.ogg b.wav
sox a.wav b.wav c.ogg
```




