TYPE
TYP_FB_Std : STRUCT
CTRL : FB_Std_CTRL;
STS : FB_Std_STS;
PRM : FB_Std_PRM;
END_STRUCT;

FB_Std_CTRL : STRUCT
Manual_Mode_on : BOOL; (*Comment*)
Manual_Forward : BOOL; (*Comment*)
Manual_Backward : BOOL; (*Comment*)
Automatic_Forward : BOOL; (*Comment*)
Automatic_Backward : BOOL; (*Comment*)
END_STRUCT;

FB_Std_STS : STRUCT
O_Forward_on : BOOL; (*forward*)
O_Backward_on : BOOL; (*backward*)
Error_MSS : BOOL; (*error*)
Status : INT; (*status*)
Objektname : STRING[50]; (*Objektname für Visu*)
END_STRUCT;

FB_Std_PRM : STRUCT
Dummy : REAL; (*Dummy*)
END_STRUCT;

END_TYPE
