# Pagerank
Google's page rank is a remarkable algorithm. Published in 1998 by Page and Brin, it was the first method used by Google Search to measure the relative importance of a certain webpage in its search engines. Although it is not currently used by Google Search, it is yet a well-used metric to calculate node importance in a Graph.

As part of 2022 Bocconi's Computer Science (Algorithms) Course, I will develop the Page Rank and Personalized Page Rank Algorithms to be applied in a unweighted graph.

## Steps to Complete

Steps to finish the project:
- [x] Implement Page Rank Algorithm
- [ ] Implement Personalized Page Rank
- [ ] Jupyter Tutorial
- [x] Readme usage
- [x] Test the results

## PageRank Algorithm
 The implemented pseudocode for page rank is:

__INPUT__ : row normalized adjacency matrix A, teleport probability p, error tolerance epsilon.

__OUTPUT__: page rank score r.
1. Set uniform vector 'v' to 1/n 1
2. Initialize rank vector 'r' with uniform vector 'v'
3. __Repeat__:
4. r &larr; (1 - p) Ã.T r<sub>last</sub>
5. S &larr;  &sum;<sub>i</sub> r<sub>i</sub>
6. r &larr; r + (1 - S)r
7. &delta; &larr; ||r - r<sub>last</sub>||<sub>1</sub>
8. r<sub>last</sub> &larr; r
9. __Until__ &delta; < &epsilon;
10. __Return__ page rank vector __r__

## Usage
The code can be run with the following command:
```
pagerank.py --indirect False --input_path data/web-Google.txt --output-path output/result.txt 
```
This will compute a page rank score vector for an unweighted directed graph specified by --input-path, and write the vector into the target file in --output-path.The detailed format of the input and output files is described below.

## Input
The default input for Page Rank is represented by the edge list of a graph with the following format:
```
# format: source (int) target (int)
1	3
1	6
1	7
2   1
...
```
Note that the node id should start with 0 and increase by one unit.
## Output
The output format will be a node id list with its respect page rank score.
```
# format: node id (int) page rank score (float)
1 2.071016e-06
2 3.663066e-06
3 7.527511e-07
4 8.633286e-07
...
```
Note that bigger the Graph is, smaller will be its node score, since it has to sum to 1.
## Reference

Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). The PageRank citation ranking: Bringing order to the web. Stanford InfoLab.

Wikipedia contributors. (2022, May 11). PageRank. In Wikipedia, The Free Encyclopedia. Retrieved 23:20, May 14, 2022, from https://en.wikipedia.org/w/index.php?title=PageRank&oldid=1087243583

Langville, A. N., & Meyer, C. D. (2011). Google's PageRank and beyond: The science of search engine rankings. Princeton University Press.

## License
[MIT](https://choosealicense.com/licenses/mit/)