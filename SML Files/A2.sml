(*---------------------------------------------*)
fun isPrime(n) = let fun f(a) = if n < a*a then true else if n mod a = 0 then false else f(a+1) in f(2) end;
fun findPrimes(n) = let fun f(a,b) = if a*3 > n then (0,0,0) else if isPrime(a) then if isPrime(b) andalso isPrime(n-a-b) then (a,b,n-a-b) else if b > n-a-b then f(a+1,a+1) else f(a,b+1) else f(a+1,a+1) in f(2,2) end;
(*---------------------------------------------*)
fun MAX(a,b)= if a>=b then a else b;
fun maximumValue(n,v,w,W)= let fun iter(0,x) = 0|iter(n,x) = if w(n) > x then iter(n-1,x) else MAX(iter(n-1,x-w(n))+v(n),iter(n-1,x)) in iter(n,W) end;
fun value(1) = 500 |value(2) = 700 |value(3) = 300 |value(4) = 200 |value(5) = 300 |value(n)=0;
fun weights(1) = 40 |weights(2) = 80 |weights(3) = 30 |weights(4) = 50 |weights(5) = 20 |weights(n)=0;
maximumValue(5,value,weights,100);
(*---------------------------------------------*)
fun toString(0) = "0"
|toString(1) = "1"
|toString(2) = "2"
|toString(3) = "3"
|toString(4) = "4"
|toString(5) = "5"
|toString(6) = "6"
|toString(7) = "7"
|toString(8) = "8"
|toString(9) = "9"
|toString(n) = let fun iter(x,c) = if x = 0 then c else iter(x div 10,toString(x mod 10)^c) in iter(n,"") end;
fun convertUnitsRec(a,n,f) = let fun alpha(x,y) = let fun namer(x) = if x = 0 then "" else " "^toString(x)^" "^n(y) in if f(y+1) = 0 then namer(x) else alpha(x div f(y),y+1)^namer(x mod f(y)) end in alpha(a,0) end;
fun convertUnitsIter(a,n,f) = let fun alpha(x,y,c) = let fun namer(x) = if x = 0 then "" else " "^toString(x)^" "^n(y) in if f(y+1) = 0 then namer(x)^c else alpha(x div f(y),y+1,namer(x mod f(y))^c) end in alpha(a,0,"") end;
(*---------------------------------------------*)
fun intsqrt(n) = let val b = let fun alpha(b) = if b > n div 4 then b else alpha(4*b) in alpha(1) end in let fun iter(x,z) = if z = 1 then x else if (2*x+1)*(2*x+1) > n div (z div 4) then iter(2*x,z div 4) else iter(2*x + 1,z div 4) in iter(1,b) end end;
intsqrt(472364567);