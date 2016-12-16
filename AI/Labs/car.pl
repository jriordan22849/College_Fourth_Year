byCar(auckland,hamilton).
byCar(hamilton,raglan).
byCar(valmont,saarbruecken).
byCar(valmont,metz).

byTrain(metz,frankfurt).
byTrain(saarbruecken,frankfurt).
byTrain(metz,paris).
byTrain(saarbruecken,paris).

byPlane(frankfurt,bangkok).
byPlane(frankfurt,singapore).
byPlane(paris,losAngeles).
byPlane(bangkok,auckland).
byPlane(singapore,auckland).
byPlane(losAngeles,auckland).

travel(X,Y) :- byCar(X,Y); byTrain(X,Y); byPlane(X,Y).
travel(X,Y) :- ((byCar(X,Z), write(" " + X + " By car to " + Z + " ") );((byTrain(X,Z), write(" " + X + " By train to " + Z + " ")));(byPlane(X,Z) , write(" " + X + " By plane to " + Z + " "))) , travel(Z,Y),dif(X,Y).
