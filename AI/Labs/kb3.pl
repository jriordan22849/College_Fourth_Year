father(albert,james).
father(james,harry).
father(adam, john).
mother(ann, john).
mother(ruth,james).
mother(lili,harry).


wizard(lili).
wizard(ruth).
wizard(albert).
wizard(ann).
wizard(X) :-
	father(Y,X),
	wizard(Y);
	mother(Z,X),
	wizard(Z).
