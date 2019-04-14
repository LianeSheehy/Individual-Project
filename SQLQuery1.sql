#select * from TBL_D17125670;
cursor.execute("select id, name from tbl_D17125670") 

row = cursor.fetchone() 

if row: 

    print(row)
##########################################

while True:
    row = cursor.fetchone()
    if not row:
        break
    print('id:', row.id)
##########################################
cursor.execute("select id, name from tbl_D17125670")
rows = cursor.fetchall()
for row in rows:
    print(row.id, row.name)
    
##########################################
insert into tbl_D17125670
(ID,NAME, AGE, ROLE, NOTES) 
VALUES(6, 'Carlos', 57, 'Office Boy',null) 


insert into tbl_D17125670
(ID,NAME, AGE, ROLE, NOTES) 
VALUES(7, 'Mary', 36, 'IT',null)

insert into tbl_D17125670
(ID,NAME, AGE, ROLE, NOTES) 
VALUES(8, 'Ton', 57, 'Office Boy',null)

#########################################
cursor.execute("delete from tbl_D17125670 where id = ?", '8')
print(cursor.rowcount, 'tbl_D17125670 deleted')
cnxn.commit()

#########################################
