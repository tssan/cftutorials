Title: How to create website using Pelican
Date: 2021-06-28 10:20
Category: Tutorials
Tags: tutorial, pelican, blog

# Prerequisites

Pelican is a static site generator created in Python programming language. So the main requirement is Python language. For this tutorial I'm using Linux based operating system that have Python already installed. Some basic knowledge of how to use terminal will help you but even if you are new to that I will try to write down every command that will be required to complete this tutorial.


> For Windows users I recommend creating virtual machine using virtualbox or WSL (Windows Subsystem for Linux in Windows 10).


After Pelican is installed user can jump right into writting articles and other content. For that any text editor will suffice. I'm using Sublime Text editor.

Customazing blog appearance require knowledge abut **HTML** and **CSS**. Pelican has build in templates system that can be also used to change blog layout and styles. There are ready to use themes for Pelican. (link)

To sum up requirements for this tutorial are:

* Linux based OS, Python3 (optionally on Windows: WSL or Virtualbox)
* Text editor
* Hsting space for your blog files
* Domain

Recommended:

* Terminal basic knowladge

# What will you learn from this tutorial

After this tutorial you will be able to create and install blog website on you hosting account. This is easy and fast way to create web content with minimum technical skills.

# Step 1: Python environment setup

Let's create root folder for our project.

`mkdir myblog`

`cd myblog`

Now we need virtuale environment. I'm using `virtualenv` for this:

`virtualenv -p python3 .venv`

> if `virtualenv` command is not found then you must install it by: `sudo apt install python3-pip` and then `sudo pip3 install virtualenv`

That's it! All preparation is completed. Now we can install Pelican and start using it to create blog!

# Step 2: Installing Pelican

To actually use virtual environemt created in previous step you must activate it by this command:

`. .venv/bin/activate`

After that you should see some kind off indicator that virtualenv is active in your shell prompt (may be different for different shells)

Inside activated venv let's install Pelican:

`pip install "pelican[markdown]"`

You can check if Pelican was installed:

`pelican --version`

# Step 3: Using Pelican's quickstart

Pelican is ready to use. It has build-in quickstart command to speed up setup process. Let's use it, run:

`pelican-quickstart`

There will be few steps that are a basic configuration for your blog. Remember that all of settings below can be changed later on in `pelicanconf.py` file. Let's discuss them step by step:

* `> Where do you want to create your new web site? [.]` - It is a relative path to the content folder. I recommend leave it as default. Just hit ENTER.

* `> What will be the title of this web site?` - Set title for your Blog

* `> Who will be the author of this web site?` - Can be a full name or nickname

* `> What will be the default language of this web site? [en]` - Set correct language. ENTER to leave default `en`

* `> Do you want to specify a URL prefix? e.g., https://example.com   (Y/n)` - If you don't know the http address for your blog yet then skip this setting

* `> What is your URL prefix? (see above example; no trailing slash)` - shows only if (Y) was aswered in previous question, put your blog http address eg.: https://example.com

* `> Do you want to enable article pagination? (Y/n)`

* `> How many articles per page do you want? [10]`

* `> What is your time zone? [Europe/Paris]`

* `> Do you want to generate a tasks.py/Makefile to automate generation and  publishing? (Y/n)`

* `> Do you want to upload your website using FTP? (y/N)` - skip ENTER

* `> Do you want to upload your website using SSH? (y/N)` - skip ENTER

* `> Do you want to upload your website using Dropbox? (y/N)` - skip ENTER

* `> Do you want to upload your website using S3? (y/N)` - y

* `> What is the name of your S3 bucket? [my_s3_bucket]` - set name of S3 bucket for your blog (can be created later)

* `> Do you want to upload your website using Rackspace Cloud Files? (y/N)` - skip ENTER

* `> Do you want to upload your website using GitHub Pages? (y/N)` - y

* `> Is this your personal page (username.github.io)? (y/N)` - skip ENTER


# Step 4: CLI - how to use Pelican's commands

All commands requires a virtualenv to be activated:

`. .venv/bin/activate`

Now there is a `pelican` command ready to use. Before you start anything I encourage you to check all available options by typing `pelican --help`.

There are 2 moste usefull commands:

`pelican content` - this will generate blog website and put it in `output` folder

and

`pelican --listen` - that will start up development server and host generated site that you can check in your browser under `http://127.0.0.1:8000` address


> NOTE: Quickstart generates also Makefile that provides usefull commands like `make devserver` that starts development server that will automatically rebuild after you change any content file.

Great! Now we can actually wirte first article ;)


# Step 5: Managing content - adding first blog entry

To add new content you just need to create files inside `content` folder.

`touch content/my-first-article.md`

I'm choosing `Markdown` format. It is also possible to use `html` files out of the box. To use other formats check [pelican-plugins](https://github.com/getpelican/pelican-plugins).

The sample article file can looks like this:

```markdown
Title: My first article
Date: 2021-07-10 11:00
Category: News

# My header

Sit et magna dolore id consectetur qui sed cillum magna est incididunt veniam laborum.
```

After file is saved you need to use `pelican generate` command to make changes in `output` folder. Refresh your page and check your first article!

# Step 6: Changing Theme



# Step 7: Adding custom CSS style

# Step 8: Deploying site

# Step 8 (A): Using GitHub Pages

# Step 8 (B): Using S3
