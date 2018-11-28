FUNCTION_BLOCK FB_Std
VAR_INPUT
Enable : BOOL; (*Bausteinfreigabe*)
MSS : BOOL; (*MSS OK*)
END_VAR
VAR_OUTPUT
O_Forward : BOOL; (*Forderband vorwaerts ein*)
O_Backward : BOOL; (*Forderband rueckwaerts ein*)
END_VAR
VAR_IN_OUT
ObjectStruct : TYP_FB_Std; (*Type of FB Std*)
END_VAR
END_FUNCTION_BLOCK