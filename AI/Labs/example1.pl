cat(fluffy).
cat(lucky).
dog(ben).
hungry(ben).
sunny.
chases(X,Y):-dog(X), cat(Y).
mouse(bob).
mouse(fred).
chases(X,Y):- cat(X), mouse(Y).

