directTrain(forbach,saarbruecken).
directTrain(freyming,forbach).
directTrain(fahlquemont,stAvold).
directTrain(stAvold,forbach).
directTrain(saarbruecken,dudweiler).
directTrain(metz,fahlquemont).
directTrain(nancy,metz).

travel_between(X,Y) :- directTrain(X,Y).
travel_between(X,Y) :- directTrain(X,Z), travel_between(Z,Y).

