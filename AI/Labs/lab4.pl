male(paul).
male(albert).
male(vernon).
male(james).
male(dudley).
male(harry).
female(helen).
female(ruth).
female(petunia).
female(lili).

parentOf(hugo,albert).
parentOf(mary,albert).
parentOf(paul,petunia).
parentOf(helen,petunia).
parentOf(paul,lili).
parentOf(helen,lili).
parentOf(albert,james).
parentOf(ruth,james).
parentOf(lili,harry).
parentOf(james,harry).
parentOf(vernon,dudley).
parentOf(petunia,dudley).



fatherOf(X,Y) :- male(X),
	parentOf(X,Y).

motherOf(X,Y) :- female(X),
	parentOf(X,Y).


grandfatherOf(X,Y) :- fatherOf(X,Z),parentOf(Z,Y).
grandmotherOf(X,Y) :- motherOf(X,Z),parentOf(Z,Y).
sisterOf(X,Y):- female(X), motherOf(Z,X), motherOf(Z,Y), dif(X,Y).
uncle_of(X,Y) :- male(X), motherOf(Z,X), motherOf(Z,Y), dif(X,Y).
auntOf(X,Y) :- sisterOf(X,Z), parentOf(Z,Y).
great_grand_parent(X,Y) :- parentOf(X,Z), parentOf(Z,A), parentOf(A,Y).


ancestor_of(X,Y) :- parentOf(X,Y).
ancestor_of(X,Y) :- parentOf(X,Z), ancestor_of(Z,Y).


connected(1,2).
connected(3,4).
connected(5,6).
connected(7,8).
connected(9,10).
connected(12,13).
connected(13,14).
connected(15,16).
connected(17,18).
connected(19,20).
connected(4,1).
connected(6,3).
connected(4,7).
connected(6,11).
connected(14,9).
connected(11,15).
connected(16,12).
connected(14,17).
connected(16,19).

path(X,Y) :- connected(X,Y).
path(X,Y) :- connected(X,Z), path(Z,Y).
