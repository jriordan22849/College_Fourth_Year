contains(katrina,olga).
contains(olga, natsha).
contains(natsha, irina).

is_in(X,Y) :- contains(X,Y).
is_in(X,Y) :- contains(X,Z), is_in(Z,Y).

