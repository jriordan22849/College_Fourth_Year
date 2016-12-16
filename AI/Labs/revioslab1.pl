cat(fluffy).
cat(lucky).
dog(ben).
hungry(ben).
sunny.

woman(mary).
woman(mia).
loves(john,mia).
loves(john,beer).
loves(rob,beer).

chases(X,Y) :- dog(X), cat(Y).
mouse(george).
mouse(rob).
mouse(dylan).

cat_chases(X, Y) :- cat(X), mouse(Y).
