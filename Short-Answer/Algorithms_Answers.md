#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n)


b) Linearithmic O(n log n)


c) Linear O(n)

## Exercise II


```

- unknown building height
- if at f or higher floor, the eggs will break
- find f with minimal broken/dropped eggs

We can drop an egg at each floor and test if it gets broken as we go up the building.
This will give us as many dropped eggs as it takes to get to f, but there will be many dropped eggs if f is a high number.

We have a kind of a sorted list, given we have a building with n floors in acending order. We also have a target value, which is f. This would mean that we could do a binary search for f. 

    We would start at the middle of the building and drop and egg off, if the egg breaks then we know we're past the point and we can set that as our new high point and vice versa if it does not break. 
    
    After we have our new limit we can reset our mid point by adding our low to our high point and diving by two, then dropping an egg at this point. We would repeat this process until our target floor minus 1 does not break an egg.

    This process would signifigantly reduce the amount of broken and dropped eggs.

    I believe this would result in a Logarithmic run time

````
