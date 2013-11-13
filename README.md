# lpstats - Leanpub© Statistics Tool

[![Build Status](https://travis-ci.org/manuelkiessling/lpstats.png?branch=master)](https://travis-ci.org/manuelkiessling/lpstats)


## About

This is an early version of a web-based Leanpub© sales statistics viewer written
in Python.

It currently offers exactly one use case: Display a line graph of all the sales
a given Leanpub© book has generated per day, over a freely choosable time range.

![Screenshots](https://raw.github.com/manuelkiessling/lpstats/master/other/lpstats-0.0.1_screenshot_490x371.png)

It includes a very simple client for the Leanpub© API that is used to retrieve
the sales data for the book in question. Please log in to Leanpub© and go to
https://leanpub.com/dashboard/account in order to generate your API key.


## Installation

These instructions have been tested to work on Debian GNU/Linux 7.0 "Wheezy".

You will need to set up a virtualenv for Python 2.x:

    sudo apt-get install python-virtualenv
    virtualenv lpstats-env
    cd lpstats-env
    source bin/activate
    git clone https://github.com/manuelkiessling/lpstats ./app
    cd app
    python setup.py develop
    python server.py

You can now open your browser at http://localhost:8080/


## License

    Copyright (c) 2013, Manuel Kiessling
    
    All rights reserved.
    
    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
    
    - Redistributions of source code must retain the above copyright notice, this
      list of conditions and the following disclaimer.
    - Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    - Neither the name of Manuel Kiessling nor the names of his contributors may
      be used to endorse or promote products derived from this software without
      specific prior written permission.
    
    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
    ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The Leanpub logo and the names of all Leanpub products and/or services are
either trademarks or service marks, or registered trademarks and/or service
marks of Ruboss and all rights are reserved therein by Ruboss.
