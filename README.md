# Trainfuck.py

Trainfuck.py is a interpreter that interprets the Trainfuck language which is derived from the
[Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) language, but the Trainfuck
language differs in a few ways:

* Numbers! Instead of writing `++++++++++`, you can write `+10`. This also works
    for `-`, `>`, `<`, `.`, and `:`.
* One more output char: `:`! Colon prints the numerical value of the cell instead
    of the ASCII representation.
* `@` sets the data pointer to `0`. So you can can go to any numbered cell from anywhere using ie. `@>200`.
* It doesn't have `,`. It's not really needed is it?

## How to run

You will need Python 3. That's it.

```
python trainfuck.py <filename>
```
or just
```
./trainfuck.py <filename>
```

For the file extension I like to use `.tf` (if Brainfuck is `.bf`). But don't let
that stop you from using something more fun, like `.trainfuck`.

## Hello World

```
+72.+29.+7..+3.-67.-12.+55.+24.+3.-6.-8.-67.-23.
```
It also supports:
```
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```
or any variations.

## More examples

Take advantage of calculating with big* numbers!

(*Maximum number is 255.)

Multiplication:
```
+20[->+11<]>:
```

Divition:
```
+150[-25>+<]>:
```

## Compatibility with Brainfuck

Trainfuck is to Brainfuck what C++ is to C: able to interpret the code of its predecessor. Of course not perfectly because that would be boring. Should be able to execute Brainfuck code as long as:

* Code does not rely on Comma.
* Comments don't contain any numbers or colon (Except in a comment at the top
    inside a pair of []'s).
