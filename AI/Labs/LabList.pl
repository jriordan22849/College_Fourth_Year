%% Exercise 1

%% The list is empty. So, all_as succeeds.

all_as([]).

%% The first element of the list is an a. So, we check whether the
%% rest of the list is also a list containing only a's.

all_as([a|Tail]) :- all_as(Tail).


%% ------
%% Exercise 2


%% If the input list is empty, the output list has
%% to be empty as well.

replace_a_b_c([],[]).

%% If the input list is not empty, there are four cases.
%% First case: the first element is an a. The first element
%% of the output list has to be a b. OutTail should be what
%% you get what properly replacing all a's, b's, and c's in InTail.

replace_a_b_c([a|InTail],[b|OutTail]) :-
              replace_a_b_c(InTail,OutTail).

%% Second case: the first element is a b.

replace_a_b_c([b|InTail],[c|OutTail]) :-
              replace_a_b_c(InTail,OutTail).

%% Third case: the first element is a c.

replace_a_b_c([c|InTail],[a|OutTail]) :-
              replace_a_b_c(InTail,OutTail).

%% Fourth case: the first element is something else.

replace_a_b_c([X|InTail],[X|OutTail]) :- X\=a, X\=b, X\= c,
              replace_a_b_c(InTail,OutTail).
