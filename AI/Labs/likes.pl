likes(dan, lilly).
likes(martin,laura).
likes(john, mary).
likes(mary,john).

dating(X,Y) :- likes(X,Y), likes(Y,X).

p([H|T],X,T).

%%Exercise 1.
all_as([]).
all_as([a|Tail]) :- all_as(Tail).



%% to run. replace_a_b_c([a,b,c],X).
replace_a_b_c([],[]).

%% If the input list is not empty, there are four cases.
%% First case: the first element is an a. The first element 
%% of the output list has to be a b. OutTail should be what
%% you get what properly replacing all a's, b's, and c's in InTail'.

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



%% Operations in lists.
member(X,[X|Tail]).
member(X,[Head|Tail]) :- member(X,Tail).


%% concatenation 
conc([], L, L).
conc([X|L1],L2,[X|L3]):-conc(L1,L2,L3).

%% deletion
del(X,[X|Tail],Tail).
del(X,[Y|Tail],[Y|Tail1]):-del(X,Tail,Tail1).

%%sublist/2 Solution

sublist(S,L):-conc(L1,L2,L),conc(S,L3,L2).


%% arithmetic 
min(X,Y,Z) is true if Z is the minimum of X and Y min(X,Y,X) :- X<Y.
min(X,Y,X) :- X<Y.
min(X,Y,Y) :- X>=Y.

%% if the minimum is greater than 0.


%% successor 
successor(X,Y) :- Y is X + 1.

addNumbers(X,Y,Z) :- Z is X + Y.

%% successor           
minus(X,Y) :- Y is X - 1.


addthree(X,Y) :- Y is (X + 3) * 2.

%% increment
increment(X,Y) :- Y is X + 1.

%% signum
signum(X,Y):- X>0, Y is X-1 ; Y is 0. 

%% max two numbers
max_numbers(X,Y,X) :- X > Y.
max_numbers(X,Y,Y) :- Y >= X.

%% max of three numbers
max_of_three(X,Y,Z,J).

%% absolute
absolute(X,Y):- X>=0, Y is X.
absolute(X,Y):- Y is X * -1.



%% list member of.
member2(X, [X|T]).
member2(X, [H|T]) :- member2(X,T).


%% loop 1, 2, 3
sum_list([], 0).
sum_list([H|T], Sum) :- sum_list(T, Rest), Sum is H + Rest.

%% loop 1, 2, 3

len([],0).
len([_|T],N) :-	len(T,M), N is M+1.

%% average 
average_list([],0).
average_list(L,X) :- sum_list(L,P), len(L,W), X is P / W.

%% sort list 
quick_sort2(List,Sorted):-q_sort(List,[],Sorted).
q_sort([],Acc,Acc).
q_sort([H|T],Acc,Sorted):-
    pivoting(H,T,L1,L2),
    q_sort(L1,Acc,Sorted1),q_sort(L2,[H|Sorted1],Sorted).

%% reverse list
reverse_list([],Z,Z).
reverse_list([H|T],Z,Acc) :- reverse_list(T,Z,[H|Acc]).



prefix(P,L):- conc(P,_,L).
suffix(S,L):- conc(_,S,L).
sublist(SubL,L):- suffix(S,L), prefix(SubL,S).