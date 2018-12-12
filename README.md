# Trainfuck

Trainfuck is a interpreter based on the
[Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) language, but the Trainfuck
language differs in a few ways:

* Numbers! Instead of writing `++++++++++`, you can write `+10`. This also works
    for `-`, `>`, and `<`.
* One more output char: `:`! Colon prints the numerical value of the cell instead
    of the ASCII representation.
* It doesn't have comma. It's not really needed is it?

## How to run

The only part of this README you will read:

```
./trainfuck.py <filename>
```

For the file extension I like to use `.tf` (if Brainfuck is `.bf`). But don't let
that stop you from using something more fun, like `.trainfuck`.

## Hello World

```
+8[>+4[>++>+3>+3>+<4-]>+>+>->>+[<]<-]>>.>-3.+7..+3.>>.<-.<.+3.-6.-8.>>+.>++.
```
It also supports:
```
++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.
```
or any variations.

## Compatibility with Brainfuck

Should be able to execute Brainfuck code as long as:

* Code does not rely on Comma.
* Comments don't contain any numbers or colon (Except in a comment at the top
    inside a pair of []'s).
