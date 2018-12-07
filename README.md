# Temporal-Link-Prediction-and-Community-Detection
Final Project for Analysis of Network Data (CSE416a). 

* Who:  	Yushu Liu, Ighor Tavares, Erik Tomasic 
* What: 	Study link prediction and community detection within a company’s email network.
* Why: 	This dataset has temporal information, which allows us to analyze another aspect of the attempted tasks, and compare predicted to actual results.
* How: 	We are planning to use various algorithms at different points in time to study their performances with different amounts of data. One way is with common neighbor algorithm or/and SimRank algorithms for community detection (similar nodes are referenced by similar nodes).
* Resources:
Dataset(s) (including link/resource)
email-Eu-core temporal network: http://snap.stanford.edu/data/email-Eu-core-temporal.html
email-Eu-core network: http://snap.stanford.edu/data/email-Eu-core.html
email-EuAll network (includes emails outside institution): http://snap.stanford.edu/data/email-EuAll.html
* Notes: The network of our choosing was generated using email data from 
a large European research institution. The emails only represent 
communication between institution members (the core) and the
dataset does not contain incoming messages from or outgoing 
messages to the rest of the world. A directed edge (u,v,t) means 
that person u sent an email to person v at time t.  Finding 
communities within a research institution based on email
exchange is one of our goals. 



