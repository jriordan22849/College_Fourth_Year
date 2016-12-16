wizard(harry).
scare(Hagrid,Dudley).
magical(X) :- wizard(X).
hate(Vermon,X) :- magical(X).
hate(Petunia,X) :- scare(X,Dudley).
