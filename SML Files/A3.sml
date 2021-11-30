fun LgintToInt(X)=
  if length(X)>9 then 1000000000
  else
    let
      fun iter([],y,z) = y
        |iter(x::xs,y,z) = iter(xs,(x*z) +y,10*z)
    in iter(X,0,1) end
fun intToLgint(n)=
  if n div 10 = 0 then [n]
  else (n mod 10)::intToLgint(n div 10)
fun addLgint(L1,L2) =
  let fun iter([],[],0) = []
    |iter([],[],c) = [c]
    |iter([],x::xs,c) = ((x+c) mod 10)::iter([],xs,((x+c) div 10))
    |iter(y,[],c) = iter([],y,c)
    |iter(x::xs,y::ys,c) = ((y+x+c) mod 10)::iter(xs,ys,((y+x+c) div 10))
  in iter(L1,L2,0) end
fun LgLesseq(L1,L2) =
  let fun iter([],[],c) = c
    |iter([],y,c) = true
    |iter(x,[],c) = false
    |iter(x::xs,y::ys,c) =
      if x=y then iter(xs,ys,c)
      else iter(xs,ys,x<y)
  in iter(L1,L2,true) end
fun multiplyLgint(L1,L2) =
  let fun multiply1(L,x) =
    let fun iter([],0) = []
      |iter([],c) = (c mod 10)::iter([], c div 10)
      |iter(x::xs,c) = ((x+c) mod 10)::iter(xs, (x+c) div 10)
    fun mapx([]) = []
        |mapx(y::ys) = (x*y)::mapx(ys)
    in iter(mapx(L),0) end
  in
    let fun iter(x,[],c) = c
    |iter(x,y::ys,c) = iter(0::x,ys,addLgint(multiply1(x,y),c))
    in iter(L1,L2,[]) end
  end;
fun qPerformance(L) =
  let val (q1,q2,q3,q4,q5) =
    let fun sum((a1,a2,a3,a4,a5),(b1,b2,b3,b4,b5)) = (a1+b1,a2+b2,a3+b3,a4+b4,a5+b5)
    in foldl sum (0,0,0,0,0) L end
  val leng = length(L)
  fun hike(x1,x2,x3,x4,x5) =
    let fun q(1) = q1 |q(2) = q2 |q(3) = q3 |q(4) = q4 |q(x) = 0
    fun x(1) = x1 |x(2) = x2 |x(3) = x3 |x(4) = x4 |x(n) = 0
      in
        let fun qhike(n) =
          let fun iter(l,m) = if 10*leng*(x(n)) < l*(q(n)) then m else iter(l+1,m+1)
          in iter(11,0) end
        in (x5*(qhike(1)+qhike(2)+qhike(3)+qhike(4)+100)) div 100 end
      end
  in map hike L end
fun budgetRaise(L) =
  let fun sum1(a,b) = a+b
    fun sum2((a1,a2,a3,a4,a5),b) = a5+b
    val x = foldl sum2 0 L
    val y = foldl sum1 0 (qPerformance(L))
  in (real(y)/real(x))-1.0 end;
fun lexicographicPerm(li:char list) =
  let val Li =
    let fun sort([])=[]
      |sort([x])=[x]
      |sort(L) =
      let fun split([])=([],[])
        |split([a])=([a],[])
        |split(x::y::z)=
          let val (a,b) = split(z)
      in (x::a,y::b) end
      fun merge(l1,[]) = l1
        |merge([],l2) = l2
        |merge(x::l1,y::l2) =
          if x<y then x::merge(l1,y::l2)
          else y::merge(x::l1,l2)
      val (L1,L2) = split(L)
      in merge(sort(L1),sort(L2)) end
    in sort(li) end
  fun Perm([]) = [[]]
    |Perm([a]) = [[a]]
    |Perm(L) =
    let fun nlexi(n) =
      let fun lexilist(n) =
        let fun iter(i,[]) = raise Empty
          |iter(i,x::xs) =
          if i = n then (x,xs)
          else
            let val (a,b) = iter(i+1,xs)
            in (a,x::b) end
        val (a,b) = iter(0,L)
        in (a,Perm(b)) end
      fun append(a,[]) = []
        |append(a,x::xs) = (a::x)::(append(a,xs))
      in append(lexilist(n)) end
    fun iterater(i) =
      if i = length(L) then []
      else (nlexi(i))@(iterater(i+1))
    in iterater(0) end
  in Perm(Li) end;
fun lexicographicPermDup(li:char list) =
  let val Li =
    let fun sort([])=[]
      |sort([x])=[x]
      |sort(L) =
      let fun split([])=([],[])
        |split([a])=([a],[])
        |split(x::y::z)=
          let val (a,b) = split(z)
      in (x::a,y::b) end
      fun merge(l1,[]) = l1
        |merge([],l2) = l2
        |merge(x::l1,y::l2) =
          if x<y then x::merge(l1,y::l2)
          else y::merge(x::l1,l2)
      val (L1,L2) = split(L)
      in merge(sort(L1),sort(L2)) end
    in sort(li) end
  fun Perm([]) = [[]]
    |Perm([a]) = [[a]]
    |Perm(L) =
    let fun nlexi(n) =
      let fun lexilist(n) =
        let fun iter(i,[]) = raise Empty
          |iter(i,x::xs) =
          if i = n then (x,xs)
          else
            let val (a,b) = iter(i+1,xs)
            in (a,x::b) end
        val (a,b) = iter(0,L)
        in (a,Perm(b)) end
      fun append(a,[]) = []
        |append(a,x::xs) = (a::x)::(append(a,xs))
      in append(lexilist(n)) end
    val Leng = length(L)
    fun nterm(n) =
      let fun iter(i,[]) = raise Empty
        |iter(i,x::xs) =
        if i = n then x
        else iter(i+1,xs)
      in iter(0,L) end
    fun iterater(i) =
      if i = Leng then []
      else
        if i = Leng - 1 then (nlexi(i))
        else
        if (nterm(i))=(nterm(i+1)) then (iterater(i+1))
        else (nlexi(i))@(iterater(i+1))
    in iterater(0) end
  in Perm(Li) end;
