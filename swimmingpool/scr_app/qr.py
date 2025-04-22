@admin.route("/admin_manage_table",methods=['get','post'])
def admin_manage_table():
    data={}
    if 'submit' in request.form:
        table=request.form['table']
        
        
        qry="insert into tables values(null,'%s','pending','pending')"%(table)
        res=insert(qry)
        
        if res:
            o="select * from tables where table_id='%s'"%(res)
            e=select(o)
            if e:
                session['name']=e[0]['table_number']
            qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
            )
            qr.add_data(res)
            qr.make(fit=True)

            # Create an image of the QR code
            img = qr.make_image(fill_color="black", back_color="white")
            rr="static/qr_image/"+ session['name'] +".png" # Save the QR code image to a file
            img.save(rr)
            
            up="update tables set qr_image='%s' where table_id='%s'"%(rr,res)
            update(up)
        
        return '''<script>alert("Added Successfully");window.location='/admin_manage_table'</script>'''