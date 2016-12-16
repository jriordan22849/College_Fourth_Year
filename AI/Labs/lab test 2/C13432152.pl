%% Jonathan Riordan
%% C13432152
%% Lab Test 2.

%% Question 1.
connected(a,b,10).
connected(b,c,5).
connected(b,d,5).
connected(f,e,15).
connected(e,d,10).
connected(d,g,5).
connected(g,h,10).
connected(g,i,15).

conc([], L, L).
conc([X|L1],L2,[X|L3]):-conc(L1,L2,L3).


route(X,Y,Z) :- connected(X,Y,Z).
route(X,Y,Z) :- connected(X,Q,Z),conc(X,Q,Z).

distance(X,Y,Z) :- connected(X,Y,Z).
distance(X,Y,Z) :- connected(X,Q,Z),distance(Q,Y,Z).

%% Question 2
fn(X,Y) :- X < 0, Y is 1.
fn(X,Y) :- X >= 100, Y is X.
fn(X,Y) :- X >= 0, X < 100, J is X + 1, fn(J,Y).