# Straw

Extract images and other streams from PDF files 🐍.


## Introduction

This library is dedicated to implementing extraction procedures for binary streams in PDF files. Currently this only includes images, however we hope to expand to other streams, and indeed other file formats.


## Installation

```sh
$ pip install straw
```


## API

```py
>>> import straw

>>> images = straw.extract_images('./file.pdf')
```

The `extract_images` method returns an array of image instances, each having a `data` attribute which holds the raw binary data of the image. The image can be saved to disk by simply writing this data to a file. 


## Future

* Pillow integration
* Support for stream formats other than images
* Support for other file formats with embedded streams.
