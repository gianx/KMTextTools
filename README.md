KMTextTools
===========

## Description

KMTextTools is a [Keyboard Maestro](http://www.keyboardmaestro.com/) macro I use on a daily basis to manage text. 

## Usage

Install it in [Keyboard Maestro](http://www.keyboardmaestro.com/) then select a text and press SHIFT+CONTROL+OPTION+COMMAND+T (you can change the shortcut editing your macro).

A window will pop-up showing you all the transformations you can apply to your selected text.

Now we assume to have highlited the following text (without quotes):

"the quick brown fox 
jumps over the lazy dog"

And following the oputput copyed to the system clipboard command by command

### Echo

the quick brown fox 
jumps over the lazy dog

### Capitalize all text

THE QUICK BROWN FOX 
JUMPS OVER THE LAZY DOG

### Capitalize only first letter

The quick brown fox 
jumps over the lazy dog

### Capitalize every first letter

The Quick Brown Fox 
Jumps Over The Lazy Dog

### Lowercase

The Quick Brown Fox 
Jumps Over The Lazy Dog

### Contrary

god yzal eht revo spmuj
 xof nworb kciuq eht

### Contrary by line

xof nworb kciuq eht
god yzal eht revo spmuj

### Reverse lines

jumps over the lazy dog
the quick brown fox

### Count lines

2

### Count words

9

### Prepare list for Oracle IN statement 

This option is useful when you have a list and want to transform it in a string useful for Oracle statements.

For exemple if you have this list:

PEAR
APPLE
ORANGE
BANANA

you obtain 

('PEAR','APPLE','ORANGE','BANANA')

### Replace newline with space

Easy to understand. Consider the list above.

The output is:

PEAR APPLE ORANGE BANANA

@2013 Gianluca Nieri, GNU GPL v2 licence
