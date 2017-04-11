# Burrows-Wheeler Encoding


This is just a quick implementation of Burrows-Wheeler encoding.


`bwt(s)` returns the encoded version of the string `s`.


`bwti(e)` returns the decoded version of the string `e`.

# Examples:
```
bwt('Hello, World!') # => ,d!o$ lHrellWo
bwti(',d!o$ lHrellWo')# => Hello, World!

bwt('The quick brown fox jumped over the lazy dog.') # => kynxeder.g$l ie hhpv otTu c uwd rfm eb qjoooza
bwti('kynxeder.g$l ie hhpv otTu c uwd rfm eb qjoooza')# => The quick brown fox jumped over the lazy dog.

bwt('cool beans') # => lse $boaocn
bwti('lse $boaocn')# => cool beans

```