/*
 * Jonathan Riordan
 *
 */
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

parent_of(paul, petunia).
parent_of(helen,petunia).
parent_of(paul, lili).
parent_of(helen,lili).
parent_of(albert,james).
parent_of(ruth, james).
parent_of(lili, harry).
parent_of(james,harry).
parent_of(vernon, dudley).
parent_of(petunia, dudley).


father_of(X,Y) :- male(X), parent_of(X,Y).
mother_of(X,Y) :-  female(X), parent_of(X,Y).
grandfather_of(X,Y) :- male(X), father_of(X,Z), parent_of(Z,Y).
grandmother_of(X,Y) :- female(Y), mother_of(X,Z), parent_of(Z,Y).
sister_of(X,Y) :-  father_of(Z,Y), father_of(Z,X), dif(X,Y).
aunt_of(X,Y) :- female(X), sister_of(X,Z), parent_of(Z,Y).


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
path(X,Y) :- connected(X,Z),
             path(Z,Y).

