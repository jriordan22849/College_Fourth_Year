all_as([]).
all_as([a|Tail]) :- all_as(Tail).


replace_a_b_c([],[]).
replace_a_b_c([a|InTail],[b|OutTail]) :-
              replace_a_b_c(InTail,OutTail).
replace_a_b_c([b|InTail],[c|OutTail]) :-
              replace_a_b_c(InTail,OutTail).
replace_a_b_c([c|InTail],[a|OutTail]) :-
              replace_a_b_c(InTail,OutTail).
replace_a_b_c([X|InTail],[X|OutTail]) :- X\=a, X\=b, X\= c,
              replace_a_b_c(InTail,OutTail).


member(X,[X|T]).
member(X,[H|T]) :- member(X,T).
