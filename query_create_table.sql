create database proj1; -- create database

USE proj1;

create table vaccinate(
	S_VC_DT CHAR(10) PRIMARY KEY
	, FIR_SUB	INT
	, FIR_INC1 INT
	, FIR_INC INT
	, FIR_INC_RATE FLOAT
	, SCD_INC1 INT
	, SCD_INC INT
	, SCD_INC_RATE FLOAT
	, ADD_INC1 INT
	, ADD_INC INT
	, ADD_INC_RATE FLOAT
	, ADD_SUB INT
)

CREATE TABLE corona3 (
	서울기준일 VARCHAR(15) PRIMARY KEY ,
   서울시확진자 INT(11),
   서울시추가확진 INT(11),
   서울시치료중 INT(11),
   서울시퇴원 INT(11),
   서울시추가퇴원 INT(11),
   서울시사망 INT(11) ,
   서울시의심환자전체 INT(11),
   서울시의심환자검사중 INT(11) ,
   서울시검사결과_음성 INT(11),
   전국기준일 VARCHAR(15),
   전국확진 INT(11) ,
   전국추가확진 INT(11) ,
   전국치료중 INT(11) ,
   전국퇴원 INT(11),
   전국사망 INT(11),
   전국의심환자전체 INT(11),
   전국의심환자검사중 INT(11),
   전국의심환자검사결과_음성 INT(11),
   자가격리자해외입국자감시중 INT(11),
   자가격리자해외입국자감시해제 INT(11),
   자가격리자접촉자감시중 INT(11),
   자가격리자접촉자감시해제 INT(11),
   확인중확진자 INT(11)
)