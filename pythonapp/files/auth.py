from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify;
from .models import Record;
from . import db;

auth = Blueprint('auth',__name__)

@auth.route('/create_note',methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        NOTE = request.form.get('note').upper().strip()
        if len(NOTE) > 300:
            flash("Length of Note can't be greater than 300 Characters",category='error')
        else:
            try:
                new_record= Record(note=NOTE)
                db.session.add(new_record)
                db.session.commit()
                flash(' Note Successfully Added...',category='success')
                return redirect(url_for('auth.create_note'))
            except:
                flash('Error Encountered while adding your note... Contact Admin Support',category='error')
    
    return render_template('create_note.html')


@auth.route('/note',methods=['GET', 'POST'])
def note():
    if request.method == 'POST':
        id = request.form.get('note_id')
        data = Record.query.filter_by(id=(id)).first()
        if data:
            return render_template('note_page.html',data=data)
        else:
            flash('Note Id not found', category='error')
            return redirect(url_for('views.noteid'))
    return redirect(url_for('views.home'))    
    
@auth.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        id = request.form.get('note_id')
        note = request.form.get('note').upper().strip()
        status = request.form.get('status').upper().strip()
        noteid = Record.query.filter_by(id=(id)).first()
        if len(note) > 300:
             flash("Length of Note can't be greater than 300 Characters",category='error')
             return redirect(url_for('views.dashboard'))
        else:
            try:
                noteid.note = note
                noteid.status = status
                db.session.commit()    
                flash('Your note has been successfully updated', category='success')
                return redirect(url_for('views.home'))
            except Exception as e:
                flash('There was an error while updating the note', category='error')
                return redirect(url_for('views.home'))
      
    return redirect(url_for('views.home'))

@auth.route('/delete',methods=['POST','GET'])
def delete():
    if request.method == 'POST':
        id = request.form.get('note_id')
        noteid = Record.query.filter_by(id=(id)).first()
        try:
            db.session.delete(noteid)
            db.session.commit()    
            flash('Your note has been successfully deleted', category='success')
            return redirect(url_for('views.home'))
        except:
            flash('There was an error while deleting your note', category='error')
            return redirect(url_for('views.home'))
    return redirect(url_for('views.home'))

@auth.route('/deleteSelected',methods=['POST','GET'])
def deleteSelected():
    if request.method == 'POST':
        payload = request.json['ids']
        if payload:
            payload = payload.split(',')
            try:
                for ids in payload:
                    noteid = Record.query.filter_by(id=(ids)).first()
                    db.session.delete(noteid)
                    db.session.commit()
                response = jsonify('<span class=\'flash green\'>Your note has been successfully deleted</span>')
                response.status_code = 200
                return response
            except:
                response = jsonify('<span class=\'flash red\'>OOPS, an internal error occur during deletion</span>')
                response.status_code = 500
                return response
    return redirect(url_for('views.home'))

# return render_template('note_page.html')
# noteid = int(request.args.get('note_id'))
# if request.method == 'GET': 
    # for x,y in noteid.items():
    #     print(x,y)
    
    # print(noteid)
    
    
# if request.method == 'POST':
    # print(g.notesid)
    # print("hello")
    # return render_template('home.html')
#     note = request.form.get('note').upper().strip()
#     status = request.form.get('status').upper().strip()
#     print(note,status)
    # notesid = int(request.args.get('note_id'))
    # print(notesid)
    # note = request.form.get('note').upper().strip()
    # status = request.form.get('status').upper().strip()
    # 
    # dictData = {
    #     "id" : data.id,
    #     "status" : data.status,
    #     "note" : data.note
    # }
    # jsonData = json.dumps(dictData)
    # print(jsonData)


#     try:
#         noteid.note = note
#         noteid.status = status
#         db.session.commit()    
#         flash('Your note has been successfully updated', category='success')
#         return render_template('home.html')
#     except:
#         flash('There was an error while updating the note')