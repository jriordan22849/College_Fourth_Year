sits_left_of(ron,natalie).
sits_left_of(hermoine,ron).
sits_left_of(harry,hermoine).
sits_left_of(colin,harry).
sits_left_of(seamus,colin).
sits_left_of(angelina,seamus).
sits_left_of(ginny,angelina).
sits_left_of(dean,ginny).
sits_left_of(dennis,dean).
sits_left_of(lee,dennis).
sits_left_of(george,lee).
sits_left_of(fred,george).
sits_left_of(alicia,fred).
sits_left_of(nevel,alicia).
sits_left_of(lavender,nevel).
sits_left_of(parvati,lavender).
sits_left_of(katie,parvati).


are_neighbours(X,Y,Z) :-  sits_left_of(X,Z), sits_left_of(Z,Y).
next_to_each_other(X,Y) :- sits_left_of(X,Y); sits_left_of(Y,X).


