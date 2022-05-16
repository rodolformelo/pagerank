# Pagerank
Google's page rank is a historical algorithm. Published in 1998 by Pager and Brin, it was the first method used by Google Search to measure the relative importance of a certain webpage in its search engines. Although it is not currently used by Google Search, it is yet a well-used metric to calculate node importance in a Graph.

As part of 2022 Bocconi's Computer Science (Algorithms) Course, I will develop the Page Rank and Personalized Page Rank Algorithms to be applied in a unweighted graph.

## Steps to Complete

Steps to finish the project:
- [x] Implement Page Rank Algorithm
- [ ] Implement Personalized Page Rank
- [ ] Jupyter Tutorial
- [ ] Readme usage
- [ ] Test the results

## Page Rank Algorithm
 The pseudocode implemented here for page rank using Power Iteration with dead ends is:

__INPUT__ : row normalized adjacency matrix A, teleport probability p, error tolerance epsilon.

__OUTPUT__: page rank score r.
1. Set uniform vector 'v' to 1/n 1
2. Initialize rank vector 'r' with uniform vector 'v'
3. __Repeat__:
4. r &larr; (1 - p) Ã.T r<sub>last</sub>
5. S &larr;  &sum;<sub>i</sub> r<sub>i</sub>
6. r &larr; r + (1 - S)r
7. &delta; &larr; ||r - r<sub>last</sub>||<sub>1</sub>
8. __Until__ &delta; < &epsilon;
9. __Return__ page rank vector __r__
## Reference

Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). The PageRank citation ranking: Bringing order to the web. Stanford InfoLab.

Wikipedia contributors. (2022, May 11). PageRank. In Wikipedia, The Free Encyclopedia. Retrieved 23:20, May 14, 2022, from https://en.wikipedia.org/w/index.php?title=PageRank&oldid=1087243583

## License
[MIT](https://choosealicense.com/licenses/mit/)