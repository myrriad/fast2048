seq(0,X,1,16)->|LG2048
1->|LG2048(1)
|LG2048
prgmD2048
1->E
While E
	getKey
	Repeat max(Ans={24,25,26,34
	getKey
	End
	Ans->K

	|LG2048
	If K=25
	{Ans(1),Ans(5),Ans(9),Ans(13),Ans(2),Ans(6),Ans(10),Ans(14),Ans(3),Ans(7),Ans(11),Ans(15),Ans(4),Ans(8),Ans(12),Ans(16)}
	If K=26
	{Ans(4),Ans(3),Ans(2),Ans(1),Ans(8),Ans(7),Ans(6),Ans(5),Ans(12),Ans(11),Ans(10),Ans(9),Ans(16),Ans(15),Ans(14),Ans(13)}
	If K=34
	{Ans(13),Ans(9),Ans(5),Ans(1),Ans(14),Ans(10),Ans(6),Ans(2),Ans(15),Ans(11),Ans(7),Ans(3),Ans(16),Ans(12),Ans(8),Ans(4)}
	prgmS2048
	prgmM2048
	If K=25
    {Ans(1),Ans(5),Ans(9),Ans(13),Ans(2),Ans(6),Ans(10),Ans(14),Ans(3),Ans(7),Ans(11),Ans(15),Ans(4),Ans(8),Ans(12),Ans(16)}

	If K=26
	{Ans(4),Ans(3),Ans(2),Ans(1),Ans(8),Ans(7),Ans(6),Ans(5),Ans(12),Ans(11),Ans(10),Ans(9),Ans(16),Ans(15),Ans(14),Ans(13)}
	If K=34
	{Ans(4),Ans(8),Ans(12),Ans(16),Ans(3),Ans(7),Ans(11),Ans(15),Ans(2),Ans(6),Ans(10),Ans(14),Ans(1),Ans(5),Ans(9),Ans(13)}

	Ans->|LG2048

	cumSum(not(|LG2048))->|LTEMP
	|LTEMP(16)
	If Ans=0
		0->E

	randInt(1,Ans)

	If randInt(0,3)=0
	Then
	2->|LG2048(sum(|LTEMP<Ans)+1)
	Else
	1->|LG2048(sum(|LTEMP<Ans)+1)
	End

	|LG2048
	prgmD2048
End
