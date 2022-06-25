'''
# we are creating db for our website once you've written the above commands,
# go to terminal and type "python"
# then write "app.create_all()"
# '''

# class todo(db.Model):
#     sno = db.Column(db.Integer,primary_key=True)
#     title = db.Column(db.String(200),nullable=False)
#     desc = db.Column(db.String(500),nullable=False)
#     date_created = db.Column(db.DateTime,defaut = datetime.utcnow)

#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.title}"

