TYPE
TYP_FB_Std : STRUCT
	CTRL : FB_Std_CTRL;
	STS : FB_Std_STS;
	PRM : FB_Std_PRM;
END_STRUCT;

FB_Std_CTRL : STRUCT
	Dummy : BOOL; (*Dummy*)
END_STRUCT;

FB_Std_STS : STRUCT
	Dummy : BOOL; (*Dummy*)
END_STRUCT;

FB_Std_PRM : STRUCT
	Dummy : REAL; (*Dummy*)
END_STRUCT;

END_TYPE
