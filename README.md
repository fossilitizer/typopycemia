# Typopycemia
A cmomnad line tool for ionrtdnciug large qtuanities of tyops into a text srteam while mantiiianng oevlarl word shpae and making the reader belviee that they're reaidng porper Engilsh

# Usage
On a raw string
```bash
$ python typopycemia.py "Hello, World!"
Hlelo, Wlrod!
```
On a file (any valid file path will apply the filter to the file)
```bash
$ python typopycemia.py example/bee-movie.txt
NRARTAOR: 

(Baclk srceen with txet; The snuod of bzuznig bees can be herad) 
Acndcirog to all known lwas 

of aatvioin, 


trhee is no way a bee 
suolhd be able to fly. 
... snip ...
```

With Pipes:


### Options
#### -d, --doubles: Preserve Doubles
This flag will tell the algorithm to keep double letters together, this is done by joining them in the buffer before shuffling:
```python
'hello'
['h', 'e', 'l', 'l', 'o'] -> ['h', 'e', 'll', 'o']
```
#### -b, --birfucate: Bifurcate the word before shuffling
This flag allows you to keep letters from being shuffled across the midpoint of the word
```python
'adhominem'
['a', 'd', 'h', 'o', 'm', 'i', 'n', 'e', 'm']
-> 
['a', 'd', 'h', 'o', 'm'] + ['i', 'n', 'e', 'm']]
```
The `-d` flag will always run first, so a `typopycemia -d -b <input>` call will bifrucate the words *after* the dual letters are joined

These flags are instroduced to try and make the effect more general by allowing a more strict preservation of word shape according to the [research done by Graham Rawlinson](https://www.mrc-cbu.cam.ac.uk/people/matt.davis/Cmabridge/rawlinson/).