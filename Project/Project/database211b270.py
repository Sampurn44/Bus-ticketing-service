from tkinter import *
from tkinter import messagebox
root = Tk()
import sqlite3
con=sqlite3.Connection("bus_reservation211b270")
cur=con.cursor()
try:
    cur.execute('create table route_details(RID varchar(6),station_name varchar(20), SID int(3), constraint route_pk primary key (RID,SID))')
    cur.execute('create table operator_details(operator_name varchar(40),OID varchar(6) primary key,address varchar(50), phone_number bigint(12), Email varchar(30))')
    cur.execute('create table bus_details(BID varchar(6) primary key,Bus_Type varchar(20),Op_name varchar(35), operator_id varchar(6), route_id varchar(5),seat_capacity smallint(2), fare int(6), constraint fk_oid foreign key (operator_id) references operator(OID), constraint fk_rid foreign key (route_id) references route_details(RID))')
    cur.execute('create table running_details(RBID varchar(6), running_date date, seat_available smallint(2), constraint run_pk primary key(running_date,RBID),foreign key (RBID) references bus_details(BID))')
    cur.execute('create table booking_history(pname varchar(20), gender char(5), age smallint(3),mobile bigint(10) primary key,bus varchar(6) ,travelling_date date,booking_date date,no_of_seats smallint(2),total_fare int(6), booking_ref_number int(5),foreign key (bus) references bus_details(BID))')
except:m=1

