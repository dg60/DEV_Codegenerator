//***********************************************
// Codegenerator BuR V0.9.0
// by dgrill
// http://www.dgrill.at
// dgrill@dgrill.at
// Date of generation: 28.11.2018 22:22
//***********************************************

//***********************************************
// Foerderband 1   =HV1+M1
//***********************************************
FB1(
	Enable := True,
	MSS := True,
	O_Forward := "O_10_0",
	O_Backward := "O_11_0",
	ObjectStruct := "DB_FB_Std".FB1);

//***********************************************
// Foerderband 2  =HV1+M2
//***********************************************
FB2(
	Enable := True,
	MSS := True,
	O_Forward := "O_10_1",
	O_Backward := "O_11_1",
	ObjectStruct := "DB_FB_Std".FB2);

//***********************************************
// Foerderband 3  =HV1+M3
//***********************************************
FB3(
	Enable := True,
	MSS := True,
	O_Forward := "O_10_2",
	O_Backward := "O_11_2",
	ObjectStruct := "DB_FB_Std".FB3);

//***********************************************
// Foerderband 4  =HV1+M4
//***********************************************
FB4(
	Enable := True,
	MSS := True,
	O_Forward := "O_10_3",
	O_Backward := "O_11_3",
	ObjectStruct := "DB_FB_Std".FB4);