try:
    cur.execute('''insert into route_details values('RT1MP1','Guna',1),('RT1MP1','Bina',2),('RT1MP1','Bhopal',3),('RT2MP1','Guna',3),('RT2MP1','Bina',2),('RT2MP1','Bhopal',1),('RT3MP1','Guna',1),('RT3MP1','Sagar',2),('RT3MP1','Indore',3),('RT4MP1','Guna',3),('RT4MP1','Sagar',2),('RT4MP1','Indore',1),('RT1MP2','Vidisha',1),('RT1MP2','Bhopal',2),('RT1MP2','Indore',3),('RT1MP2','Nagpur',4),('RT2MP2','Nagpur',1),('RT2MP2','Indore',2),('RT2MP2','Bhopal',3),('RT2MP2','Vidisha',4),('RT1UP1','Guna',1),('RT1UP1','Jhansi',2),('RT2UP1','Guna',2),('RT2UP1','Jhansi',1),('RT1RJ1','Guna',1),('RT1RJ1','Kota',2),('RT1RJ1','Jaipur',3),('RT2RJ1','Guna',3),('RT2RJ1','Kota',2),('RT2RJ1','Jaipur',1)''')
    cur.execute('''insert into operator_details values('Asif Travels','MPOP1','Lalghati, Bhopal',1234567890,'asiftravels@gmail.com'),('Triphati Bus Service','MPOP2','Hotel Varun, Guna',9876543210,'triphati@gmail.com'),('Shakti Bus','MPOP3','Near Bus Stand, Vidisha',7592236561,'shaktibus@hotmail.com '),('Kamla Travels','MPOP4','Kamla Travels 13,Indore,M.P.',07314090788,'shivys10@gmail.com'),('Amar Travels','MPOP5','Amar travels office rishivihar, Gwalior, M.P.',9425748083,'amartravels12@gmail.com'),('Bharti Tours And Travels','RJOP1','H-79,Lal bagh,Dhyanchand Marg,Kota',9829056423,'info@bhartitours.com'),('Samay Shatabdi Travels','UPOP1','Shatabdi Terminal,Kanpur',7518904313,'help@samayshatabditravels.com')''')
    cur.execute('''insert into bus_details values('MP1B01','AC Seater 2+2','Asif travels','MPOP1','RT1MP1',40,200),('MP1B02','AC Seater 2+2','Asif travels','MPOP1','RT2MP1',40,200),('MP1B0','AC Seater 2+2','Triphati Bus Service','MPOP2','RT1MP1',40,180),('MP1B04','AC Sleeper 2+1','Triphati Bus Service','MPOP2','RT2MP1',40,180),('MP1B05',' NON AC Seater 2+2','Asif Travels','MPOP1','RT1MP1',20,150),('MP1B06','NON AC Seater 2+2','Asif Travels','MPOP1','RT2MP1',20,150),('MP1B07',' NON AC Seater 2+2','SHAKTI Travels','MPOP3','RT3MP1',38,320),('MP1B08','NON AC Sleeper 3+3','Kamla Travels','MPOP4','RT4MP1',30,900),('MP1B09','NON AC Seater 3+3','AMAR TRAVELS','MPOP5','RT1MP2',40,487),('MP1B10','AC Seater 2+1','SHAKTI Travels','MPOP3','RT2MP2',44,380),('UP1B01','AC Seater 2+2','SAMAY SHATABDI','UPOP1','RT1UP1',40,490),('UP1B02','AC Sleeper 3+1','SAMAY SHATABDI','UPOP1','RT2UP1',40,490),('RJ1B01','AC Sleeper 2+1','Bharti Tour And Travels','RJOP1','RT1RJ1',30,900),('RJ1B02','AC Sleeper 2+1','Samay Shatabdi Travels','UPOP1','RT2RJ1',38,1300)''')
    cur.execute('''insert into running_details values('MP1B01','2022-12-01',40),( 'MP1B01','2022-12-02',40),( 'MP1B01','2022-12-03',40),( 'MP1B01','2022-12-04',40),( 'MP1B01','2022-12-05',40),( 'MP1B01','2022-12-06',40),( 'MP1B02','2022-12-01',40),( 'MP1B02','2022-12-02',40),( 'MP1B02','2022-12-03',40),( 'MP1B02','2022-12-04',40),('MP1B03','2022-12-01',38),('MP1B03','2022-12-02',38),('MP1B03','2022-12-04',38),('MP1B03','2022-12-05',38),('MP1B04','2022-12-01',36),('MP1B04','2022-12-03',36),('MP1B04','2022-12-05',36),('MP1B04','2022-12-07',36),('MP1B06','2022-12-02',38),('MP1B06','2022-12-04',38),('MP1B06','2022-12-06',38),('MP1B06','2022-12-08',38),('MP1B07','2022-12-01',38),('MP1B07','2022-12-02',40),('MP1B07','2022-12-03',40),('MP1B07','2022-12-04',40),('MP1B07','2022-12-05',40),('MP1B08','2022-12-01',40),('MP1B08','2022-12-02',38),('MP1B08','2022-12-03',38),('MP1B08','2022-12-04',38),('MP1B08','2022-12-05',38),('MP1B09','2022-12-01',30),('MP1B09','2022-12-02',30),('MP3B09','2022-12-03',0),('MP1B09','2022-12-4',30),('MP0B09','2022-12-05',30),('MP1B10','2022-12-01',40),('MP1B10','2022-12-02',40),('MP1B10','2022-12-03',40),('MP1B10','2022-12-04',40),('MP1B10','2022-12-06',40),('UP1B01','2022-12-01',40),('UP1B01','2022-12-02',40),('UP1B01','2022-12-03',40),('UP1B01','2022-12-04',40),( 'UP1B01','2022-12-05',30),( 'UP1B02','2022-12-01',30),( 'UP1B02','2022-12-02',30),( 'UP1B02','2022-12-03',30),( 'UP1B02','2022-12-04',30),( 'UP1B02','2022-12-05',30),( 'RJ1B01','2022-12-01',38),( 'RJ1B01','2022-12-02',38),( 'RJ1B01','2022-12-03',38),( 'RJ1B01','2022-12-04',38),( 'RJ1B01','2022-12-05',38),('RJ1B02','2022-12-01',30),('RJ1B02','2022-12-02',30),('RJ1B02','2022-12-03',30),('RJ1B02','2022-12-4',30),('RJ1B02','2022-12-05',30)''')
except: n=1

con.commit()
con.close














cur.execute('select * from route_details')
res=cur.fetchall()
print(res)
